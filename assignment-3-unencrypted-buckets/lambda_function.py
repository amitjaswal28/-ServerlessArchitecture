# === Assignment 3: Monitor Unencrypted S3 Buckets ===
# File: assignment-3-unencrypted-buckets/lambda_function.py
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']
    unencrypted = []

    for bucket in buckets:
        try:
            s3.get_bucket_encryption(Bucket=bucket['Name'])
        except Exception:
            unencrypted.append(bucket['Name'])

    print(f"Buckets without server-side encryption: {unencrypted}")