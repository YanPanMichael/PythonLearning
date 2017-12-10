#coding="utf-8"
import urllib2
import re

# req = urllib2.urlopen("http://www.baidu.com")
# print type(req)
# print dir(req)
# print req.code
# print req.read()
# print type(req.read())
# print req.headers.values()

def get_proxy_from_cnpproxy():
    try:
        p1 = re.compile(r'''"(.+?)": "http://y0.ifengimg.com/base/origin/(.+?).min"''')
        p2 = re.compile(r'''<li><a href="http://(.+?)/" target="_blank">(.+?)</a></li>''')
        target = "http://news.ifeng.com/a/20171210/54042354_0.shtml?_zbs_baidu_news#p=1"
        req = urllib2.urlopen(target)
        result = req.read()
        matchs = re.findall(p2, result)
        for item in matchs:
            print str(item)
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason

get_proxy_from_cnpproxy()
