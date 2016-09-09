# this is the build script


# FIRST: init the libraries we need for parsing Yaml, Markdown
import markdown

# Second: read the HTML & Markdown files into a string
htmlfile = open('template.html','r')
htmlfile = htmlfile.read().strip('.')
mdfile = open('content.md','r')
mdfile = mdfile.read().strip('.')

# Third: parse the markdown into an HTML string
content = markdown.markdown(mdfile)

# Fourth: replace the {content_here} blocks in the HTML with markdown
html = htmlfile.replace('{content_here}',content)

# Fifth: save the generated HTML into a new file.
newfile = open('output/index.html','w')
newfile.write(html)
