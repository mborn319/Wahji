#creates wahji files

import os, platform

def make():

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
