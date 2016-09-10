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
