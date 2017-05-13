#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 向安道全及其团队致敬！
# 本程序用于查询可转债、可交换债的最新成交价是否已达到预设的买入价。
# 版本：1.0

__author__ = 'Andy'

import urllib2 #urllib2是Python内部模块，无需安装。
import time #time是Python内部模块,无需安装。
from datetime import datetime

# 用于解析URL页面
def bsObjForm(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib2.Request(url=url, headers=headers)
    html = urllib2.urlopen(req).read().decode('gbk','ignore')
    #print html
    return html

#判断是否发送通知：预设价格:key_value, EB名称:EB_name, EB实时价格:EB_price
def getEBprice(key_value, EB_name, EB_price):
    if EB_price != 0:
        if EB_price <= key_value:
            msg = EB_name+u" 的计划买入价是："+str(key_value)+u"，当前最新价是："+str(EB_price)
            print msg

# 获取可转债的最新成交价格
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
            #print eb_name, dict[key], eb_price
            getEBprice(dict[key], eb_name, eb_price) #判断是否发送通知

if __name__ == '__main__':

    # 以下eb_dict数据字典用于保存可转债的交易代码和预设想买入的价格。
    # 例如：格力转债的代码：sh110030，预设的买入价格:108.00，则'sh110030':108.000。
    # 如果某只可转债还没有上市交易，或者不想查询其交易价格，则将其预设价格设为0.00，例如：永东转债：'sz128014':0，这样就不会收到此可转债的最新成交价了。
    # 请根据个人需要，自行修改以下eb_dict中的数据：
    eb_dict = {'sh110030':107.000, 'sh110031':101.50, 'sh110032':105.00, 'sh110033':108.00, 'sh110034':110.5, 'sh110035':107.5, 'sh113008':100.00, 'sh113009':109.50, 'sh113010':103.50, 'sh113011':100.00, 'sh113012':104.50, 'sz120001':100.00, 'sz123001':100.50, 'sz127003':100.50, 'sz128009':111.00, 'sz128010':111.50, 'sz128011':109.50, 'sz128012':100.00, 'sz128013':100.00, 'sz128014':0, 'sh132001':103.00, 'sh132002':103.00, 'sh132003':101.00, 'sh132004':92.00, 'sh132005':102.00, 'sh132006':102.00, 'sh132007':93.00, 'sh132008':0, 'sz150016':1.00}

    now_time = datetime.now()
    today_year = now_time.year
    today_month = now_time.month
    today_day = now_time.day
    #print today_year, today_month, today_day

    end_time = datetime(today_year, today_month, today_day, 15, 10, 10) # 设定程序每天运行的结束时间到当天的15:10:10。
    #print end_time

    while datetime.now() < end_time:
        #print datetime.now()
        print time.asctime(time.localtime(time.time())) #显示查询时间
        print u"以下可转债的最新成交价已低于计划买入价："+'\n'
        getEBinfo(eb_dict)
        time.sleep(600)  # 延时查询的秒数,600即延时我分钟查询一次。
        print

    print time.asctime(time.localtime(time.time())) #显示当前时间
    print u"今日交易时间已结束。"
