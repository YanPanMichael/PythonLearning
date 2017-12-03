import re
import sys
import os

p=re.compile(r'abc')
print type(p)
print dir(p)
m=p.match("abcdef")
print dir(m)
print m.group()

p=re.compile(".")
m1=p.match('dig')
print m1.group()

p2=re.compile("\.")
try:
    print p2.match("abc.s.").group()
except Exception, e:
    print e.message
# print m2.group()
print p2.findall('abc.s.')