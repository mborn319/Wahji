import os

def createDirectories():
    current = os.getcwd()

    items = [f for f in os.listdir(current) if os.path.isdir(os.path.join(current, f))]
    new = current + "/Site"
    os.mkdir(new)
    os.chdir(new)
    for i in items:
        os.mkdir(new + "/" + i)

def copyFiles():
    current = os.getcwd()
    print "The current directory is " + current


createDirectories()
copyFiles()
    
