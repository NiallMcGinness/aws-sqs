import boto3
from pathlib import Path

s3 = boto3.resource('s3')
s3client = boto3.client('s3')
my_bucket = s3.Bucket('cellmask')
s3_folder_name = "models/models/test-model224rs30-v0-0"
dest_folder = Path("test")
"""
for file in my_bucket.objects.all():
    print file.key
"""

for obj in my_bucket.objects.filter(Prefix=s3_folder_name):
    #print(obj)
    print('{0}:{1}'.format(my_bucket.name, obj.key))
    pl = Path(obj.key)
    #print(pl.name)
    dest_filename = str( dest_folder.joinpath(pl.name) )
    print(dest_filename)
    s3client.download_file(my_bucket.name, obj.key, dest_filename)


