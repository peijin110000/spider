from selenium import webdriver
import urllib.request
import re,itertools
import json
'''driver = webdriver.PhantomJS(executable_path='D:\python\phantomjs\phantomjs.exe')
driver.get("http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,desc&page=1,9999&feature=|&dt=1519887987954&atfc=&onlySale=0")


imgdiv = re.findall('{.+?}',driver.page_source,re.S)	
text = json.loads(imgdiv)
print(text)
driver.quit()'''
with open('13json.json', 'r') as f:
    data = json.load(f)
    datas = data['datas']
    print(datas[0])
	