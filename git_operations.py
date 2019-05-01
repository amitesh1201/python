#!/usr/bin/python3.6

# This file performs the git operations.

import sys, getopt, os

def usage():
    print("Check the following options")
    print("-s,--status:        Display the status")
    print("-a,--add <args>:    Add newly created file to the git")
    print("-m,--commit <args>: Commit the file")
    print("-p,--push:          Push the file to the git branch")

def get_branch():
    os.system("git status")


#def add_file():

#def commit_file():

#def push_file():


def main(argv):
    try:
        opts, argv =getopt.getopt(argv,"sa:m:p,h",["status","add=","commit=","push","help"])
        if not opts:
            usage()
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, argv in opts:
        if opt in ("-s","--status"):
            get_branch()
        elif opt in ("-a","--add"):





if __name__ == '__main__':
   main(sys.argv[1:])
