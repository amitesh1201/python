#!/usr/bin/python3.6

import os
from sys import exit

class Parent:
    parentAttr = 100
    def __init__(self):
        print ("Calling parent constructor")

    def parentMethod(self):
        print("Call parent method")

    def setAttr(self, attr):
         Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute: ", Parent.parentAttr)



class child(Parent):
    def __init__(self):
        print("Calling child contructor")

    def childMethod(self):
        print("Calling child method")


c = child()
c.childMethod()
c.parentMethod()
c.setAttr(1000)
c.getAttr()

