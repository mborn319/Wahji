import yaml
"""This file opens the wahji.yml file, parses the site_name and theme,
   then outputs the corresponding values into an html file"""

stream = file('wahji.yml', 'r')

"""Converts the contents of wahji.yml into a python dictionary"""
site_info = yaml.load(stream) 

"""Iterates over the dictionary, assigning dictionary values to associated variables"""
for key, value in site_info.items():
    if key == "site_name":
        title = value
    if key == "theme":
        site_theme = value

"""Creates output.html file and writes to it using variables extracted from wahji.yml"""
f2 = open('output.html', 'w')
## TO DO:
## Finish html header
f2.write("<title>" + title + "</title> \n")
f2.write("<h1 class=\"" + site_theme + "\">Some Sort of Head Goes Here</h1>")
## TO DO:
## Finish html body
f2.close()
