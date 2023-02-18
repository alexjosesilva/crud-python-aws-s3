import boto3
import re 
from configure import *

class ReadFilesInBucket(object):
    
    def __init__(self) -> None:
        pass
    
    def list_all_files_in_bucket(self):
        bucket_name = "bucketuse2023"
        try:
            s3 = boto3.resource('s3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY
            )
            
            my_bucket = s3.Bucket(bucket_name)
            for my_bucket_obj in my_bucket.objects.all():
                print(my_bucket_obj.key)
                
        except Exception as err:
            print("An exception occurred: read name files in bucket in aws s3: ", err)
        

    def list_filtre_files_in_bucket(self, filtre):
        bucket_name = "bucketuse2023"
        try:
            s3 = boto3.resource('s3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY
            )
            
            my_bucket = s3.Bucket(bucket_name)
            for my_bucket_obj in my_bucket.objects.filter(Prefix=filtre):
                print(my_bucket_obj.key)
                
        except Exception as err:
            print("An exception occurred: read name files in bucket in aws s3: ", err)  
    
        
    def list_types_files_in_bucket(self, type_files):
        bucket_name = "bucketuse2023"
        try:
            s3 = boto3.resource('s3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY
            )
            
            my_bucket = s3.Bucket(bucket_name)
            substring =  "\d"
            for my_bucket_obj in my_bucket.objects.all():
                if re.search(substring,  my_bucket_obj.key):  
                    print(my_bucket_obj.key)
                
        except Exception as err:
            print("An exception occurred: read name files in bucket in aws s3: ", err) 