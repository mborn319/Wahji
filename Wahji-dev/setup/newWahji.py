import os, shutil
import yamlParser

def site(name):

    title_tag, site_theme = yamlParser.yamlParse()

    print site_theme

    os.mkdir(name)
    os.chdir(name)

    shutil.copytree("/home/dadeeley67/git/Wahji/setup/content","content")
    shutil.copytree("/home/dadeeley67/git/Wahji/setup/themes/"+site_theme,"themes")
    shutil.copy("/home/dadeeley67/git/Wahji/setup/404.html","404.html")
