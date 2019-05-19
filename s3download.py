import boto3

s3 = boto3.client('s3')

bucket = "cellorgs"

s3.download_file(bucket,'cellorgstest.txt','test-dowload.txt')
