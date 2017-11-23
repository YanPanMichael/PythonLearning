#!/usr/bin/python
#coding:utf-8

fp1 = file("targetTest.txt","r+")
s = fp1.read()
fp1.seek(0,0)
fp1.write(s.replace("hahaha","hello"))
fp1.close()