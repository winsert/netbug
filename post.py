import urllib
import urllib2

values ={"uesername":"winsert", "password":"jsl142857"}
data = urllib.urlencode(values)
url = "https://www.jisilu.cn/login/"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()
print data
