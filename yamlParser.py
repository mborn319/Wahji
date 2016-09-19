import yaml

"""
    yamlParse function for parsing working variables from any yaml file.
    This can be pulled into another python script as a module.
"""
def yamlParse(site_dir):
    filename = 'wahji.yml'

    # get the settings file for the given site directory
    stream = file(site_dir + "/" + filename, 'r')

    # Converts the contents of wahji.yml into a python dictionary
    data = yaml.load(stream) 

    # Later, we'll probably do special stuff with these settings

    # Return the python dictionary / object.
    return data
