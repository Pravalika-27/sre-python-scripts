import boto3

client = boto3.client('cloudwatch')

response = client.put_metric_alarm(
    AlarmName='HighCPUUsage',
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Statistic='Average',
    Period=300,
    EvaluationPeriods=1,
    Threshold=80.0,
    ComparisonOperator='GreaterThanThreshold',
    Dimensions=[
        {'Name': 'InstanceId', 'Value': 'i-xxxxxxxxxxxxxxxxx'},
    ],
    AlarmActions=['arn:aws:sns:region:account-id:my-sns-topic'],
    Unit='Percent'
)
print("Alarm created")