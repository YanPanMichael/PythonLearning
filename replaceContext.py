#!/usr/bin/python
#coding:utf-8

fp1 = file("test.txt","r")
fp2 = file("targetTest.txt","w")
for s in fp1.readlines():
    fp2.write(s.replace("hello","hahaha"))

fp1.close()
fp2.close()