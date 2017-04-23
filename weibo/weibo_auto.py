# -*- coding: UTF-8 -*-
#!/usr/bin/env python

__author__ = 'winsert@163.com'

#实现微博登录，(无需获取code,token）发布文字和图片 

from weibo import Client

# weibo api访问配置
APP_KEY = '3892485022'
APP_SECRET = 'f9bc5028f592d99d2433a42c05ea01f0'
REDIRECT_URL = 'https://api.weibo.com/oauth2/default.html' #非必须
USER_NAME = '13395317077'
USER_PASSWORD = 'wb142857'

#api = Client(APP_KEY, APP_SECRET, REDIRECT_URL, username=USER_NAME, password=USER_PASSWORD)

api = Client(APP_KEY, APP_SECRET, '', username=USER_NAME, password=USER_PASSWORD)

#file_pic = open('bird.jpg', 'rb')

text = "02 AUTO Send a weibo"

# update用于发布文本
api.post('statuses/update', status=text)

# upload用于发布文本和图片
#api.post('statuses/upload', status=text, pic=file_pic)
