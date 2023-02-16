import boto
import boto.s3
import sys
from boto.s3.key import Key

#user bucketuser
AWS_ACCESS_KEY_ID = 'AKIA4BSTJ23SAS2G2JPR'
AWS_SECRET_ACCESS_KEY = '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'

#bucket_name = AWS_ACCESS_KEY_ID.lower() + '-dump'
bucket_name = "bucketuse2023"
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)

bucket = conn.get_bucket(bucket_name,)
print(bucket)