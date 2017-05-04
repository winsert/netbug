#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序用于查询可转债、可交换债的最新价是否已达到进货价，并通过微信发送通知。

__author__ = 'winsert@163.com'

import urllib2
import itchat

# 用于解析URL页面
def bsObjForm(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib2.Request(url=url, headers=headers)
    html = urllib2.urlopen(req).read().decode('gbk','ignore')
    #print html
    return html

#判断是否发送通知：预设价格:key_value, EB名称:EB_name, EB实时价格:EB_price
def getEBprice(key_value, EB_name, EB_price):
    if EB_price <= key_value:
        msg = EB_name+u"的进货价是："+str(key_value)+u"，最新价是："+str(EB_price)
        #print msg
        itchat.auto_login(hotReload=True)
        itchat.send(msg, toUserName='filehelper')

# 获取可转债的价格
def getEBinfo(dict):

    for key in dict.keys():
        #print key
        if dict[key] != 0: #dict[key]:EB预设价格
            url = "http://hq.sinajs.cn/list="+key #生成用于查询的URL
            #print url
            resp = bsObjForm(url)
            temp_list = resp.split(',')
            #print temp_list
            eb_name = temp_list[0][21:25] #获取EB名称
            eb_price = float(temp_list[3]) #获取EB实时价格
            #print "名称：%r，进货价：%r，最新成交价：%r。" %(eb_name, dict[key], eb_price)
            #print eb_name, dict[key], eb_price
            getEBprice(dict[key], eb_name, eb_price) #判断是否发送通知

if __name__ == '__main__':

    # eb列表用于保存交易代码
    eb_dict = {'sh110030':108.000, 'sh110031':101.50, 'sh110032':106.00, 'sh110033':108.00, 'sh110034':110.5, 'sh110035':107.5, 'sh113008':0, 'sh113009':109.50, 'sh113010':104.50, 'sh113011':100.00, 'sh113012':104.50, 'sz120001':107.00, 'sz123001':100.50, 'sz127003':100.50, 'sz128009':111.00, 'sz128010':111.50, 'sz128011':109.50, 'sz128012':101.00, 'sz128013':100.00, 'sz128014':0, 'sh132001':103.00, 'sh132002':103.00, 'sh132003':101.50, 'sh132004':92.00, 'sh132005':102.20, 'sh132006':104.50, 'sh132007':94.00, 'sh132008':0, 'sz150016':1.00}

    getEBinfo(eb_dict)
