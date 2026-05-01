from app import app
from services.db_service import db

with app.app_context():
    print("Dropping and recreating all tables for the new schema...")
    db.drop_all()
    db.create_all()
    print("Database updated successfully!")
