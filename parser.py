import markdown

md = open("test.md","r+")
md = md.read()
md = markdown.markdown(md)

html = open("test.html","w")
html.write(md);
html.close()
