import boto3
from configure import *
class UploadFile(object):
    
    def __init__(self) -> None:
        pass
    
    def upload_file(self):
    
        bucket_name = "bucketuse2023"
        file_name = "input/business-financial-data-september-2022-quarter.csv"
        object_name = 'input/business-financial-data-september-2022-quarter.csv'
        
        try:
            s3 = boto3.resource('s3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY
            )
            s3.Bucket(bucket_name).upload_file(object_name, file_name)
        except Exception as err:
            print("An exception occurred: upload: ", err)

