#!/usr/bin/python

i = 0
numbers = []
while i < 6:
    print "%d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers

    print "%d" % i


print "The numbers: "

for num in numbers:
   print num
