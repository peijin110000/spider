#!/usr/bin/python
# -*- code:UTF-8 -*-
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
for gh in lists:
	urls = gh
	imgs = urllib.request.urlopen(urls).read()
	imgs = imgs.decode('UTF-8')
	imgdiv = re.findall('<div id="big-pic" style="margin-left:auto;margin-right:auto;width:990px">(.+?)</div>',imgs,re.S)
	print(imgdiv)
 
