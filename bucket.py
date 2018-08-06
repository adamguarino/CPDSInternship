import boto3
import botocore
s3 = boto3.resource('s3')
bucketname = 'bucketname'
"""s3.create_bucket(Bucket=bucketname, CreateBucketConfiguration={
    'LocationConstraint': 'us-east-2'})"""
filename = 'filename'
#s3.upload_file(filename,bucketname,filename)

key = 'key'
try:
    s3.Bucket(bucketname).download_file(key,filename)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code']=='404':
        print('The object does not exist.')
    else:
        raise 
