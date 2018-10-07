from selenium import webdriver
import urllib.request
import re,itertools
import os
url="https://www.woyaogexing.com/touxiang/katong/"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
dl = re.findall('<div class="txList ">(.+?)</div>',data,re.S)
list = []
allheadurl = []
allheads = []
#print(dl)

for li in dl:
	fz = re.findall('<a href="(.+?)">',li,re.S)
	for ls in fz:
		list.append(ls)
pattern = re.compile('2018/(.+?).html')
result1 = pattern.findall(list[0])
for lz in list:
    pattern = re.compile('2018/(.+?).html')
    result1 = pattern.findall(lz)
    allheadurl.append(result1)
for lh in allheadurl:
    if lh:
        str = 'https://www.woyaogexing.com//touxiang/katong/2018/'+lh[0]+'.html'
        if str not in allheads:
            allheads.append(str)
#print(allheads)
x=1
for im in allheads:
    print(im)
    data = urllib.request.urlopen(im).read()
    data = data.decode('UTF-8')
    imgdiv = re.findall('<li class="tx-img">(.+?)</li>',data,re.S)
    for hm in imgdiv:
        imgurl = re.findall('<img class="lazy" src="(.+?)"',hm,re.S)
        urllib.request.urlretrieve('https:'+imgurl[0],'D:\python\img\lottery%s.jpg' % x)
        print('已获取%s张图片' % x)
        x+=1
        if(x==101):
            os._exit()
        
