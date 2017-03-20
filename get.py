import urllib
import urllib2

values = {}
values["username"] = ""
values["password"] = ""
data = urllib.urlencode(values)
url = "http://passport.csdn.net/"

geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
