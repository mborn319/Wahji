import yaml

"""
    yamlParse function for parsing working variables from Yaml file.
    This can be pulled into another python script as a module.
"""
def yamlParse():
    stream = file('wahji.yml', 'r')

    # Converts the contents of wahji.yml into a python dictionary
    site_info = yaml.load(stream) 

    # Later, we'll probably do special stuff with these settings

    # Return the python dictionary / object.
    return title_tag, site_theme
