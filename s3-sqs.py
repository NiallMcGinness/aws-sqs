import boto3

sqs = boto3.resource('sqs', region_name="ca-central-1")

for queue in sqs.queues.all():
    print(queue.url)
queue = sqs.get_queue_by_name(QueueName='s3-upload')

print(queue.url)
print(queue.attributes.get('DelaySeconds'))

