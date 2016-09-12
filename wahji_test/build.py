import os, sys, platform, shutil

def createSite():
    os.mkdir("Site")
    print os.getcwd()

def fname():
    for root, dir, files in os.walk("."):
        if ".wahji" in files:
            print "Found it!"
	    createSite()
	    return True
	    break
        else:
	    return False
	    break

boolean = fname()


if boolean == True:
    file1 = open("/home/ubuntu/CS370/wahji_test/404.html", "r+")
    file2 = open("/home/ubuntu/CS370/wahji_test/Site/404.html", "w+")
    str1 = file1.read()
    file2.write(str1)
    file1.close()
    file2.close()
    count = 0
    current = os.getcwd()
    files = [f for f in os.listdir(current) if os.path.isfile(os.path.join(current, f))]
    for f in files:
	print f
	count += 1
    print "Total files: " + str(count)
    menu_flag = False 
