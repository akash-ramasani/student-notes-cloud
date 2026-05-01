import boto3
from flask import current_app

def get_s3_client():
    return boto3.client(
        's3',
        aws_access_key_id=current_app.config.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=current_app.config.get('AWS_SECRET_ACCESS_KEY'),
        region_name=current_app.config['AWS_REGION']
    )

def upload_file_to_s3(file, filename):
    s3 = get_s3_client()
    bucket = current_app.config['S3_BUCKET_NAME']
    try:
        s3.upload_fileobj(
            file,
            bucket,
            filename,
            ExtraArgs={"ContentType": file.content_type}
        )
        return filename # Return the key, not the URL
    except Exception as e:
        print(f"Error uploading to S3: {e}")
        return None

def generate_presigned_url(s3_key):
    s3 = get_s3_client()
    try:
        url = s3.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': current_app.config['S3_BUCKET_NAME'],
                'Key': s3_key
            },
            ExpiresIn=3600 # 1 hour
        )
        return url
    except Exception as e:
        print(f"Error generating presigned URL: {e}")
        return None
