import boto3

# Let's use Amazon S3
#s3 = boto3.resource('s3')
s3 = boto3.client("s3")
bucket_name = "cellmask"
all_objects = s3.list_objects(Bucket = bucket_name, Prefix="models/")['Contents']['Key'] 
#list_tables = s3.get_list_of_tables(Bucket = bucket_name)
print(all_objects)

