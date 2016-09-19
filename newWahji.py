import os, shutil
import yamlParser

def site(project_name, wahji_dir):
    site_dir = wahji_dir + "/" + project_name

    # Create the new site directory
    os.mkdir(project_name)
    os.chdir(project_name)

    # Copy the default site settings file into the new site dir
    shutil.copyfile(wahji_dir + "/wahji.yml",site_dir + "/wahji.yml")

    # Copy the default content from the Wahji installation dir to the new site dir
    shutil.copytree(wahji_dir + "/content", site_dir + "/content")

    # Now that we have a site-specific wahji.yml settings file, read it!
    site_settings = yamlParser.yamlParse(site_dir)

    print "Site settings:"
    print site_settings

    # Copy the default theme from the Wahji installation dir to the new site dir
    shutil.copytree(wahji_dir + "/themes/" + site_settings["theme"], site_dir + "/themes")
