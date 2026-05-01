from app import app, db
from services.db_service import User
from services.auth_service import get_cognito_client
from flask import current_app

with app.app_context():
    username = 'test_professor'
    user = User.query.filter_by(username=username).first()
    
    # 1. Delete from Cognito
    try:
        client = get_cognito_client()
        client.admin_delete_user(
            UserPoolId=app.config['COGNITO_USER_POOL_ID'],
            Username=username
        )
        print(f"Deleted {username} from Cognito.")
    except Exception as e:
        print(f"Cognito deletion error (user might not exist): {e}")

    # 2. Delete from RDS
    if user:
        db.session.delete(user)
        db.session.commit()
        print(f"Deleted {username} from RDS Database.")
    else:
        print(f"User {username} not found in RDS.")

