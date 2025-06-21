# === Assignment 2: Automated S3 Bucket Cleanup ===
# File: assignment-2-s3-cleanup/lambda_function.py
import boto3
import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'your-bucket-name'  # Replace with your bucket

    response = s3.list_objects_v2(Bucket=bucket_name)
    deleted_files = []

    if 'Contents' in response:
        for obj in response['Contents']:
            if (datetime.datetime.now(datetime.timezone.utc) - obj['LastModified']).days > 30:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
                deleted_files.append(obj['Key'])

    print(f"Deleted files older than 30 days: {deleted_files}")