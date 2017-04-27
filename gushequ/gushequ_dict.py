#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'winsert@163.com'

import requests
from bs4 import BeautifulSoup
 
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

url = 'http://www.gushequ.com' # 访问网址

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}  #浏览器请求头

content = requests.get(url, headers = headers) #使用requests中的get方法来获取url

## 获取总页数
pages = BeautifulSoup(content.text, 'lxml').find_all('a', class_='page-numbers') #获取总页数
#print pages[-2]
page = pages[-2].get_text()
print "共有 %r 页。" % int(page)

gsq_dic = {} #创建一个保存解析结果的字典

## 分页提取内容
for i in range(1, int(page)+1):
#for i in range(1, 2): # 测试提取第一页的数据
    page_url = 'http://www.gushequ.com/page/'+str(i)
    print '正在解析:', page_url
    page_content = requests.get(page_url, headers = headers) #requests每一个页面
    page_soup = BeautifulSoup(page_content.text, 'lxml').find('div', id='primary').find_all('a', rel='bookmark') # 解析每一个页面

    for j in page_soup: # 从每个页面中解析出title和href
        #print j['title']
        gsq_key = j['title']
        #print j['href']
        gsq_value = j['href']
        #print '\n'
        gsq_dic[gsq_key] = gsq_value

#print gsq_dic # 打印字典内容

print "共解析出 %r 条纪录" % len(gsq_dic)

# 将字典写入txt文件
df = open('gushequ_dict.txt', 'w') # 打开文件
df.write(str(gsq_dic).strip())
df.close()
print "已将解析结果写入gushequ_dic.txt"
