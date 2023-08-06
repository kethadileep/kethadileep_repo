import boto3

s3_client = boto3.client(s3)

bucket = s2_client.create_bucket(
    'package_storage_bucket',
    IAM_role: 'iam000011'

)

for bucket in list_buckets():
    print(bucket)

