# Baton

Prerequisites to run the python script
1. install aws cli
2. configure aws with access key and secret key

python script to be run by

>>python list_ec2.py
>>python list_ec2.py t2.micro

Prerequisities to run ansible playbook

set aws access and secret key as environment variables by executing

export AWS_ACCESS_KEY="XXXXXXXXXXXXXXXX"
export AWS_SECRET_ACCESS_KEY="XXXXXXXXXXXXXXXXXXXXX"

Also change the keypair and security group in the ansible playbook to what you have in your aws account.
run the ansible playbook by

>>ansible-playbook ec2creation.yaml
