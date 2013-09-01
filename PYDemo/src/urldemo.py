import urllib2

opener = urllib2.build_opener()
f = opener.open("http://itercast.com/ask/")
print f.read()
f.close()
