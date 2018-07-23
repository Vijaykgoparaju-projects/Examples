class FileHandlingExp:

    def collectFilePath():
        
        try:
            myFileName=input("Enter the File name:-\n")
            myFileName.strip()
            print(myFileName)
            myFile=open(myFileName,"xt")
            myFile=open(myFileName,"wt")
            myFile.write("This is Vijay\n")
        except FileNotFoundError:
            print("Please enter the correct file path that exists\n")
       


FileHandlingExp.collectFilePath()