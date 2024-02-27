import boto3

# Function defined
def create_s3_bucket(bucket_name):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Create the bucket
    s3.create_bucket(Bucket=bucket_name)

    print(f'Successfully created bucket: {bucket_name}')

# This code will only run if the script is executed directly, not when it's imported as a module
if __name__ == "__main__":
    bucket_name = 'your-unique-bucket-name'  # Replace this with your desired bucket name
    create_s3_bucket(bucket_name)

# Additionally, make sure your AWS credentials are correctly set up. You can do this by either configuring the AWS CLI (aws configure) or setting environment variables (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION). This will allow Boto3 to authenticate with AWS and create the bucket in your account.

