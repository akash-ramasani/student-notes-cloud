from app import app
from services.db_service import db

with app.app_context():
    print("Creating tables in RDS...")
    db.create_all()
    print("Tables created successfully!")
