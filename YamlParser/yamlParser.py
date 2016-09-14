"""
    wahji build
    This section generates variables to be used in static HTML files
"""

# FIRST: init the library needed for parsing Yaml
import yaml

"""
    Main function for parsing working variables from Yaml file.
    This can be pulled into another python script as a module.
"""
def yamlParse():
    stream = file('wahji.yml', 'r')

    # Converts the contents of wahji.yml into a python dictionary
    site_info = yaml.load(stream) 

    # return the python dictionary so that other scripts can get at the values
    return site_info
