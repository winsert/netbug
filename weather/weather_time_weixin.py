#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序每10分钟从济南市气象台获取一次“植物园”观测点的气象信息，并发布到微信平台。

__author__ = 'Andy'

import requests, lxml
from bs4 import BeautifulSoup
import time
from datetime import datetime
import itchat

# 解析页面:
def getSoup(url):

    soup_url = url 

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'}

    content = requests.get(soup_url, headers=headers) 

    soup = BeautifulSoup(content.text, 'lxml')

    return soup

# 获取天气实况:
def getWeather():

    weather_url = "http://jnqx.jinan.gov.cn/jnszfqxj/front/zdz/list.do?type=1"

    soup = getSoup(weather_url)
    result = soup.find('div', align="center").find_all('td')

    wlist = []
    for w in result:
        wlist.append(w.get_text())

    #print wlist[18]

    weather_msg = u'地点：'+wlist[16].strip().strip('\n').strip('\t').strip('\r')+u'\n时间：'+wlist[17]+u'\n温度：'+wlist[18].strip()+u'℃'+u'\n湿度：'+wlist[19].strip()+u'％'+u'\n风向：'+wlist[20]+u'\n风速：'+wlist[21].strip()+u'm/s'+u'\n雨量：'+wlist[22].strip()+u'mm/h'+u'\n气压：'+wlist[23].strip()+u'hPa'+'\n'

    return weather_msg

# 获取PM2.5数据：
def getPM25():

    PM_url = 'http://www.pm25.com/jinan.html'
    soup = getSoup(PM_url)
    #city = soup.find(class_='bi_loaction_city')  # 城市名称
    aqi = soup.find("a", {"class", "bi_aqiarea_num"})  # AQI指数
    quality = soup.select(".bi_aqiarea_right span")  # 空气质量等级
    result = soup.find("div", class_='bi_aqiarea_bottom')  # 空气质量描述

    PM25_msg = u'AQI指数：' + aqi.text + u'\n空气质量：' + quality[0].text + result.text

    return PM25_msg

if __name__ == '__main__':

    itchat.auto_login(enableCmdQR=2) # 通过二维码登录微信
    #itchat.auto_login(hotReload=True)

    now_time = datetime.now()
    today_year = now_time.year
    today_month = now_time.month
    today_day = now_time.day
    #print today_year, today_month, today_day

    end_time = datetime(today_year, today_month, today_day, 23, 10, 10) # 设定程序每天运行的结束时间。
    #print end_time

    while datetime.now() < end_time:
        print time.ctime() #显示当前时间
        print u"\n查询此刻天气实况："
        weather = getWeather()
        print weather
        itchat.send(weather, 'filehelper')
        print u"查询此刻PM2.5数据："
        PM25 = getPM25()
        print PM25
        itchat.send(PM25, 'filehelper')
        time.sleep(1200)  # 延时查询的秒数,600即延时我分钟查询一次。
        print

    print time.ctime() #显示当前时间
    end_msg =  u"今日查询结束。"
    print end_msg
    itchat.send(end_msg, 'filehelper')
