#!/usr/bin/python3.6


def fun(a,b,c):
    print(a,b,c)

list = [1,2,3]

fun(*list)

def num(*args):
    for i in range(0,len(args)):
        print(args[i])

num(1,2,3)
num(23,43)


def fun2(a,b,c):
    print(a,b,c)

d = {'a':2, 'b': 4, 'c': 6}

fun2(**d)

def fun3(**kwargs):
    print(type(kwargs))

    for key in kwargs:
        print("%s = %s" % (key,kwargs[key]))

fun3(name="geeks", ID="101", language="Python")