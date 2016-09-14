#creates wahji files

import os, platform

def make():


	"""creates theme folder and its contents"""
	print "Creating content folder"
	os.mkdir("content")
	print "Creating themes folder"
	os.mkdir("themes")
	print "Creating CSS folder"
	os.mkdir("themes/css")
	print "Creating img folder"
	os.mkdir("themes/img")
	print "Creating js folder"
	os.mkdir("themes/js")

	"""creates hidden wahji file"""
	print "Creating .wahji file"
	file = open(".wahji","w")
	file.close()

	"""creates 404.html file"""
	print "Creating 404.html file"
	file = open("404.html","w+")
	file.close()

	print "Done!"
