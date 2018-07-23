class FileHandlingExp:

    def collectFilePath():
        
        try:
            myFilePath=input("Enter the File Path along with File Name:-\n")
            myFilePath=myFilePath.strip()
            print(myFilePath)
            myFile=open(myFilePath,"at")
            myFile.write("This is Vijay\n")
        except FileNotFoundError:
            print("Please enter the correct file path that exists\n")
       


FileHandlingExp.collectFilePath()