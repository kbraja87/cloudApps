""" This utility is developed for the learning purpose
This file contains various functions to demonstrate my learning
towards event driven architecture"""

# Import the required modules
import logging
import boto3
import os
import subprocess
from botocore.exceptions import ClientError

# Setup the logger environment
logger = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

# Setup the AWS objects
s3_client = boto3.client('s3')
sns_client = boto3.client('sns', region_name='us-east-1')

# Static Values for the process
data_bucket_for_upload = "user-data-store-2022"
source_files_path = "C:\\Users\\karth\\OneDrive\\Desktop\\files_to_upload"


# Get the s3 buckets
def get_s3_buckets(client):
    available_bucket_names = []
    bucket_list = client.list_buckets()
    for bucket_names in bucket_list['Buckets']:
        available_bucket_names.append(bucket_names['Name'])
    return available_bucket_names


# Uploads the files to s3 from the specified local path:
def s3_upload_files(client, bucket, files_path):
    subprocess.call('dir', shell=True)
    files_list = os.listdir(files_path)
    print(files_list)
    for file in files_list:
        file_to_upload = os.path.join(files_path,file)
        try:
            response = client.upload_file(file_to_upload, bucket, file)
        except ClientError as e:
            logging.error(e)
            return False
    return True


# Main function that calls the required functionalities
if __name__ == '__main__':
    s3_bucket_names = get_s3_buckets(s3_client)
    s3_upload_files_response = s3_upload_files(s3_client, data_bucket_for_upload, source_files_path)
    if s3_upload_files_response:
        print("S3 Upload is successful")



















