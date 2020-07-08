import boto3
import sys

ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    if len(sys.argv)>1:
        if instance.instance_type == sys.argv[1]:
            print instance.id , instance.instance_type
    else:
        print instance.id , instance.instance_type
