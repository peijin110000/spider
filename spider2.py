#!/usr/bin/python
# -*- code:UTF-8 -*-
import urllib.request
import http.cookiejar
import re,itertools
cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
HEADER = {
    
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Connection": "keep-alive",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0"
}
url="http://www.nationalgeographic.com.cn/index.php?m=content&c=index&a=show&catid=596&id=4752"
req = urllib.request.Request(url,None,HEADER)
data = urllib.request.urlopen(req).read()
data = data.decode('UTF-8')
out = open('w1.txt','w')
out.write(data)
out.close()
print(data)

 
