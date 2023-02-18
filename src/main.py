from upload_file import *
from get_file import *
from read_file import *
from delete_file import *
from read_names_files_in_bucket import *

def main():
    #read files in bucket aws s3
    print("read all files in bucket s3")
    read_files_bucket = ReadFilesInBucket()
    read_files_bucket.list_all_files_in_bucket()
    
    #read files in bucket aws s3
    print("read files in bucket s3 type = csv")
    read_files_bucket = ReadFilesInBucket()
    read_files_bucket.list_types_files_in_bucket("csv")
    
     #read files in bucket aws s3
    print("read files in bucket s3 folder = dump")
    read_files_bucket = ReadFilesInBucket()
    read_files_bucket.list_filtre_files_in_bucket("dump")
    
    #upload 
    print("Upload file")
    upload = UploadFile()
    upload.upload_file()

    #get file
    print("Get file")
    download = GetFile()
    download.get_file()
    
    #read
    print("Read file")
    read = ReadFile()
    read.read_file()
    
    #delete
    print("Delet file")
    delete = DeleteFile()
    delete.delete_file()
    
    
    
if __name__ == "__main__":
    main()