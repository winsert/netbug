import urllib
import urllib2

values ={"uesername":"", "password":""}
data = urllib.urlencode(values)
print data
url = "https://passport.csdn.net/"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()
