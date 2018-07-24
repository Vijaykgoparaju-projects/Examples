import os
def DeleteFileAndWrite():
        filepath=str(input("Enter the file path"))
        filepath.replace("/","//")
        if(os.path.isfile(filepath)):
            print("File Exists")
            os.remove(filepath)
        else:
            print("File does not exists")
            DeleteFileAndWrite()
                    
DeleteFileAndWrite()