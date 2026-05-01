from app import app
from services.db_service import db

with app.app_context():
    # Check if table exists
    inspector = db.inspect(db.engine)
    if 'materials' not in inspector.get_table_names():
        print("Creating materials table...")
        # We can use db.create_all() which only creates missing tables
        db.create_all()
        print("Done.")
    else:
        print("Materials table already exists.")
    
    # Optional: Try to migrate existing s3_keys if needed (but since we are modernising, maybe not necessary)
    # Actually, let's keep it simple.
