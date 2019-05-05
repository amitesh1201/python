#!/usr/bin/python3.6

# Login to the user entered ip.

import sys, getopt, os

def usage():
    print("Use following option to ssh")
    print("-s: Enter user name to login")
    print("-f: Login to 192.168.50.x")
    print("-s: Login to 192.168.60.x")

def login(user_name,user_ip):
    os.system("ssh " + user_name + "@" + user_ip)

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"u:f:s:h")
        if not opts:
            usage()
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-u"):
            user_name = arg
            if not user_name:
                usage()
                exit (2)
        if opt in ("-f"):
            if not arg:
                usage()
                exit (2)
            user_ip = "192.168.50."+arg
        elif opt in ("-s"):
            if not arg:
                usage()
                exit (2)
            user_ip = "192.168.60."+arg

    login(user_name,user_ip)

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except OSError as err:
      print("OS error: {0}".format(err))
