from selenium import webdriver
import urllib.request
import re,itertools
driver = webdriver.PhantomJS(executable_path='D:\python\phantomjs\phantomjs.exe')
driver.get("http://fund.eastmoney.com/fund.html")

imgdiv = re.findall('<table align="center" class="dbtable" id="oTable">.+?</table>',driver.page_source,re.S)	
print(imgdiv)
f= open('test.txt','w')
f.write(driver.page_source)
f.close()
f = open('11.txt','w')
f.write(imgdiv[0])
f.close()
fundcode = re.findall('<td class="">.+?</td>',imgdiv[0],re.S)
f = open('12.txt','w')
f.write(imgdiv[0])
f.close()
driver.quit()
	