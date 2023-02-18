import boto3
from configure import *

class DeleteFile(object):
    
    def __init__(self) -> None:
        pass
    
    def delete_file(self):
        
        file_name = 'input/s2.csv'
        bucket_name = "bucketuse2023"

        try:
            s3 = boto3.resource('s3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY
            )
            s3.Object(bucket_name, file_name).delete()
            
        except Exception as err:
            print("An exception occurred: upload: ", err)