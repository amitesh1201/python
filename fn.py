#!/bin/bash

def print_two(*args):
   arg1,arg2 = args
   print "arg1: %r,arg2: %r" % (arg1, arg2)

print_two ("A","B")

def print_two_again(arg1,arg2):
   print "arg1: %r, arg2: %r" %(arg1, arg2)

print_two_again("C","D")

def print_one(arg1):
   print "one: %r" %arg1

print_one(1)

def print_none():
   print "no arg"

print_none()
