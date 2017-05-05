#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 本程序用于查询今日和历史上今日的天气信息,并发送到微博

__author__ = 'winsert@163.com'

import urllib2
import datetime
from bs4 import BeautifulSoup
from weibo import Client

# 用于解析URL页面
def bsObjForm(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib2.Request(url=url, headers=headers)
    html = urllib2.urlopen(req).read()
    #print html
    return html

def bsObjFormHistory(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib2.Request(url=url, headers=headers)
    html = urllib2.urlopen(req).read().decode('UTF-8','ignore')
    return html

# 获取历史上的天气信息
def getHistoryWeather(url, month_day):
    resp = bsObjFormHistory(url)
    soup = BeautifulSoup(resp, "html.parser")
    all = soup.find('div', class_="blk_02").find_all('tr')
    for tr in all:
        #print tr.get_text()
        day_list = tr.get_text().splitlines()
        #print day_list
        if month_day in day_list:
            av_high = day_list[2]
            av_low = day_list[3]
            his_high = day_list[5]
            his_low = day_list[6]
            #print u"历史上今日平均最高温度："+av_high+u"度，平均最低温度："+av_low+u"度，极端最高温度："+his_high+u"度，极端最低温度："+his_low+u"度。"
            history_weather = u"历史上今日平均最高温度："+av_high+u"度，平均最低温度："+av_low+u"度，极端最高温度："+his_high+u"度，极端最低温度："+his_low+u"度。"
    return history_weather

# 获取今日天气信息
def getTodayWeather(url):
    resp = bsObjForm(url)
    soup = BeautifulSoup(resp, "html.parser")
    city = soup.city.string
    status = soup.status1.string
    #wind_direction = soup.direction1.string
    #wind_power = soup.power1.string
    temp1 = soup.temperature1.string
    temp2 = soup.temperature2.string
    today_weather = u"城市："+city+'\n'+u"今日："+status+'\n'+u"气温："+temp1+"-"+temp2
    #print today_weather
    return today_weather

def sendWeibo(today_weather, history_weather):

    # weibo api访问配置
    APP_KEY = 'XXXX'
    APP_SECRET = 'XXXX'
    REDIRECT_URL = 'https://api.weibo.com/oauth2/default.html' #非必须
    USER_NAME = 'XXXX'
    USER_PASSWORD = 'XXXX'

    api = Client(APP_KEY, APP_SECRET, '', username=USER_NAME, password=USER_PASSWORD)

    text = today_weather+'\n'+history_weather+'\n'+u"数据来源：weather.sina.com.cn"
    print text

    # update用于发布文本
    api.post('statuses/update', status=text)
    print u"微博发送成功！"

if __name__ == '__main__':
    
    today_url = "http://php.weather.sina.com.cn/xml.php?city=%BC%C3%C4%CF&password=DJOYnieT8234jlsK&day=0"
    today_weather = getTodayWeather(today_url)

    today = datetime.date.today()
    month_day = str(today.month)+str(today.day)
    history_url = "http://php.weather.sina.com.cn/whd.php?c=1&city=%BC%C3%C4%CF&dpc=1"
    history_weather = getHistoryWeather(history_url, month_day)

    sendWeibo(today_weather, history_weather )
