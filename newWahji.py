import os, shutil
import yamlParser

def site(project_name, wahji_dir):
    site_dir = wahji_dir + "/" + project_name

    # Create the new site directory
    os.mkdir(project_name)
    os.chdir(project_name)

    # Copy the default content from the Wahji installation dir to the new site dir
    shutil.copytree(wahji_dir + "/content", project_name + "content")

    # Now that we have a site-specific wahji.yml settings file, read it!
    site_settings = yamlParser.yamlParse(site_dir)

    print site_theme

    # Copy the default theme from the Wahji installation dir to the new site dir
    shutil.copytree(wahji_dir + "/themes/" + site_settings.theme,"themes")
