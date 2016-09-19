import markdown, os

def build(site_dir, site_settings):
    content_dir = site_dir + "/content"
    theme_dir = site_dir + "/themes/"
    
    # Get a list of files from a given directory
    def getFiles(dirname):
	return os.listdir(dirname)

    # Read the contents of a given file.
    def readFile(thefilename):
	thefile = open(thefilename, "r")
	return thefile.read().strip(".")

    # Get the filename of a file with no extension.
    def basename(thefilename):
	pos =  thefilename.find(".")
	return thefilename.replace(thefilename[pos:], "")

    # Get the HTML template (Notice we always use the theme's index.html file)
    htmlfile = readFile(theme_dir + "/index.html")

    # For each markdown file in the content/ folder...
    contentfiles = getFiles(content_dir)
    for filename in contentfiles:
        full_filename = content_dir + "/" + filename
        new_filename = basename(filename) + ".html"
        if os.path.isdir(full_filename):
            # For now, skip over directories
            continue
	# read the Markdown file into a string
	mdfile = readFile(content_dir + "/" + filename)

	# parse the markdown into an HTML string
	content = markdown.markdown(mdfile)

	# replace the {content_here} blocks in the HTML with markdown
	html = htmlfile.replace("{content_here}",content)

	# save the generated HTML into a new file.
	newfile = open(site_dir + "/" + new_filename,"w")
	newfile.write(html)

	# Nice message
	print "Generated " + new_filename
