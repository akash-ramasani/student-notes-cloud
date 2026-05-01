import boto3
from flask import current_app
from .db_service import db, User

def get_cognito_client():
    return boto3.client('cognito-idp', region_name=current_app.config['AWS_REGION'])

def register_user(username, email, password, role):
    # 0. Check if user already exists in RDS
    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        if existing_user.username == username:
            return None, "This username is already taken. Please choose another."
        else:
            return None, "This email is already registered. Please sign in or use another email."

    client = get_cognito_client()
    try:
        # 1. Register in Cognito
        client.sign_up(
            ClientId=current_app.config['COGNITO_APP_CLIENT_ID'],
            Username=username,
            Password=password,
            UserAttributes=[
                {'Name': 'email', 'Value': email}
            ]
        )
        
        # 2. Create placeholder in RDS
        new_user = User(
            username=username, 
            email=email, 
            role=role, 
            display_name=username,
            name_changes_left=3
        )
        db.session.add(new_user)
        db.session.commit()
        
        return new_user, "Success! Please check your email for the verification code."
    except Exception as e:
        # Provide a cleaner error message if possible
        error_msg = str(e)
        if "UsernameExistsException" in error_msg:
            return None, "This username already exists in our system."
        return None, f"Registration failed: {error_msg}"

def authenticate_user(username, password):
    client = get_cognito_client()
    try:
        # 1. Authenticate with Cognito
        client.initiate_auth(
            ClientId=current_app.config['COGNITO_APP_CLIENT_ID'],
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password
            }
        )
        
        # 2. Get user from RDS
        user = User.query.filter_by(username=username).first()
        return user
    except Exception as e:
        print(f"Auth error: {e}")
        return None

def verify_user(username, otp):
    client = get_cognito_client()
    try:
        client.confirm_sign_up(
            ClientId=current_app.config['COGNITO_APP_CLIENT_ID'],
            Username=username,
            ConfirmationCode=otp
        )
        return True, "Verification successful! You can now log in."
    except Exception as e:
        return False, str(e)

def initiate_forgot_password(username):
    client = get_cognito_client()
    try:
        client.forgot_password(
            ClientId=current_app.config['COGNITO_APP_CLIENT_ID'],
            Username=username
        )
        return True, "Success! A reset code has been sent to your email."
    except Exception as e:
        return False, str(e)

def confirm_forgot_password(username, code, new_password):
    client = get_cognito_client()
    try:
        client.confirm_forgot_password(
            ClientId=current_app.config['COGNITO_APP_CLIENT_ID'],
            Username=username,
            ConfirmationCode=code,
            Password=new_password
        )
        return True, "Password reset successful! You can now log in with your new password."
    except Exception as e:
        return False, str(e)
