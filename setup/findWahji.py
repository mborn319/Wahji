import os, platform

def find():
	my_platform = platform.system()

	if my_platform == "Windows":
		"""Some code"""
	elif my_platform == "Linux":
		"""some code"""
	elif my_platform == "Darwin":
		lookfor = ".wahji"
		for root, dirs, files in os.walk('/Users'):
    			if lookfor in files:
					loc = root
					return loc
        				break
