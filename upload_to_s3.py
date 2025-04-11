import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = 'aistorygenerator'
FILE_NAME = 'reddit_stories.txt'
S3_KEY = 'reddit_stories.txt'  # No folder — just the file name

s3 = boto3.client('s3')

try:
    s3.upload_file(FILE_NAME, BUCKET_NAME, S3_KEY)
    print(f"✅ Uploaded {FILE_NAME} to s3://{BUCKET_NAME}/{S3_KEY}")
except ClientError as e:
    print("❌ Upload failed:", e.response['Error']['Message'])
