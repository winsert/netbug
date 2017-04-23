# -*- coding: UTF-8 -*-
#!/usr/bin/env python

__author__ = 'winsert@163.com'

#实现微博登录，(无需获取code,token）发布文字和图片 

from weibo import Client

# weibo api访问配置
APP_KEY = 'XXXXX'
APP_SECRET = 'XXXXX'
REDIRECT_URL = 'https://api.weibo.com/oauth2/default.html' #非必须
USER_NAME = 'XXXXX'
USER_PASSWORD = 'XXXXX'

#api = Client(APP_KEY, APP_SECRET, REDIRECT_URL, username=USER_NAME, password=USER_PASSWORD)

api = Client(APP_KEY, APP_SECRET, '', username=USER_NAME, password=USER_PASSWORD)

#file_pic = open('XXXXX.jpg', 'rb')

text = "AUTO Send a weibo"

# update用于发布文本
api.post('statuses/update', status=text)

# upload用于发布文本和图片
#api.post('statuses/upload', status=text, pic=file_pic)
