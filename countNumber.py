#!/usr/bin/python
#coding:utf-8

import re

fp = file("test.txt", "r")
count = 0
for s in fp.readlines():
    li = re.findall("hello", s)
    if len(li) > 0:
        count = count + len(li)

print "Search "+ str(count) +" hello"
fp.close()