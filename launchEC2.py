#/usr/bin/python

import boto.ec2
import time
conn = boto.ec2.connect_to_region('us-west-2',aws_access_key_id='XXXXXXXXXXXXXXXXXXXX',aws_secret_access_key='XXXXXXXXXXXXXXXXXXXX')
reservation = conn.run_instances(
    'ami-d8a563b8',
    key_name='awsassignment',
    instance_type='t2.micro',
    security_groups=['awsassignment']
)
instance = reservation.instances[0]
while instance.update() != "running":
    time.sleep(5)
print instance.ip_address


