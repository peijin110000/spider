from selenium import webdriver
import urllib.request
import re,itertools
import json
import pymysql
'''driver = webdriver.PhantomJS(executable_path='D:\python\phantomjs\phantomjs.exe')
driver.get("http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,desc&page=1,9999&feature=|&dt=1519887987954&atfc=&onlySale=0")


imgdiv = re.findall('{.+?}',driver.page_source,re.S)	
text = json.loads(imgdiv)
print(text)
driver.quit()'''
db = pymysql.connect("localhost","root","root","foundation",charset='utf8')
cursor = db.cursor()
with open('13json.json', 'r') as f:
    data = json.load(f)
    datas = data['datas']
    i = 1
    for val in datas:
        sql = "insert into fund_detail(fund_code,fund_name) values('" + val[0] + "','" + val[1] + "')"
        i = i + 1
        try:
            cursor.execute(sql)
            print(cursor.rowcount)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
            
    print(i)