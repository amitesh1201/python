#!/usr/bin/python

from sys import argv

script, filename = argv

print "Erase content of the file %r" % filename
print "Use CTRL-C to cancel"
print "Cont. to erase, press enter"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file."
target.truncate()


print "Enter three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Write to the file."

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

print "Close the file."
target.close()

print "\n"

print "Read the following file %s" % filename
target = open(filename)
print target.read()
