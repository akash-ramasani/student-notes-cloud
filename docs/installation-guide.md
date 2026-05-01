# Installation Guide

## Prerequisites
- Python 3.8+
- AWS Account (S3 Bucket)
- SQLite (Local development)

## Setup Steps

### 1. Clone & Environment
```bash
cp .env.template .env
# Fill in your AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_S3_BUCKET
```

### 2. Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
```

### 3. Database Initialization
The application will automatically create the `student_notes.db` SQLite file on the first run.

### 4. Running the App
```bash
python app.py
```
Visit `http://localhost:5000` in your browser.

## S3 Permissions
Ensure your IAM user has `s3:PutObject` and `s3:GetObject` permissions for the specified bucket.
