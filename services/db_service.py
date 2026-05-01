from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import uuid

db = SQLAlchemy()

# Many-to-Many relationship for students and classes
class_enrollment = db.Table('class_enrollment',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('class_id', db.Integer, db.ForeignKey('classes.id'), primary_key=True)
)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False) # 'student' or 'professor'
    display_name = db.Column(db.String(100))
    name_changes_left = db.Column(db.Integer, default=3)
    
    # Relationships
    owned_classes = db.relationship('Class', backref='professor', lazy=True)
    enrolled_classes = db.relationship('Class', secondary=class_enrollment, backref=db.backref('students', lazy='dynamic'))
    personal_notes = db.relationship('Note', backref='owner', lazy=True)

class Class(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    join_code = db.Column(db.String(10), unique=True, nullable=False, default=lambda: str(uuid.uuid4())[:8].upper())
    professor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    elements = db.relationship('CourseElement', backref='parent_class', lazy=True, order_by="CourseElement.position")

class CourseElement(db.Model):
    __tablename__ = 'course_elements'
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(20), nullable=False) # 'module', 'midterm', 'final'
    position = db.Column(db.Integer, nullable=False)
    
    # Relationships
    materials = db.relationship('Material', backref='element', lazy=True, cascade="all, delete-orphan")

class Material(db.Model):
    __tablename__ = 'materials'
    id = db.Column(db.Integer, primary_key=True)
    element_id = db.Column(db.Integer, db.ForeignKey('course_elements.id'), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    s3_key = db.Column(db.String(500), nullable=False)
    uploaded_at = db.Column(db.DateTime, server_default=db.func.now())

    @property
    def s3_url(self):
        from services.s3_service import generate_presigned_url
        return generate_presigned_url(self.s3_key)

class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    s3_key = db.Column(db.String(500), nullable=False)
    file_size = db.Column(db.Integer)
    content_type = db.Column(db.String(100))
    uploaded_at = db.Column(db.DateTime, server_default=db.func.now())

    @property
    def s3_url(self):
        from services.s3_service import generate_presigned_url
        return generate_presigned_url(self.s3_key)
