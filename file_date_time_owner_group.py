#!/usr/bin/python
# This script display the creation date, size, owner and group of the file.
import os, sys, datetime
from pwd import getpwuid
from grp import getgrgid

file_name=input("Enter the file name: ")

if not os.path.exists(file_name):
    print("Enter the valid file name")
    sys.exit(1)

if not os.path.isfile(file_name):
    print("Enter the valid file name")
    sys.exit(1)

    

cdate=datetime.datetime.fromtimestamp(os.path.getctime(file_name)).strftime("%Y %b %d")
size=os.path.getsize(file_name)
file_owner=getpwuid(os.stat(file_name).st_uid).pw_name
file_group=getgrgid(os.stat(file_name).st_gid).gr_name

print(f"Check the following creation date and size of the file {file_name} ") 
print(f"Creation date: {cdate}")
print(f"Size: {size}")
print(f"File Owner: {file_owner}")
print(f"File Group: {file_group}")
