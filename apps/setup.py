""" This utility is developed for the learning purpose
This file contains various functions to demonstrate my learning
towards Setup and provision resources for event driven architectures"""

# Import the required Libraries
import logging
import boto3
import os
import subprocess
from botocore.exceptions import ClientError

# Setup the logger
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

# Initializing the boto3 objects
s3_client = boto3.client('s3')
sns_client = boto3.client('sns', region_name='us-east-1')

# Setting up resource names
sns_topic_name = "aws-demo-sns-type"
data_bucket_for_upload = "user-data-store-2022"


# Create s3 bucket
def create_s3_bucket(client,data_bucket):
    logger.info("Creating s3 bucket")
    bucket_creation_response = s3_client.create_bucket(Bucket=data_bucket)
    logger.info(bucket_creation_response)
    return bucket_creation_response


# Create SNS Topic
def sns_create_topic(client, topic_name):
    try:
        sns_client_response = client.create_topic(Name=topic_name)
        logger.info(sns_client_response)
    except ClientError:
        logger.error("Unable to create topic. Please look into the issue")
    else:
        logger.info(sns_client_response)
        return sns_client_response


# Main Function
if __name__ == '__main__':
    logger.info("AWS Resources Setup Process - Begins")
    s3_bucket_creation_response = create_s3_bucket(s3_client, data_bucket_for_upload)
    sns_create_topic_response = sns_create_topic(sns_client,sns_topic_name)
    logger.info("AWS Resources Setup Process - Ends")
