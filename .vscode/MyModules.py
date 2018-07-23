import platform

def systemInfoDisplay():
    x=platform.system()
    print("Your System is:-\n",x,"\n")
    x=dir(platform)
    print("All variables and functions in your system are:-",x)
def printFunction(textToPrint):
    print("\n Here is the text you have passed \n",textToPrint)
def printArchitecture():
    print("\n Here is the text you have passed \n",platform.architecture)