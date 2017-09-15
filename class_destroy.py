#!/usr/local/bin/python

class Point:
    z = 20
    def __init__(self, x=4, y=10):
        self.x = x
        self.y = y
        print x, y
    def __del__(self):
        class_name = self.__class__.__name__
        var = self.__class__.z
        print class_name, "Destroyed"

pt1 = Point()
pt2 = pt1
pt3 = pt1

print id(pt1), id(pt2), id(pt3), id(Point.z) # prints the ids of the object
print Point.z

del pt1
del pt2
del pt3
del Point.z
