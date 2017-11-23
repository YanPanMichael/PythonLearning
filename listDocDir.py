#!/usr/bin/python
#coding:utf-8

import os

def dirList(path):
    filelist = os.listdir(path)
    fpath = os.getcwd()
    allfile = []
    for filename in filelist:
        # allfile.append(fpath+filename)
        filepath = os.path.join(fpath,filename)
        if os.path.isdir(filepath):
            dirList(filepath)
        allfile.append(filepath)
    return allfile

def dirList2(path):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path,filename)
        if os.path.isdir(filepath):
            dirList2(filepath)
        print filepath

def dirList3():
    walkObj = os.walk('/Users/michael/Documents/pythonLearning')
    for path,d,filelist in walkObj:
        for filename in filelist:
            print os.path.join(path,filename)
    

# print allfile
# allfile = dirList2('/Users/michael/Documents/pythonLearning')
dirList3()