#coding=utf-8
import re
import urllib2



def getRSS():
  
  """
  test branch master
  aa = getRSS()
  for i in range(0,len(aa)/2):
    print str(i)+":" + aa[i]['title']
    print str(i)+":" +aa[i]['xmlUrl']
  """
  f = open("feedly.opml")
  rss = f.read()
  abstarct = re.compile(r'<outline type="rss".*?"/>',re.DOTALL).findall(rss)
  vid_list = []
  for i in range(0,len(abstarct)):
        title = re.compile(r'title="(.*?)"',re.DOTALL).findall(abstarct[i])
        xmlUrl = re.compile(r'xmlUrl="(.*?)"',re.DOTALL).findall(abstarct[i])
        vid = {
            'title' : title[0],
            'xmlUrl'  : xmlUrl[0]
        }
        vid_list.append(vid)  
  return vid_list
  
def getURL(url):
    #url = 'http://blog.asia.playstation.com/community/feeds/blogs?community=2068'
    res = urllib2.urlopen(url).read()
    item = re.compile(r'<item>.*?</item>',re.DOTALL).findall(res)
    #print item
    vid_list = []
    for i in range(0,len(item)):
        title = re.compile(r'<title>(.*?)</title>',re.DOTALL).findall(item[i])
        link = re.compile(r'<link>(.*?)</link>',re.DOTALL).findall(item[i])
        description = re.compile(r'<description>(.*?)</description>',re.DOTALL).findall(item[i])
        pubDate = re.compile(r'<pubDate>(.*?)</pubDate>',re.DOTALL).findall(item[i])
        pubDate1 = re.compile(r'<pubDate1>(.*?)</pubDate1>',re.DOTALL).findall(item[i])
#         print title[0]
#         print link[0]
#         print description[0]
#         print pubDate[0]
        vid = {
            'title' : title[0],
            'link' : link[0],
            'description' : description[0],
            'pubDate' : pubDate[0]
        }
        vid_list.append(vid)
    return vid_list

def filter_tags(htmlstr):
    re_test1=re.compile(';.*?&.*?;',re.DOTALL)
    re_test2=re.compile('!--.*?].*?--',re.DOTALL)
    re_test3=re.compile('div class=".*?"',re.DOTALL)
    re_test4=re.compile('pspan style=".*?"',re.DOTALL)
    re_test5=re.compile('&.*? style=".*?"',re.DOTALL)
    s=re_test1.sub('',htmlstr)
    s=re_test2.sub('',s)
    s=re_test3.sub('',s)
    s=re_test4.sub('',s)
    s=s.replace('&lt','')
    s=re_test5.sub('',s)
    return s

# with open("test.txt","a") as f:
#   artice = getURL("http://blog.asia.playstation.com/community/feeds/blogs?community=2068")
#   f.writelines(name + "\n")
aa  = getURL("http://blog.asia.playstation.com/community/feeds/blogs?community=2068")
print aa[0]['description']
print "123"
description =  filter_tags(aa[0]['description'])
print description
with open("test.txt","a") as f:
  f.truncate()
  f.close()
# for i in range(0,len(aa)):
#   title =  str(i)+"_title:" + aa[i]['title']
#   link =  str(i)+"_link:" +aa[i]['link']
#   description =  str(i)+"_description:" +filter_tags(aa[i]['description'])
#   pubDate = str(i)+"_pubDate:" +aa[i]['pubDate']
#   with open("test.txt","a") as f:
#     f.writelines(title + "\n")
#     f.writelines(link + "\n")
#     f.writelines(description + "\n")
#     f.writelines(pubDate + "\n")
# f.close()
