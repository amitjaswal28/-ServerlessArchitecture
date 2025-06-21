# === Assignment 6: Monitor and Alert High AWS Billing ===
# File: assignment-6-billing-alert/lambda_function.py
import boto3
import datetime

def lambda_handler(event, context):
    cloudwatch = boto3.client('cloudwatch')
    sns = boto3.client('sns')

    threshold = 50.0  # USD
    topic_arn = 'arn:aws:sns:region:account-id:YourTopic'  # Replace with your SNS topic ARN

    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/Billing',
        MetricName='EstimatedCharges',
        Dimensions=[{'Name': 'Currency', 'Value': 'USD'}],
        StartTime=datetime.datetime.utcnow() - datetime.timedelta(days=1),
        EndTime=datetime.datetime.utcnow(),
        Period=86400,
        Statistics=['Maximum']
    )

    datapoints = response.get('Datapoints', [])
    if datapoints and datapoints[0]['Maximum'] > threshold:
        message = f"Alert: AWS Billing has exceeded ${threshold}. Current: ${datapoints[0]['Maximum']:.2f}"
        sns.publish(TopicArn=topic_arn, Message=message)
        print("Billing alert sent")
    else:
        print("Billing is under control.")