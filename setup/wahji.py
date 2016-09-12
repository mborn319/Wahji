#! /usr/bin/env python
#Template Wahji file
import os
import sys
import argparse


def wahjiUsage():
	return '''wahji [-h] {init,new <project_name>,build} '''

class Wahji(object):
	def __init__(self):
		parser = argparse.ArgumentParser(description="Wahji is a static site generator. Here will be some details about the project.... ", usage=wahjiUsage())
		parser.add_argument('opt', help="Running wahji with the 'init' option will create the .wahji file in the CWD, and establish the themes directory. Running wahji with the new option requires an additonal parameter which is a project name. Running wahji with the build option will create the site directory.")
		args = parser.parse_args(sys.argv[1:2])
		getattr(self, args.opt)()

	def init(self):
		print "call the init module..."

	def new(self):
		parser = argparse.ArgumentParser(description='Create a new wahji project', usage=wahjiUsage())
		parser.add_argument('project_name')
		args = parser.parse_args(sys.argv[2:])
		print "Creating " + args.project_name + "..."

	def build(self):
		print "call build module..."

if __name__ == "__main__":
	Wahji()
