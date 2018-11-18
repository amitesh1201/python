#!/usr/bin/python3.6

# This script create the file.

import os
from sys import exit

def check_file_dir(file_name):

    # Check user enter value is dir or file.
    if path.isdir(file_name):
        print("The ", file_name, "is directory")
    elif path.isfile(file_name):
        print("The ", file_name, "is file already exist")

def create_file(file_name):
    # Open the file in write mode.
    f = open(file_name, 'w')
    f.close()
    print("The empty file ", file_name, "is created.")



### Main Section ###

file_name = input("Enter file name: ")
if file_name == "":
    print("The file name should not be empty")
    exit()
else:
   check_file_dir(file_name)
   create_file(file_name)
