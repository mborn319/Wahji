#deletes wahji content

import os, shutil, platform

"""delete them folder and its contents"""
shutil.rmtree("themes")

"""delete .wahji file"""
os.remove(".wahji")

"""delete 4040.html file"""
os.remove("404.html")

"""delete content folder"""
shutil.rmtree("content")

"""delete test.html file"""
os.remove("test.html")

"""checks os to figure out where command directory will go"""
my_platform = platform.system()

if my_platform == "CYGWIN_NT-6.1":
	os.rmdir("commands")
elif my_platform == "Windows":
	"""Some code to remove directory"""
elif my_platform == "Linux":
	os.rmdir("/usr/local/lib/python2.7/dist-packages/wahji/commands")
	os.rmdir("/usr/local/lib/python2.7/dist-packages/wahji")
elif my_platform == "Darwin":
	os.rmdir("commands")
else:
	os.rmdir("commands")
print "Deleted wahji files."
