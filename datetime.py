#!/usr/local/bin/python

import time

ticks = time.time()

print ticks

localtime =  time.localtime(time.time())

print localtime

localtime = time.asctime(time.localtime(time.time()))

print localtime
