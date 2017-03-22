# -*- coding: UTF-8 -*-

import urllib2
import cookielib

cookie = cookielib.CookieJar() #声明一个CookieJar对象实例来保存cookie

handler = urllib2.HTTPCookieProcessor(cookie) #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器

opener = urllib2.build_opener(handler) #通过handler来构建opener

response = opener.open('http://www.baidu.com')

for item in cookie:
    print 'Name = ' + item.name
    print 'Value = ' + item.value
