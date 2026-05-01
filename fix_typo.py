from app import app
from services.db_service import db, CourseElement

with app.app_context():
    # Find the element with the typo
    element = CourseElement.query.filter_by(title="Week 3: Cloud Platoforms").first()
    if element:
        print(f"Fixing typo in: {element.title}")
        element.title = "Week 3: Cloud Platforms"
        db.session.commit()
        print("Success.")
    else:
        # Try a broader search just in case
        element = CourseElement.query.filter(CourseElement.title.like("%Platoforms%")).first()
        if element:
            print(f"Fixing typo in found element: {element.title}")
            element.title = element.title.replace("Platoforms", "Platforms")
            db.session.commit()
            print("Success.")
        else:
            print("No typo found.")
