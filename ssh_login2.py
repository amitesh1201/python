#!/usr/bin/python3.6

# Login to the user entered ip.

import sys, getopt, os

def usage():
    print("Use following option to ssh")
    print("-u: Enter user name to login")
    print("-l: Login to 192.168.x.x")

def login(user_name,user_ip):
    if not user_name or not user_ip:
        print("The username or user ip should not be empty")
    os.system("ssh " + user_name + "@" + user_ip)

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"u:l:h")
        if not opts:
            usage()
            sys.exit(2)
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-u"):
            if not arg:
                usage()
                sys.exit(2)
            user_name = arg
        if opt in ("-l"):
            if not arg:
                usage()
                sys.exit(2)
            user_ip = "192.168."+arg
        elif opt in ("-h"):
            usage()
            sys.exit(2)
    login(user_name, user_ip)


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except OSError as err:
      print("OS error: {0}".format(err))
