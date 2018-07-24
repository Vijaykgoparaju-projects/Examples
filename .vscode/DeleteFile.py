import os
def DeleteFileAndWrite():
    
    try:
        filepath=str(input("Enter the file path"))
        filepath.replace("/","//")
        os.remove(filepath)
        print("File Deleted successfully")
    except FileNotFoundError:
        print("this file does not exisits")
        DeleteFileAndWrite()

    
DeleteFileAndWrite()