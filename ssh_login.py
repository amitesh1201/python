#!/usr/bin/python3.6

# Login to the user entered ip.

import sys, getopt, os

def usage():
    print("Use following option to ssh")
    print("-u: Enter user name to login")
    print("-f: Login to 192.168.50.x")
    print("-s: Login to 192.168.60.x")
    print("-a:  Enter any IP to login")

def login(user_name,user_ip):
    if not user_name or not user_ip:
        print("The username or user ip should not be empty")
    os.system("ssh " + user_name + "@" + user_ip)

def main(argv):
    try:
        user_name = "csadmin"
        opts, args = getopt.getopt(argv,"u:f:s:a:h")
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
        if opt in ("-f"):
            if not arg:
                usage()
                sys.exit(2)
            user_ip = "192.168.50."+arg
        elif opt in ("-s"):
            if not arg:
                usage()
                sys.exit(2)
            user_ip = "192.168.60."+arg
        elif opt in ("-a"):
            if not arg:
                usage()
                sys.exit(2)
            user_ip = arg
        elif opt in ("-h"):
            usage()
            sys.exit(2)
    login(user_name, user_ip)


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except OSError as err:
      print("OS error: {0}".format(err))
