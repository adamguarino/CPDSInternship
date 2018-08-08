#https://boto3.readthedocs.io/en/latest/guide/s3-example-creating-buckets.html

import boto3
import botocore
s3 = boto3.resource('s3') 
bucketname = 'bucketname' 
#This command creates a bucket in the location you specify. Note: certain locations don't work with making buckets for some reason
"""s3.create_bucket(Bucket=bucketname, CreateBucketConfiguration={
    'LocationConstraint': 'us-east-2'})"""
filename = 'filename'
#s3.upload_file(filename,bucketname,filename) #uploading files just requires a bucket and a file

key = 'key' #a file's key can be obtained from the AWS S3 Client by clicking the area around it
try:
    s3.Bucket(bucketname).download_file(key,filename)
except botocore.exceptions.ClientError as e:    #exception handling if the file doesn't exist
    if e.response['Error']['Code']=='404':
        print('The object does not exist.')
    else:
        raise 
