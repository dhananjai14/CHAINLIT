# import boto3
# import json

# def lambda_handler(event, context):
#     # Get the EC2 instance ID from the event
#     instance_id = event['detail']['instance-id']
#     instance_name = event['detail']['instance-name']

#     # Get the list of tags for the instance
#     ec2 = boto3.client('ec2')
#     tags = ec2.describe_tags(Filters=[{'Name': 'resource-id', 'Values': [instance_id]}])['Tags']

#     # Check if the instance has the "patch_group" tag
#     patch_group_tag = next((tag for tag in tags if tag['Key'] == 'patch_group'), None)

#     # If the instance does not have the "patch_group" tag, send an email notification
#     if not patch_group_tag:
#         sns = boto3.client('sns')
#         sns.publish(
#             TopicArn='arn:aws:sns:us-east-1:123456789012:my-topic',
#             Message='EC2 instance {} ({}) does not have the "patch_group" tag.'.format(instance_name, instance_id)
#         )

#     return {
#         'statusCode': 200
#     }

import boto3

sns = boto3.client('sns')
ec2 = boto3.client('ec2')

# # Replace with your SNS topic ARN
SNS_TOPIC_ARN = 'arn:aws:lambda:us-east-1:730335610167:function:check_patch_group'

def lambda_handler(event, context):
    for record in event['Records']:
        # Check if the event is for an EC2 instance state change
        if record['eventName'] == 'RunInstances':
            instance_id = record['responseElements']['instancesSet']['items'][0]['instanceId']
            instance_details = ec2.describe_instances(InstanceIds=[instance_id])
            tags = instance_details['Reservations'][0]['Instances'][0].get('Tags', [])

            # Check for the presence of 'Patch Group' tag
            patch_group_tag = next((tag for tag in tags if tag['Key'] == 'patch_group'), None)
            if not patch_group_tag:
                # Send notification if 'Patch Group' tag is missing
                sns.publish(
                    TopicArn=SNS_TOPIC_ARN,
                    Subject='EC2 Instance Without Patch Group',
                    Message=f'Instance {instance_id} has been launched without a Patch Group tag.'
                )

    return {
        'statusCode': 200,
        'body': 'Success'
    }



'''
can be added to filters: 
instance-state-name - The state of the instance ( pending | running | shutting-down | terminated | stopping | stopped).
 parameter: 'State': {
                        'Code': 123,
                        'Name': 'pending'|'running'|'shutting-down'|'terminated'|'stopping'|'stopped'
                    },'''

my_dict = {
    'key1': 'part1',
    'key2': 'part2',
    'key3': 'part1',
    'key4': 'part3',
    'key5': 'part1'}

def dict_keys(dictionary):
    # Using next() to find the first key with value 'part1'
    lst = []
    for key, value in dictionary.items():
        if value == "part1":
            lst.append(key)
        
    # first_key = next((key for key, value in dictionary.items() if value == 'part1'), None)
    return lst

print(dict_keys(my_dict))

