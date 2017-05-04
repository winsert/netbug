#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序用于获取可转债、可交换债的实时交易价格

__author__ = 'winsert@163.com'

import urllib2

# 用于解析URL页面
def bsObjForm(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib2.Request(url=url, headers=headers)
    html = urllib2.urlopen(req).read().decode('gbk','ignore')
    #print html
    return html

# 获取可转债的价格
def getEBinfo(url):
    resp = bsObjForm(url)
    temp_list = resp.split(',')
    #print temp_list
    eb_name = temp_list[0][21:25]
    eb_price = temp_list[3]
    print eb_name, eb_price

if __name__ == '__main__':

    # eb列表用于保存交易代码
    eb_code = ['sh110030', 'sh110031', 'sh110032', 'sh110033', 'sh110034', 'sh110035', 'sh113008', 'sh113009', 'sh113010', 'sh113011', 'sh113012', 'sz120001', 'sz123001', 'sz127003', 'sz128009', 'sz128010', 'sz128011', 'sz128012', 'sz128013', 'sh132001', 'sh132002', 'sh132003', 'sh132004', 'sh132005', 'sh132006', 'sh132007']

    eb_len = len(eb_code)
    for i in range(eb_len):
        #print eb[i]
        # 生成查询实时价格的URL
        url = "http://hq.sinajs.cn/list="+eb_code[i]
        #print url

        getEBinfo(url)
