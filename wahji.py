#! /usr/bin/env python

""" 
    wahji new [site_name]
    Sets up the folder structure so that the user is ready to edit their website.
"""
import os, platform

def fname():
	for root, dir, files in os.walk("."):
	        if ".wahji" in files:
	            print "Found it!"
	            return True
	            break
	        else:
	            print "Couldn't find .wahji."
	            return False
	            break

boolean = fname()

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

"""
    wahji build
    This section generates the static HTML files
"""

# FIRST: init the libraries we need for parsing Yaml, Markdown
import markdown
import os
#from os.path import basename

"""
    Functions for working with files
"""
# Get a list of files from a given directory
def getFiles(dirname):
    return os.listdir(dirname)

# Read the contents of a given file.
def readFile(thefilename):
    thefile = open(thefilename, 'r')

    return thefile.read().strip('.')

def basename(thefilename):
    pos =  thefilename.find('.')
    return thefilename.replace(thefilename[pos:], '')

# Get the HTML template (just one hardcoded filename for now)
htmlfile = readFile('template.html')

"""
    For each markdown file in the content/ folder...
"""
contentfiles = getFiles('content')
for filename in contentfiles:
    # read the Markdown file into a string
    mdfile = readFile('content/' + filename)

    # parse the markdown into an HTML string
    content = markdown.markdown(mdfile)

    # replace the {content_here} blocks in the HTML with markdown
    html = htmlfile.replace('{content_here}',content)

    # save the generated HTML into a new file.
    newfile = open('output/' + basename(filename) + '.html','w')
    newfile.write(html)

    print filename
