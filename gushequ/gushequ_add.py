#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#向gushequ_dict.json追加内容

__author__ = 'winsert@163.com'

import requests, json
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
print "当前gushequ.com共有 %r 页。" % int(page)

#导入gushequ_dict.json
gj = open('gushequ.json', 'r')
gj_dic = json.loads(gj.read())
gj.close()
old_len = len(gj_dic)

## 分页提取内容
#for i in range(1, int(page)+1):
for i in range(1, 2): # 测试提取第一页的数据
    page_url = 'http://www.gushequ.com/page/'+str(i)
    print '正在解析:', page_url, '\n'
    page_content = requests.get(page_url, headers = headers) #requests每一个页面
    page_soup = BeautifulSoup(page_content.text, 'lxml').find('div', id='primary').find_all('a', rel='bookmark') # 解析每一个页面

    for j in page_soup: # 从每个页面中解析出title和href
        new_key = j['title']
        if new_key not in gj_dic:
            print '新增加：', new_key, '\n'
            new_value = j['href']
            gj_dic[new_key] = new_value
        else:
            break

print "本次共新增 %r 条记录。" % int(len(gj_dic)-old_len)

# 将字典写入json文件
df = open('gushequ.json', 'w') # 打开文件
df.write(json.dumps(gj_dic))
df.close()
print "已将解析结果写入gushequ.json"
