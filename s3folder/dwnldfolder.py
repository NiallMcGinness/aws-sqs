import boto3

s3 = boto3.resource('s3')

bucket_name = "cellmask"
key = "models/models/"

s3.Bucket(bucket_name).download_file(key, 'models')