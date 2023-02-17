import boto3
from configure import *
bucket_name = "bucketuse2023"
class GetFile(object):
    
    def __init__(self) -> None:
        pass
    
    def get_file(self):
        try:
            s3 = boto3.resource('s3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY
            )
            s3.Bucket(bucket_name).download_file('input/s2.csv', 'input/s2.csv')
        except Exception as err:
            print("An exception occurred: upload: ", err)