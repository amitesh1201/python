#!/usr/bin/python

from sys import argv

script, filename = argv

txt = open(filename)

print "File name is %s" % filename
print txt.read()

print "Enter another file name" 
file_another = raw_input("> ")

txt_another = open(file_another)
print txt_another.read()


