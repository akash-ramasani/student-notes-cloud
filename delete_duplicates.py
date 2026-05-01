from app import app
from services.db_service import db, CourseElement

with app.app_context():
    # Find all elements with the title "Week 4: What is IAM?"
    elements = CourseElement.query.filter_by(title="Week 4: What is IAM?").all()
    
    if len(elements) > 1:
        # Keep the first one, delete the rest
        to_delete = elements[1:]
        print(f"Found {len(elements)} duplicates. Deleting {len(to_delete)}...")
        for el in to_delete:
            print(f"Deleting element ID: {el.id}")
            db.session.delete(el)
        db.session.commit()
        print("Success.")
    else:
        print("No duplicates found.")
