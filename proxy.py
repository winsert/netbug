#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re, requests

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

iplist = []

html = requests.get("http://haoip.cc/tiqu.htm")

iplistn = re.findall(r'r/>(.*?)<b', html.text, re.S) #从html.text中获取所有r/><b的内容，re.S的意思是包括匹配包括换行符，findall返回的是个list

for ip in iplistn:
    i = re.sub('\n', '', ip) ##re.sub 是re模块替换的方法，这儿表示将\n替换为空
    iplist.append(i.strip()) 
    print i.strip()

print iplist
