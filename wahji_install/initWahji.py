#creates wahji files

import os, platform

def make(cur_dir):

        print "setting up Wahji in directory: %s" % cur_dir
        os.chdir(cur_dir)

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
	print "Creating html folder"
	os.mkdir("themes/js/html")

	"""creates hidden wahji file"""
	print "Creating .wahji file"
	file = open(".wahji","w")
	file.close()

	print "Done!"
