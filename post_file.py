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

bucket = conn.create_bucket(bucket_name, location=boto.s3.connection.Location.DEFAULT)
testfile = "input/annual-2022.csv"

print("Uploading=",testfile," to Amazon S3 bucket: ", bucket_name)

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()
    

k = Key(bucket)
k.key = "dump/annual-2022.csv"
k.set_contents_from_filename(testfile, cb=percent_cb, num_cb=10)