import os, platform

def find():
	my_platform = platform.system()

	if my_platform == "Windows":
		"""Some code"""
	elif my_platform == "Linux":
		lookfor = ".wahji"
		for root, dirs, files in os.walk('/home'):
    			if lookfor in files:
					loc = root
					return loc
        				break
	elif my_platform == "Darwin":
		lookfor = ".wahji"
		for root, dirs, files in os.walk('/Users'):
    			if lookfor in files:
					loc = root
					return loc
        				break
