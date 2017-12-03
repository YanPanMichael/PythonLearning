#coding=utf-8

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

p3=re.compile("[abc]*") #zero or more
p4=re.compile("[abc]+") #once or more
print p3.findall('abcdef')
print p4.findall('abcdef')

#贪婪模式是指匹配最长的字符串 'abc'
p5=re.compile("[abc]*?") #not greedy
p6=re.compile("[abc]+?") #not greedy
print p5.findall('abcdef')
print p6.findall('abcdef')

p7=re.compile("[abc]{2}") #匹配长度为2的子串
print p7.findall('abcabc')
p8=re.compile("[abc]{2,3}") #匹配长度为3的子串
print p8.findall('abcabc')
p9=re.compile("[abc]{2,3}?") #匹配长度为2的子串
print p9.findall('abcabc')

p10=re.compile("^[abc]*")
print p10.findall('bcabc')

p10=re.compile("[^abc]*?r$") # not abc string
print p10.findall('bcadfer')

p11=re.compile('(?P<mySelf>a)b(c)') # not abc string
m=p11.match('abcdef')
print m.group()
print m.groups() 
print m.groupdict()

p12=re.compile(r'(?P<mySelf>a)b(c)(?P=mySelf)\1') # not abc string
print p12.findall('abcaaa')

p13=re.compile(r'\w+(?=\d)') #之后的字符串为数字 匹配出现一次以上的单词
print p13.findall('hello1 world2 hahaha3')

p15=re.compile(r'(?<=\d)aa') #之前的字符串为数字 匹配出现一次以上的单词
print p15.findall('hello1a world2 haha3aa')

p16=re.compile(r'abc',re.I) #或略大小写
print p16.findall('aBC')

p17=re.compile(r'(\w+) (\w+)') #relpace two words positions
str1='hi petter, how age'
print p17.sub(r'\2 \1', str1)