import boto3

sqs = boto3.resource('sqs', region_name="ca-central-1")

for queue in sqs.queues.all():
    print(queue.url)
queue = sqs.get_queue_by_name(QueueName='s3-upload')

print(queue.url)
print(queue.attributes.get('DelaySeconds'))

response = client.receive_message(
    QueueUrl=queue.url,
    AttributeNames=[
        'All'|'Policy'|'VisibilityTimeout'|'MaximumMessageSize'|'MessageRetentionPeriod'|'ApproximateNumberOfMessages'|'ApproximateNumberOfMessagesNotVisible'|'CreatedTimestamp'|'LastModifiedTimestamp'|'QueueArn'|'ApproximateNumberOfMessagesDelayed'|'DelaySeconds'|'ReceiveMessageWaitTimeSeconds'|'RedrivePolicy'|'FifoQueue'|'ContentBasedDeduplication'|'KmsMasterKeyId'|'KmsDataKeyReusePeriodSeconds',
    ],
    MessageAttributeNames=[
        'string',
    ],
    MaxNumberOfMessages=123,
    VisibilityTimeout=123,
    WaitTimeSeconds=123,
    ReceiveRequestAttemptId='string'
)

print(response)