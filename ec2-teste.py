import boto3

#Access Key ID:
#--> AKIAIIMCT6UW6ZABVQBA
#Secret Access Key:
#--> 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


ec2 = boto3.client('ec2')
if sys.argv[1] == 'ON':
    response = ec2.monitor_instances(InstanceIds=['INSTANCE_ID'])
else:
    response = ec2.unmonitor_instances(InstanceIds=['INSTANCE_ID'])
print(response)