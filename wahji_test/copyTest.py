import os

directory = os.path.abspath("/home/ubuntu/CS370/wahji_test/content/")
if os.path.exists(directory):
    os.chdir(directory)
else:
    print "***" + directory + " does not exist***"
print "The current directory is " + os.getcwd()
