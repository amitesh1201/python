#!/usr/bin/python3.6

# This script creates the directory.
import os
import errno

dir_name =  input("Enter dir path: ")

try:
    # Create the target directory.
    os.mkdir(dir_name)
    print ("Directory ", dir_name , " created ")
#except OSError as e:
except FileNotFoundError:
    #if e.errno != errno.EEXIST:
      print("Directory ", dir_name , " already exist")