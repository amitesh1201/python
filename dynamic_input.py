#!/usr/bin/python

element = []
num = ""
add = 0
num = raw_input() 

# The range() function only does numbers from the fi rst to the last, not including the last. So it
# stops at two, not three, in the above. This turns out to be the most common way to do this kind
# of loop.


for i in range (1, int(num)):
    print "Adding %d to the list." %i
    element.append(i)
    num <= i

for i in element:
    print "Element : %d" %i   
    add = add + i

print "Addition %d" %add
