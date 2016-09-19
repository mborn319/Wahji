#deletes wahji content
import os, shutil, platform

def rem(loc):

	os.chdir(loc)
	
	site = raw_input("Input site folder: ")

	print "Are you sure you want to delete", site, "Y/N: "
	confirm = raw_input()
	
	if confirm == "Y" or confirm == "y":
		"""delete site folder"""
		shutil.rmtree(site)
		print "Deleting site"

	elif confirm == "N" or confirm == "n":
		print "Site folder was not deleted"

