# -*- coding: UTF-8 -*-
#!/usr/bin/env python

__author__ = 'winsert@163.com'

#access to SinaWeibo By sinaweibopy 
#实现微博发文字和图片

from weibo import APIClient 
#import webbrowser

# weibo api访问配置
APP_KEY = 'XXXX'
MY_APP_SECRET = 'XXXX'
REDIRECT_URL = 'https://api.weibo.com/oauth2/default.html'

api = APIClient(app_key=APP_KEY,app_secret=MY_APP_SECRET,redirect_uri=REDIRECT_URL)
authorize_url = api.get_authorize_url()
print authorize_url
#webbrowser.open_new(authorize_url)

code = raw_input("打开URL,输入code: ").strip()

request = api.request_access_token(code, REDIRECT_URL)
access_token = request.access_token #access_token就是获得的token
expires_in = request.expires_in #expires_in是授权的过期时间 （UNIX时间）
api.set_access_token(access_token, expires_in) #用set_access_token保存授权

# 发布文本和图片
f = open('bird.jpg', 'rb')
r = api.statuses.upload.post(status=u'Test weibo with picture', pic=f)
f.close()

# 只发布文本:
#r = api.statuses.update.post(status=u'Test weibo with text')

print "微博已完成发布。"
