# -*- coding: UTF-8 -*-

import urllib2
import cookielib

cookie = cookielib.MozillaCookieJar()  #声明一个MozillaCookieJar对象实例

cookie.load ('cookie.txt', ignore_discard = True, ignore_expires = True)

req = urllib2.Request("http://www.baidu.com")

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

response = opener.open(req)

print response.read()
