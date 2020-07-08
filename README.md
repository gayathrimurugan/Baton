# Baton

python script to be run by

>>python list_ec2.py
>>python list_ec2.py t2.micro

Prerequisities to run ansible playbook

set aws access and secret key as environment variables by executing

export AWS_ACCESS_KEY="XXXXXXXXXXXXXXXX"
export AWS_SECRET_ACCESS_KEY="XXXXXXXXXXXXXXXXXXXXX"

run the ansible playbook by

ansible-playbook ec2creation.yaml
