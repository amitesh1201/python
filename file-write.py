#!/usr/bin/python3.6

# This script write to the file.
import os
from sys import exit

def check_file_dir(file_name):
    # Check entered value is file or dir.
    if os.path.isdir(file_name):
        print("The ", file_name, "is directory.")
        exit()
    elif os.path.isfile(file_name):
        print ("The ", file_name, "already exist.")
        exit()

def create_write_file(file_name):
    f = open(file_name,'w')
    line = input("Enter the lines..\n")
    f.write(line)
    f.close()

def read_file(file_name):
    f = open(file_name)
    print (f.read())
    f.close()


### Main ###

file_name = input("Enter the file name: ")
if file_name == "":
    print("The file name should not be empty.")
    exit()

check_file_dir(file_name)
create_write_file(file_name)
read_file(file_name)