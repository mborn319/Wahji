#deletes wahji content
import os, shutil, platform

def rem(loc):

	os.chdir(loc)
	
	print "deleting content"
		
	"""delete them folder and its contents"""
	shutil.rmtree("themes")

	"""delete .wahji file"""
	os.remove(".wahji")

	"""delete 4040.html file"""
	os.remove("404.html")

	"""delete content folder"""
	shutil.rmtree("content")

