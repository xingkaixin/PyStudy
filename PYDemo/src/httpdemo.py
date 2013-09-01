import httplib


http = httplib.HTTPConnection('itercast.com',80)
http.request('GET','/ask')
print http.getresponse().read()

http.close()
