import urllib
import urllib2

url = ""
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
values = {'username':'', 'password':''}
headers = {'User-Agent':user_agent}
data = urlilib.urlencode(values)
reques = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()
