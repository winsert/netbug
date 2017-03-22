# -*- coding: UTF-8 -*-

import urllib
import urllib2
import cookielib

filename = 'imooc.txt'

cookie = cookielib.MozillaCookieJar(filename)

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

postdata = urllib.urlencode({'email':'winsert@163.com', 'password':'im142857'})

loginUrl = 'http://www.imooc.com/user/newlogin'

result = opener.open(loginUrl, postdata)

cookie.save(ignore_discard=True, ignore_expires=True)

gradeUrl = 'http://www.imooc.com/u/5074576/courses' #请求访问课程网址

result = opener.open(gradeUrl)

print result.read()
