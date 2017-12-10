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
    parten = re.compile(r'''<script src="https://(.+?).bdstatic.com/5aV1bjqh_Q23odCf/static/(.+?)/js/(.+?).js"></script>''')
    target = "http://www.baidu.com"
    req = urllib2.urlopen(target)
    result = req.read()
    print result
    matchs = parten.findall(result)
    print matchs

get_proxy_from_cnpproxy()
