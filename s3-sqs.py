import boto3

client = boto3.client('sqs', region_name="ca-central-1")

queue = sqs.get_queue_by_name(QueueName='s3-upload')

print(queue.url)
print(queue.attributes.get('DelaySeconds'))

