# netbug：用于学习网络爬虫

cookie_load.py      学习使用cookie_load('cookie.txt')

cookie.py
学习使用cookie = cookielib.MozillaCookieJar(filename),
handler = urllib2.HTTPCookieProcessor(cookie) #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
opener = urllib2.build_opener(handler) #通过handler来构建opener

cookie.txt          保存cookie

demo.py             学习response.read()，type(response)

download.py         
学习request模块+Proxy,timeout,num_retries
须与mzitu.py一起在/pic目录下使用

get.py              学习urllib.urlencode生成data，然后尝试get、post访问

head.py             学习使用headers

imooc.py    imooc.txt
学习使用urllib,urllib2,cookielib访问www.imooc.com，cookie保存在cookie.txt

mydownload.py       学习requests,re组合访问

post.py             学习urllib.urlencode生成data，然后尝试post访

proxy.py    proxy.csv
从http://haoip.cc/tiqu.htm获取proxy列表，并保存到proxy.csv

proxy_list.py       读取proxy.csv，生成list

proxy.py.bak        将获取的proxy保存在list中

quishi.py           爬取糗事百科www.qiushibaike.com

re.py               学习re模块做正则式解析

try.py              学习用try排队错误

repuest.py  soup.txt
将requests后的url再BeautifulSoup，并保存到soup.txt

soup.py             用于对request.py生成的soup.txt进行解析,find

m.py                临时修改文件

