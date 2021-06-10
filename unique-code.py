import re
import boto3
from botocore.client import Config

def getNumbers(str):
	a = re.findall(r'[0-9]+', str)
	return a


str = input("Enter the Selfie name:")
a = getNumbers(str)
print("Unique Code is:")
print(*a)

def save(*a):
	r=''.join(*a)
	print(r+".jpg")

ACCESS_KEY_ID = '**********************'
ACCESS_SECRET_KEY = '***********************'
BUCKET_NAME = 'kwikpik-test'
FILE_NAME = save(*a)

data = open(FILE_NAME, 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)

s3.Bucket(BUCKET_NAME).put_object(Key=FILE_NAME, Body=data, ACL='public-read')

print ("Done uploading")

