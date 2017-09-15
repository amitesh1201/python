#!/usr/local/bin/python

class Parent:
    def myMethod(self):
        print "Calling parent method."

class Child:
    def myMethod(self):
        print "Calling child method."


c = Child()
c.myMethod()

p = Parent()
p.myMethod()
