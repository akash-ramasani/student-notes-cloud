from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from config import Config
from services.db_service import db, User, Note, Class, CourseElement, Material
from services.auth_service import register_user, authenticate_user, verify_user, initiate_forgot_password, confirm_forgot_password
from services.s3_service import upload_file_to_s3
import os
import logging
import watchtower
import boto3

app = Flask(__name__)
app.config.from_object(Config)

# Configure CloudWatch Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("NoteCloud")

try:
    cw_client = boto3.client(
        "logs",
        aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'],
        region_name=app.config['AWS_REGION']
    )
    # Stream to "NoteCloud/Production" log group
    app_handler = watchtower.CloudWatchLogHandler(
        boto3_client=cw_client,
        log_group="NoteCloud",
        stream_name="Production"
    )
    logger.addHandler(app_handler)
    logger.info("CloudWatch logging initialized successfully.")
except Exception as e:
    print(f"Failed to initialize CloudWatch logging: {e}")

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = authenticate_user(username, password)
        if user:
            login_user(user)
            logger.info(f"User login: {username} (Role: {user.role})")
            return redirect(url_for('dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role') # 'student' or 'professor'
        user, msg = register_user(username, email, password, role)
        if user:
            flash(msg, 'success')
            return redirect(url_for('verify', username=username))
        flash(msg, 'error')
    return render_template('register.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    username = request.args.get('username') or request.form.get('username')
    if not username:
        return redirect(url_for('register'))
        
    if request.method == 'POST':
        otp = request.form.get('otp')
        success, msg = verify_user(username, otp)
        if success:
            flash(msg, 'success')
            return redirect(url_for('login'))
        flash(msg, 'error')
        
    return render_template('verify.html', username=username)

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        username = request.form.get('username')
        success, msg = initiate_forgot_password(username)
        if success:
            flash(msg, 'success')
            return render_template('forgot_password.html', step='confirm', username=username)
        flash(msg, 'error')
    return render_template('forgot_password.html', step='initiate')

@app.route('/reset-password', methods=['POST'])
def reset_password():
    username = request.form.get('username')
    code = request.form.get('code')
    password = request.form.get('password')
    success, msg = confirm_forgot_password(username, code, password)
    if success:
        logger.info(f"Password reset successful for user: {username}")
        flash(msg, 'success')
        return redirect(url_for('login'))
    flash(msg, 'error')
    return render_template('forgot_password.html', step='confirm', username=username)

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'professor':
        classes = current_user.owned_classes
    else:
        classes = current_user.enrolled_classes
    
    notes = Note.query.filter_by(user_id=current_user.id).order_by(Note.uploaded_at.desc()).all()
    return render_template('dashboard.html', user=current_user, notes=notes, classes=classes)

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    if request.method == 'POST':
        new_name = request.form.get('display_name')
        if new_name and new_name != current_user.display_name:
            if current_user.name_changes_left > 0:
                current_user.display_name = new_name
                current_user.name_changes_left -= 1
                db.session.commit()
                flash('Name updated successfully!')
            else:
                flash('No name changes left!')
    return render_template('account.html', user=current_user)

@app.route('/create_class', methods=['POST'])
@login_required
def create_class():
    if current_user.role != 'professor':
        return "Unauthorized", 403
    name = request.form.get('name')
    new_class = Class(name=name, professor_id=current_user.id)
    db.session.add(new_class)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/join_class', methods=['POST'])
@login_required
def join_class():
    code = request.form.get('join_code')
    class_to_join = Class.query.filter_by(join_code=code).first()
    if class_to_join:
        if class_to_join not in current_user.enrolled_classes:
            current_user.enrolled_classes.append(class_to_join)
            db.session.commit()
            flash(f'Joined {class_to_join.name}!')
        else:
            flash('Already joined this class.')
    else:
        flash('Invalid join code.')
    return redirect(url_for('dashboard'))

@app.route('/class/<int:class_id>')
@login_required
def view_class(class_id):
    course_class = Class.query.get_or_404(class_id)
    # Security check
    if current_user.role == 'professor' and course_class.professor_id != current_user.id:
        return "Unauthorized", 403
    if current_user.role == 'student' and course_class not in current_user.enrolled_classes:
        return "Unauthorized", 403
        
    # Sort elements: Module -> Midterm -> Final
    type_priority = {'module': 1, 'midterm': 2, 'final': 3}
    sorted_elements = sorted(course_class.elements, key=lambda x: (type_priority.get(x.type, 4), x.position))
    
    return render_template('classroom.html', course_class=course_class, elements=sorted_elements)

@app.route('/class/<int:class_id>/add_element', methods=['POST'])
@login_required
def add_element(class_id):
    if current_user.role != 'professor': return "Unauthorized", 403
    
    title = request.form.get('title')
    etype = request.form.get('type') # 'module', 'midterm', 'final'
    
    # Calculate position
    course_class = Class.query.get(class_id)
    pos = len(course_class.elements) + 1
    
    files = request.files.getlist('files')
    
    new_element = CourseElement(
        class_id=class_id,
        title=title,
        type=etype,
        position=pos
    )
    db.session.add(new_element)
    db.session.flush() # Get the ID
    
    for file in files:
        if file and file.filename:
            s3_key = upload_file_to_s3(file, f"class_{class_id}/element_{new_element.id}/{file.filename}")
            new_material = Material(
                element_id=new_element.id,
                original_filename=file.filename,
                s3_key=s3_key
            )
            db.session.add(new_material)
            
    db.session.commit()
    logger.info(f"Classroom module created: '{title}' in class {class_id} by {current_user.username}")
    return redirect(url_for('view_class', class_id=class_id))

@app.route('/element/<int:element_id>/delete', methods=['POST'])
@login_required
def delete_element(element_id):
    element = CourseElement.query.get_or_404(element_id)
    # Security check
    if element.parent_class.professor_id != current_user.id:
        return "Unauthorized", 403
    
    class_id = element.class_id
    db.session.delete(element)
    db.session.commit()
    logger.info(f"Classroom module deleted: '{element.title}' (ID: {element_id}) by {current_user.username}")
    flash('Element deleted successfully!', 'success')
    return redirect(url_for('view_class', class_id=class_id))

@app.route('/element/<int:element_id>/edit', methods=['POST'])
@login_required
def edit_element(element_id):
    element = CourseElement.query.get_or_404(element_id)
    # Security check
    if element.parent_class.professor_id != current_user.id:
        return "Unauthorized", 403
    
    element.title = request.form.get('title')
    element.type = request.form.get('type')
    db.session.commit()
    logger.info(f"Classroom module edited: '{element.title}' (ID: {element_id}) by {current_user.username}")
    flash('Element updated successfully!', 'success')
    return redirect(url_for('view_class', class_id=element.class_id))

@app.route('/upload', methods=['POST'])
@login_required
def upload():
    try:
        if 'note' not in request.files:
            return {"error": "No file part"}, 400
        file = request.files['note']
        if file.filename == '':
            return {"error": "No selected file"}, 400
        
        if file:
            s3_key = upload_file_to_s3(file, f"user_{current_user.id}/personal/{file.filename}")
            if s3_key:
                new_note = Note(
                    user_id=current_user.id,
                    original_filename=file.filename,
                    s3_key=s3_key
                )
                db.session.add(new_note)
                db.session.commit()
                logger.info(f"Personal file upload: {file.filename} by user {current_user.username}")
                flash('File uploaded successfully!', 'success')
            else:
                flash('S3 Upload Failed', 'error')
        
        return redirect(url_for('dashboard'))
    except Exception as e:
        logger.error(f"Upload error: {str(e)}")
        flash(f'Upload failed: {str(e)}', 'error')
        return redirect(url_for('dashboard'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5001)