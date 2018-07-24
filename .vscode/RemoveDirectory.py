import os
def DeleteDirectory():
        dirPath=str(input("Enter the Directory path to remove"))
        dirPath.replace("/","//")
        if(os.path.isdir(dirPath)):
            print("File Exists")
            os.remove(dirPath)
        else:
            print("File does not exists")
            DeleteDirectory()
                    
DeleteDirectory()