#!/usr/bin/python3.6

# This file performs the git operations
# like status, add, commit, push

import sys, getopt, os

def usage():
    print("Check the following options")
    print("-s,--status:        Display the status")
    print("-a,--add <args>:    Add newly created file to the git")
    print("-m,--commit <args>: Commit the file")
    print("-p,--push:          Push the file to the git branch")

def get_branch():
    os.system("git status")


def add_file(file_name):
    # Add to check the file exist or not
    if os.path.isfile(file_name):
        os.system("git add", file_name)
    else:
        print("The file", file_name, "not exit")
        sys.exit(2)

def commit_file(msg):
    os.system("git commit -m", msg)

def push_file():
   os.system("git push")

def get_branch():
    os.system("git branch")

def main(argv):
    try:
        opts, argv =getopt.getopt(argv,"sa:m:pb,h",["status","add=","commit=","push","branch","help"])
        if not opts:
            usage()
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, argv in opts:
        if opt in ("-s","--status"):
            get_branch()
        elif opt in ("-a","--add"):
            if not argv:
                add_file(argv)
        elif opt in ("-m","--commit"):
            if not argv:
                commit_file(argv)
        elif opt in ("-p","--push"):
            push_file()
        elif opt in ("-b","--branch"):
            get_branch()
        elif opt in ("-h","--help"):
            usage()



if __name__ == '__main__':
   main(sys.argv[1:])
