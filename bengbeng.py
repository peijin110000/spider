from selenium import webdriver
import urllib.request
import re,itertools
url="http://www.nationalgeographic.com.cn/index.php?m=content&c=index&a=lists&catid=596"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
dl = re.findall('<dl class="show-list-dl aside-box" style="margin-bottom: 30px; height:440px;">(.+?)</dl>',data,re.S)
list = []

for li in dl:
	fz = re.findall('<a href="(.+?)"',li,re.S)
	for ls in fz:
		list.append(ls)

lists = []
for gs in list:
	if gs not in lists:
		lists.append(gs)

x=1
for im in lists:

	driver = webdriver.PhantomJS(executable_path='D:\python\phantomjs\phantomjs.exe')
	driver.get(im)
	imgdiv = re.findall('<div id="big-pic" style="margin-left:auto;margin-right:auto;width:990px">(.+?)</div>',driver.page_source,re.S)
	imgurl = re.findall('<img src="(.+?)"',imgdiv[0],re.S)
	urllib.request.urlretrieve(imgurl[0],'D:\python\img\%s.jpg' % x)
	driver.quit()
	print('已获取'+ str(x) +'张图片')
	x+=1