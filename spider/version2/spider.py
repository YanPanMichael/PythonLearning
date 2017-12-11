#coding:"utf-8"

import urllib2
import re
import threading
import time

# req = urllib2.urlopen("http://www.baidu.com")
# print type(req)
# print dir(req)
# print req.code
# print req.read()
# print type(req.read())
# print req.headers.values()
proxyList=[]

def get_proxy_from_cnpproxy():
    global proxyList
    try:
        p1 = re.compile(r'''"(.+?)": "http://y0.ifengimg.com/base/origin/(.+?).min"''')
        p2 = re.compile(r'''<li><a href="http://(.+?)/" target="_blank">(.+?)</a></li>''')
        target = "http://news.ifeng.com/a/20171210/54042354_0.shtml?_zbs_baidu_news#p=1"
        req = urllib2.urlopen(target)
        result = req.read()
        matchs = re.findall(p2, result)
        for item in matchs:
            addr = item[0]
            content = item[1].decode('utf-8', 'ignore').encode('utf-8')
            l=[addr,content]
            proxyList.append(": ".join(l))
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason

class ProxyCheck(threading.Thread):
    def __init__(self, proxyList, fname):
        threading.Thread.__init__(self)
        self.proxyList = proxyList
        self.timeout = 5
        self.test_url = "https://www.baidu.com/"
        self.test_str = "11000002000001"
        self.checkedProxyList = []
        self.fname = fname

    def checkProxy(self):
        cookies = urllib2.HTTPCookieProcessor()
        for proxy in self.proxyList:
            proxy_handler = urllib2.ProxyHandler({'http' : "http://%s:%s" %(proxy[0],proxy[1])})
            opener = urllib2.build_opener(cookies.proxy_handler)
            opener.addheaders = [('User-agent','Mozlia/5.0')]
            urllib2.install_opener(opener)
            t1=time.time()
            try:
                req = urllib2.urlopen(self.test_url, timeout=self.timeout)
                result = req.read()
                timeused = time.time() - t1
                pos = result.find(self.test_str)
                if pos > -1:
                    self.checkedProxyList.append([proxy[0], proxy[1], proxy[2], proxy[3],timeused])
                else:
                    continue
            except Exception, e:
                print e.message
                continue

    def sort(self):
        sorted(self.checkedProxyList, cmp=lambda x,y:cmp(x[4],y[4]))

    def save(self):
        f = open(self.fname, 'w+')
        for proxy in self.checkedProxyList:
            print proxy
            f.write("%s:%s\t%s\t%s\t%s\n" %(proxy[0], proxy[1], proxy[2], proxy[3],str(proxy[4])))
        f.close()

    def run(self):
        self.checkProxy()
        self.sort()
        self.save()

if __name__=="__main__":
    get_proxy_from_cnpproxy()
    t1 = ProxyCheck(proxyList, "target.txt")
    t1.start()
