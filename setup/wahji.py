#! /usr/bin/env python

def test1():
	print "Test1..going to Test2"
	test2()

def test2():
	print "Test2..."
	print "Bye!"

test1()
