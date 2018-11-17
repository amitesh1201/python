#!/usr/bin/python3.6

# This script creates the directory.

dir_name =  input("Enter dir path: ")

try:
    # Create the target directory.
    os.mkdir(dir_name)
    print ("Directory ", dir_name , " created ")
except FileExistsError:
    print("Directory ", dir_name , " already exist")