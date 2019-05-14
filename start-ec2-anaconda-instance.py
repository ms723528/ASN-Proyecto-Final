import json
import boto3
import logging

#setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#define the connection
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    # TODO implement
    
    filters = [{'Name': 'tag:Name','Values': ['Anaconda']}]

    region = 'us-east-1'

    #filter the instances
    instances = ec2.instances.filter(Filters=filters)

    #locate all running instances
    StoppedInstances = [instance.id for instance in instances]
    
    #print the instances for logging purposes
    print('Stopped Instances ',StoppedInstances )
    
    #make sure there are actually instances to shut down. 
    if len(StoppedInstances) > 0:
        #perform the start-up
        startingUp = ec2.instances.filter(InstanceIds=StoppedInstances).start()
        print('Starting up ',startingUp)
    else:
        print("Nothing to see here")

