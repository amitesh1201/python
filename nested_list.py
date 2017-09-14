#!/usr/local/bin/python

my_list = ["mouse",[1,2,3],['a']]
print my_list
print my_list[1]
print "0 to 1:"
print (my_list[0:1])
print "OUTPUT:"
print my_list[1][2]
list1 = my_list[1]
print "list1:"
print list1[1]

print "------------------"

for item in my_list:
    print item

my_list = ['p','r','o','g','r','a','m','i','z']
# elements 3rd to 5th
print(my_list[2:5])
