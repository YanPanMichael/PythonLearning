#!/usr/bin/python
#coding:utf-8

import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html  = page.read()
    return html

def getImg(html):
    reg = r'\<img.*?src="(.*?\.jpg)"\>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' % x)
        x+=1

html = getHtml("https://tieba.baidu.com/p/5429187548")
print getImg(html)