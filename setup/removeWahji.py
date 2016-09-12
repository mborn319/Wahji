#deletes wahji content
import os, shutil, platform

def rem():
	for root, dir, files in os.walk("."):
	        if ".wahji" in files:
	            print "Found it!"
	            boolean = True
	            break
	        else:
	            print "Couldn't find .wahji."
	            boolean = False
	            break
	if boolean == True:

		"""delete them folder and its contents"""
		shutil.rmtree("themes")

		"""delete .wahji file"""
		os.remove(".wahji")

		"""delete 4040.html file"""
		os.remove("404.html")

		"""delete content folder"""
		shutil.rmtree("content")

		"""checks os to figure out where command directory will go"""
		my_platform = platform.system()

		if my_platform == "CYGWIN_NT-6.1":
			os.rmdir("commands")
			print "Deleted wahji files."
		elif my_platform == "Windows":
			os.rmdir("commands")
			print "Deleted wahji files."
		elif my_platform == "Linux":
			os.rmdir("/usr/local/lib/python2.7/dist-packages/wahji/commands")
			os.rmdir("/usr/local/lib/python2.7/dist-packages/wahji")
			print "Deleted wahji files."
		elif my_platform == "Darwin":
			os.rmdir("commands")
			print "Deleted wahji files."
		else:
			os.rmdir("commands")
			print "Deleted wahji files."
