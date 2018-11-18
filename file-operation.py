#!/usr/bin/python3.6

# This script operate on the file.

import os
from sys import exit
from os import path

def check_file_dir(file_name):
    # Check the entered value is file or dir.
    if os.path.isdir(file_name):
       print("The ", file_name, "is directory")
       exit()

def file_operation(file_name):
    # Perform the operation on file.
    if os.path.isfile(file_name):
        # Check the absolute path of the file.
        file_path = os.path.abspath(file_name)
        edit_status = input("Do you wish to edit the file.(y/n): ")
        if edit_status == 'y':
            f = open(file_path, 'a')
            line = input("Enter the line..\n")
            f.write('\n' + line + '\n')
            f.close()
        else:
            exit()
    else:
        print ("The ", file_name, "not exist.")
        create_status = input("Do you wish to create file.(y/n): ")
        if create_status == "y":
            f = open(file_name, 'w')
            line = input("Enter the line..\n")
            f.write(line + '\n')
            f.close()
        else:
            exit()


def read_file(file_name):
    # Read the file.
    f = open(file_name)
    print (f.read())
    f.close()

### Main ###

file_name = input("Enter the file name: ")
if file_name == "":
    print("The file name should not be empty")
    exit()

check_file_dir(file_name)
file_operation(file_name)
read_file(file_name)


