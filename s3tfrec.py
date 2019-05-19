import boto3

import time

s3client = boto3.client('s3')

bucket_name = "cellorgs"

filename = 'train224.tfrecords'

output_filename = 'train224.tfrecords'
#s3.download_file(bucket,'cellorgstest.txt','test-dowload.txt')


def download(s3client, bucket_name, filename , output_filename):
    return s3client.download_file(bucket_name,filename,output_filename)



start_time = time.time()

print("starting download")

download(s3client, bucket_name, filename , output_filename)

end_time = time.time()

print("download complete , time taken in seconds {} ".format(end_time - start_time))
