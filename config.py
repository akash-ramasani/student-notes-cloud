import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or 'dev-key-123'
    
    # RDS MySQL Configuration
    RDS_USERNAME = os.environ.get('RDS_USERNAME')
    RDS_PASSWORD = os.environ.get('RDS_PASSWORD')
    RDS_HOST = os.environ.get('RDS_HOST')
    RDS_PORT = os.environ.get('RDS_PORT', '3306')
    RDS_DB_NAME = os.environ.get('RDS_DB_NAME', 'studentnotes')
    
    # Construct MySQL URI
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{RDS_USERNAME}:{RDS_PASSWORD}@{RDS_HOST}:{RDS_PORT}/{RDS_DB_NAME}" if RDS_HOST else "sqlite:///temp.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # AWS General
    # AWS Credentials
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_REGION = os.environ.get('AWS_REGION', 'us-east-1')
    
    # S3 Configuration
    S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
    
    # Cognito Configuration
    COGNITO_USER_POOL_ID = os.environ.get('COGNITO_USER_POOL_ID')
    COGNITO_APP_CLIENT_ID = os.environ.get('COGNITO_APP_CLIENT_ID')
