#! /usr/bin/env python
import os
import sys
import argparse
import removeWahji
import findWahji
import initWahji
import newWahji
import buildWahji
import yamlParser

def wahjiUsage():
	return '''wahji [-h] {init,new <project_name>,build} '''

class wahji(object):
	def __init__(self):
		parser = argparse.ArgumentParser(description="Wahji is a static site generator. Here will be some details about the project.... ", usage=wahjiUsage())
		parser.add_argument('opt', help="Running wahji with the 'init' option will create the .wahji file in the CWD, and establish the themes directory. Running wahji with the new option requires an additonal parameter which is a project name. Running wahji with the build option will create the site directory.")
		args = parser.parse_args(sys.argv[1:2])
		getattr(self, args.opt)()

	def init(self):
		loc = findWahji.find()
		if not loc:
			initWahji.make()
		else:
			print "Wahji has already been initilized!"

	def remove(self):
		loc = findWahji.find()
		if not loc:
			print ".wahji was not found."
		else:
			removeWahji.rem(loc)

	def new(self):
		loc = findWahji.find()

		if not loc:
			print ".wahji has not been initilized."
		else:
			parser = argparse.ArgumentParser(description='Create a new wahji project', usage=wahjiUsage())
			parser.add_argument('project_name')
			args = parser.parse_args(sys.argv[2:])
			print "Creating " + args.project_name + " at " + loc
			newWahji.site(args.project_name, loc)

	def build(self):
		loc = findWahji.find()


		if not loc:
			print ".wahji file not found"
		else:
			# Get [project_name] from arguments
			parser = argparse.ArgumentParser(description='Create a new wahji project', usage=wahjiUsage())
			parser.add_argument('project_name')
			args = parser.parse_args(sys.argv[2:])

			# Read the site-specific wahji.yml settings file
                        site_dir = loc + "/" + args.project_name
			site_settings = yamlParser.yamlParse(site_dir)

			print "Site settings:"
			print site_settings

			# Run the build script
                        buildWahji.build(site_dir,site_settings)

if __name__ == "__main__":
	wahji()
