filepath=input("Enter the file path")
f=open(filepath,"w")
inputText="This is starting of file"
while(inputText!=""):
    inputText=input("Enter the text you want to write\n")
    f.writelines(inputText)
    f.writelines("\n")
f=open(filepath)
for x in f:
    print(x)
