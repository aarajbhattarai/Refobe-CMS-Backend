import boto3
s3 = boto3.client('s3', region_name=AWS_LOCATION)
response = s3.head_bucket(Bucket=AWS_STORAGE_BUCKET_NAME)
print(response)