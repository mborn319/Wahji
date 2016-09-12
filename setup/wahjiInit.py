#creates wahji files

import os, platform

def make():
	for root, dir, files in os.walk("."):
	        if ".wahji" in files:
	            print "Found .wahji!"
	            boolean = True
	            break
	        else:
	            print "Couldn't find .wahji."
	            boolean = False
	            break

	if boolean == False:
		"""creates theme folder and its contents"""
		os.mkdir("content")
		os.mkdir("themes")
		os.mkdir("themes/css")
		os.mkdir("themes/img")
		os.mkdir("themes/js")

		"""creates hidden wahji file"""
		file = open(".wahji","w")
		file.close()

		"""creates 404.html file"""
		file = open("404.html","w+")
		file.close()

		"""checks os to figure out where command directory will go"""
		my_platform = platform.system()

		if my_platform == "CYGWIN_NT-6.1":
			print "You're using CYGWIN_NT-6! Your command directory will be "
			print "located in the current directory."
			os.mkdir("commands")

		elif my_platform == "Windows":
			print "You're using Windows! Your command directory will be "
			print "located in the current directory."
			os.mkdir("commands")

		elif my_platform == "Linux":
			print "You're using Linux! Your command directory will be located in "
			print "/usr/local/lib/python2.7/dist-packages/wahji/commands"
			os.mkdir("/usr/local/lib/python2.7/dist-packages/wahji")
			os.mkdir("/usr/local/lib/python2.7/dist-packages/wahji/commands")

		elif my_platform == "Darwin":
			print "You're using Mac OS! Your command directory will be  "
			print "located in the current directory."
			os.mkdir("commands")

		else:
			os.mkdir("commands")
	else:
		print "Wahji has already been initilized."
