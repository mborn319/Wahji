# deletes wahji content
import os, shutil, platform

def rem(loc):
        
	os.chdir(loc)
	
	print "deleting content"
		
	# delete them folder and its contents
	shutil.rmtree("themes")

	# delete content folder
	shutil.rmtree("content")

