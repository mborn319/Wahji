import os

def copyFile(i, new):
    print "In copyFile and file is " + i
    print "In copyFile and new directory is " + new
    f1 = open(i, "r+")
    f2 = open(new + i, "w+")
    content = f1.read()
    f2.write(content)
    f1.close()
    f2.close()
    return

def copyDirectory(i, new):
    os.chdir(new)
    os.mkdir(i)
    return

def getDirectoryContents(current, new):
    for i in os.listdir(current):
        if os.path.isfile(i):
	    copyFile(i, new)
        elif os.path.isdir(i):
	    copyDirectory(i, new)
	    another = os.getcwd()
	    another = another + "/" + i + "/"
	    os.chdir(another)
	    print "Another is " + another
	    getDirectoryContents(another, new)
    return

def main():
    current = os.getcwd()
    new = current + "/Site/"
    os.mkdir(new)
    print "In main and current directory is " + current
    print "In main and new directory is " + new
    getDirectoryContents(current, new)

if __name__ == "__main__":
    main()    
