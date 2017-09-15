#!/usr/local/bin/python

import sys

mylist = []
printlist = []

def listfn(*list1):
    mylist.append(list1)

    return list(mylist);

#def display(*list2):
#    for var in list2:
#        print var
#    return

while True:
    print "Enter the y for continue or n for exit"
    flag = raw_input()
    if flag == 'y':
        print "Enter the value: "
        user_input = raw_input()
        printlist.append(listfn(user_input))
    elif flag == 'n':
        #display(printlist)
        print printlist
        sys.exit()
    else:
        print "Enter the y for continue or n for exit"


