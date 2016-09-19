import os, platform

def find():
        lookfor = ".wahji"
	my_platform = platform.system()

	if my_platform == "Windows":
		"""Some code"""
	elif my_platform == "Linux":
                """
                    Thoughts: could we just traverse up through the current working directory
                    (NOT necessarily the installed directory!) to find the .wahji file?
                    This is better than trying to guess where the .wahji file is,
                    ESPECIALLY since recursively searching file by file can be really slow.
                """
		for root, dirs, files in os.walk('/home'):
    			if lookfor in files:
					loc = root
					return loc
        				break
	elif my_platform == "Darwin":
		for root, dirs, files in os.walk('/Users'):
    			if lookfor in files:
					loc = root
					return loc
        				break
