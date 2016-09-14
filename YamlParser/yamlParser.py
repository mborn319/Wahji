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
def main():
    stream = file('wahji.yml', 'r')

    # Converts the contents of wahji.yml into a python dictionary
    site_info = yaml.load(stream) 

    # Iterates over the dictionary, assigning dictionary values to associated variables
    for key, value in site_info.items():
        if key == "site_name":
            title = value
        if key == "theme":
            site_theme = value

    # Creates title_tag based on parsed data from the wahji.yml
    title_tag = "<title>" + title + "</title> \n"
if __name__ == "__main__":
    main()
