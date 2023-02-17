import boto3


AWS_ACCESS_KEY_ID = 'AKIA4BSTJ23SAS2G2JPR'
AWS_SECRET_ACCESS_KEY = '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'
bucket_name = "bucketuse2023"

try:
    s3 = boto3.resource('s3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    s3.Bucket(bucket_name).download_file('input/s2.csv', 'tmp/s2.csv')
except Exception as err:
    print("An exception occurred: upload: ", err)