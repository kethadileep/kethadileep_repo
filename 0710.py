import boto3

ec2 = boto3.client('ec2')

ec2.create_ec2instance(IAM, Min =1, Max=10
                region = 'naeast'
                accesskey = ''
                securekey = '')

for ec2 in list_ec2_instance():
    print(ec2)
            