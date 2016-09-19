import os, shutil
import yamlParser

def site(project_name, wahji_dir):

    title_tag, site_theme = yamlParser.yamlParse()

    print site_theme

    # Create the new site directory
    os.mkdir(project_name)
    os.chdir(project_name)

    # Copy the default content from the Wahji installation dir to the new site dir
    shutil.copytree(wahji_dir + "/content", project_name + "content")
    shutil.copytree(wahji_dir + "/themes/" + site_theme,"themes")
