filepath=input("Enter the file path")
print(filepath.strip())
f=open(filepath)
for x in f:
    print(x,"\n\n\n")