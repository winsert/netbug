import urllib
import urllib2
import json

#values ={"user":"cbond", "secret":"7f63074f"}
#values ={"secret":"7f63074f", "user":"cbond"}
#data = urllib.urlencode(values)
#data = json.dumps(values)
#print data
#url = "http://tinywebdb.appinventor.space/&user=cbond&secret=7f63074f"
#url = "http://tinywebdb.appinventor.space/login"
#url = "http://tinywebdb.appinventor.space/webdb-cbond-7f63074f"
url = "http://tinywebdb.appinventor.space/api"
#url = "http://tinywebdb.appinventor.space/"
#request = urllib2.Request(url,data)
request = urllib2.Request(url)
response = urllib2.urlopen(request)
print response.read()
