from app import app
from services.db_service import db, User

with app.app_context():
    # Sync the confirmed Cognito user to RDS
    if not User.query.filter_by(username='akash_ramasani').first():
        print("Adding akash_ramasani to RDS...")
        user = User(username='akash_ramasani', email='akash@example.com') # Using a placeholder email
        db.session.add(user)
        db.session.commit()
        print("User added successfully!")
    else:
        print("User already exists in RDS.")
