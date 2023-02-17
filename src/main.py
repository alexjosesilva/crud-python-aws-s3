from upload_file import *
from get_file import *

def main():
    print("Get file")
    download = GetFile()
    download.get_file()
    
    print("Download file")
    upload = UploadFile()
    upload.upload_file()
    
    #Read files in bucket
    #delete file or files in bucket
    

if __name__ == "__main__":
    main()