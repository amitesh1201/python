#!/usr/bin/python3.6

# This script operate on the file.

import os
from sys import exit



def check_file_dir(file_name):
    # Check the entered value is file or dir.
    if os.path.isdir(file_name):
       print("The ", file_name, "is directory")
       exit()
    elif os.path.isfile(file_name):
       print("The ", file_name, "is the file")

def file_operation(file_name):
    if os.path.isfile(file_name):
        f = open(file_name,'a')

# If file exist then display the operation mode.

# If file not exist then ask user to create the file or not.

# If user select the operation create file then open in to append/write mode.

