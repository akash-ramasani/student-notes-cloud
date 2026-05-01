from app import app
from services.db_service import db, CourseElement

with app.app_context():
    # Find the element named "Module 1"
    element = CourseElement.query.filter_by(title="Module 1").first()
    if element:
        print(f"Deleting element: {element.title} (ID: {element.id})")
        db.session.delete(element)
        db.session.commit()
        print("Success.")
    else:
        print("Element 'Module 1' not found.")
