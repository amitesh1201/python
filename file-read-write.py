#!/usr/bin/python3.6

# This script read content from one file write to another file.

import os
from sys import exit
# Get read file name, check this file is exist or not.


def file_exist(file_name):
    global file_exist_status
    if os.path.isdir(file_name):
        print ("This ", file_name, "is direcotry")
        exit()
    if os.path.isfile(file_name):
       print("The ",file_name, "file exist")
       file_exist_status=1
    else:
        print("The ",file_name,"not exist")
        file_exist_status=0

def read_file(read_file_name):
    global read_line
    f_read = open(read_file_name)
    read_line = f_read.read()
    f_read.close()

def write_file(write_file_name):
    f_write_file = open(write_file_name, 'w')
    f_write_file.write(read_line)
    f_write_file.close()

def file_operation(read_file_name,write_file_name):
    file_exist(read_file_name)
    if file_exist_status == 1:
       read_file(read_file_name)
       file_exist(write_file_name)
       if file_exist_status == 1:
          print("The ", write_file_name, "file exist.")
          file_status = input("Do you wish to over write the file(y/n): ")
          if file_status == 'y':
             write_file(write_file_name)
             print("The ",write_file_name, "file has been over written")
          else:
              print("The file has not been over written")
              exit()
       else:
           write_file(write_file_name)
           print("The ",write_file_name,"file has been written")
    else:
        print("The ", read_file_name, "file not exist")
        exit()




### Main Section ###

read_file_name = input("Enter the file name to read: ")
write_file_name = input("Enter the file name to write: ")
file_operation(read_file_name,write_file_name)

# Wrtie the content to the file, Check the file exist or not
# If file exist then display the message that over write the file or not.
# If file not exist then create the new file and write the content to the file.

