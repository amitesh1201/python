#!/usr/bin/python

from sys import argv
from os.path import exists 

script, from_file, to_file = argv

print "Copy file %s to %s" % (from_file, to_file)


in_file = open(from_file)
indata = in_file.read()

print "The input file is %d byte long" % len(indata)

print "Does the out put file exist? %r" % exists(to_file)
print "Press enter to continue. CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
in_file.close()

print "Following content of the file %s" % to_file
dst_file = open(to_file)
print dst_file.read()
