import os, platform, glob

def find():
        wahji_dir = False
        lookfor = ".wahji"
	my_platform = platform.system()

	if my_platform == "Windows":
		"""Some code"""
	elif my_platform == "Linux":
                """
                    Get user's current working directory
                    Cite: http://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
                """
                current_dir = os.getcwd()
                while True:
                        print "Searching " + os.getcwd() + " directory for .wahji file"
                        if glob.glob(".wahji"):
                                # Found it!!
                                wahji_dir = os.getcwd()
                                print "Wahji is installed in " + wahji_dir
                                break
                        elif os.getcwd() == "/":
                                # At root directory, have not found .wahji file
                                break
                        else:
                                # Search one level up
                                os.chdir("..")
                """
                    Thoughts: could we just traverse up through the current working directory
                    (NOT necessarily the installed directory!) to find the .wahji file?
                    This is better than trying to guess where the .wahji file is,
                    ESPECIALLY since recursively searching file by file can be really slow.
		for root, dirs, files in os.walk('/home'):
    			if lookfor in files:
					loc = root
					return loc
        				break
                """
                return wahji_dir
	elif my_platform == "Darwin":
		for root, dirs, files in os.walk('/Users'):
    			if lookfor in files:
					loc = root
					return loc
        				break
