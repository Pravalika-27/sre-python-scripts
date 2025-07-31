import boto3

s3 = boto3.client('s3')
bucket_name = "your-unique-bucket-name"

response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
)
print("Bucket created:", response['Location'])