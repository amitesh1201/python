#!/usr/bin/python3.6

# This file performs the git operations
# like status, add, commit, push, checkout, pull

import sys, getopt, os

def usage():
    print("Check the following options\n")
    print("-s,--status:                  Display the status")
    print("-a,--add <file_name>:         Add newly created file to the git")
    print("-m,--commit <args>:           Commit the file")
    print("-p,--push:                    Push the file to the git branch")
    print("-c,--check-out <brach_name>:  Changed the branch")
    print("-l,--pull:                    Pull data")

def get_status():
    os.system("git status")

def add_file(file_name):
    if os.path.isfile(file_name):
        os.system("git add " + file_name)
        print("git add " + file_name)
    else:
        print("The file", file_name, "not exit")
        sys.exit(2)

def commit_file(msg):
    print("git commit -m " + '"msg"')
    os.system("git commit -m " + '"msg"')

def push_file():
   os.system("git push")

def get_branch():
    os.system("git branch")

def checkout_branch(brach_name):
    print("git checkout " + brach_name)
    os.system("git checkout " + brach_name)

def pull_data():
    os.system("git pull")

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"sa:m:pbc:l,h",["status","add=","commit=","push","branch","check-out","pull","help"])
        #print("opts", opts)
        #print("args", args)
        if not opts:
            usage()
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-s","--status"):
            get_status()
        elif opt in ("-a","--add"):
            file_name = arg
            if file_name:
                add_file(file_name)
            else:
                usage()
                sys.exit(2)
        elif opt in ("-m","--commit"):
            if arg:
                print(arg)
                commit_file(arg)
            else:
                usage()
                sys.exit(2)
        elif opt in ("-p","--push"):
            push_file()
        elif opt in ("-b","--branch"):
            get_branch()
        elif opt in ("-c","--check-out"):
            if arg:
               checkout_branch(arg)
            else:
                usage()
                sys.exit(2)
        elif opt in ("-l","pull"):
            pull_data()
        elif opt in ("-h","--help"):
            usage()



if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except OSError as err:
      print("OS error: {0}".format(err))

