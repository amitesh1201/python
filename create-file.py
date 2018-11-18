#!/usr/bin/python3.6

# This script create the file.

import os
file_name = input("Enter file name: ")

f = open(file_name,'w')
f.close()
print("The empty file ", file_name, "is created.")
