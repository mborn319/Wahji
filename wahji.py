"""
    wahji build
    This section generates the static HTML files
"""

# FIRST: init the libraries we need for parsing Yaml, Markdown
import markdown
from os.path import basename

"""
    For each file in the themes/html folder...
"""
htmlfiles = getFiles('themes/html')
for filename in htmlfiles:
    # read the HTML & Markdown files into a string
    htmlfile = readFile(filename)

    # Get the markdown file with the same name (not the same extension!)
    # as the HTML template file
    mdfilename = open(basename(filename)
    mdfile = readFile(mdfilename)

    # parse the markdown into an HTML string
    content = markdown.markdown(mdfile)

    # replace the {content_here} blocks in the HTML with markdown
    html = htmlfile.replace('{content_here}',content)

    # save the generated HTML into a new file.
    newfile = open('output/' + filename,'w')
    newfile.write(html)

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
