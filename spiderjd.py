from selenium import webdriver
import urllib.request
import re,itertools
url="https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.97.1fe75622P2gZOx&id=542842085300&skuId=3517794273860&areaId=440400&user_id=3024007173&cat_id=50070285&is_b=1&rn=8054c994f52fef06f166c489c7c67126"
driver = webdriver.PhantomJS(executable_path='D:\python\phantomjs\phantomjs.exe')
driver.get(url)
print(driver.page_source)


