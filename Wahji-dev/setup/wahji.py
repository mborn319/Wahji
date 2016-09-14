#! /usr/bin/env python
#Template Wahji file
import os
import sys
import argparse
import wahjiInit
import removeWahji
import findWahji

def wahjiUsage():
	return '''wahji [-h] {init,new <project_name>,build} '''

class Wahji(object):
	def __init__(self):
		parser = argparse.ArgumentParser(description="Wahji is a static site generator. Here will be some details about the project.... ", usage=wahjiUsage())
		parser.add_argument('opt', help="Running wahji with the 'init' option will create the .wahji file in the CWD, and establish the themes directory. Running wahji with the new option requires an additonal parameter which is a project name. Running wahji with the build option will create the site directory.")
		args = parser.parse_args(sys.argv[1:2])
		getattr(self, args.opt)()

	def init(self):
		loc = findWahji.find()
		if not loc:
			wahjiInit.make()
		else:
			print "Wahji has already been initilized!"

	def remove(self):
		loc = findWahji.find()
		if not loc:
			print ".wahji was not found."
		else:
			removeWahji.rem(loc)

	def new(self):
		boolean = findWahji.find()

		if boolean == True:
			parser = argparse.ArgumentParser(description='Create a new wahji project', usage=wahjiUsage())
			parser.add_argument('project_name')
			args = parser.parse_args(sys.argv[2:])
			print "Creating " + args.project_name + "..."
		else:
			print ".wahji file not found"

	def build(self):
		boolean = findWahji.find()

		if boolean == True:
			print "call build module..."
		else:
			print ".wahji file not found"

if __name__ == "__main__":
	Wahji()
