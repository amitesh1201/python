#!/usr/bin/python

def cheese_and_crackers(cheese_count, boxes_of_crackers):
   print "%d cheese" % cheese_count
   print "%d boxes of crackers" % boxes_of_crackers

   
print "We can just give the function numbers directly:"
cheese_and_crackers(10, 30)

print "Use variable from script:"
cheese_no = 40
boxes_no = 50

cheese_and_crackers(cheese_no, boxes_no)

print "We can do math inside to.:"
cheese_and_crackers(10 + 30,40 + 10)   



print "We can combine two, variable and math:"
cheese_and_crackers(cheese_no + 10, boxes_no + 40)
 
   
