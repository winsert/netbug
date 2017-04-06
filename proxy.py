#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re, requests, os

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

iplist = []

html = requests.get("http://haoip.cc/tiqu.htm")

iplistn = re.findall(r'r/>(.*?)<b', html.text, re.S) #从html.text中获取所有r/><b的内容，re.S的意思是包括匹配包括换行符，findall返回的是个list

if len(iplistn) == 0:
    print "没有获得新的Proxy"
else:
    os.remove('proxy.csv') #删除原有proxy.csv文件

    fp = open('proxy.csv', 'a')  #采用追加方式打开proxy.csv

    j = 0 #用于统计获得proxy地址的数量
    for ip in iplistn:
        i = re.sub('\n', '', ip) ##re.sub 是re模块替换的方法，这儿表示将\n替换为空
        iplist.append(i.strip()) 
        fp.write(i.strip())
        fp.write('\n')
        j += 1
        print j, '\t', i.strip()

print "共获得 %r 个proxy地址。" % j
fp.close()
