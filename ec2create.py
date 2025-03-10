import boto3

# Hardcoded AWS Credentials 
AWS_ACCESS_KEY = "AKIATESTACCESSKEY1234"
AWS_SECRET_KEY = "testSecretKey1234567890abcdefg"
REGION = "us-east-1"

# Hardcoded EC2 Configurtion
AMI_ID = "ami-0c55b159cbfafe1f0"  # Ubuntu 18.04 AMI
INSTANCE_TYPE = "t2.micro"
KEY_NAME = "test-key"  # Ensure this key exists in AWS
SECURITY_GROUP = "default"
KEY = /root/awspca1.pem

# Hardcoded Environment Variables
ENV_VARS = {
    "OLD_PYTHON_VERSION": "3.6",
    "APP_ENV": "testing",
    "DEBUG_MODE": "true"
}

# User Data Script (Executed on Startup)
USER_DATA = """#!/bin/bash
sudo apt update -y
sudo apt install -y python3.6 python3-pip
echo 'export OLD_PYTHON_VERSION=3.6' >> /etc/profile
echo 'export APP_ENV=testing' >> /etc/profile
echo 'export DEBUG_MODE=true' >> /etc/profile
source /etc/profile
"""

# Initialize EC2 Client
ec2 = boto3.client(
    "ec2",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION
)

# Launch EC2 Instance
response = ec2.run_instances(
    ImageId=AMI_ID,
    InstanceType=INSTANCE_TYPE,
    KeyName=KEY_NAME,
    SecurityGroups=[SECURITY_GROUP],
    MinCount=1,
    MaxCount=1,
    UserData=USER_DATA
)

# Retrieve Instance ID
instance_id = response["Instances"][0]["InstanceId"]
print(f"EC2 Instance Created: {instance_id}")
