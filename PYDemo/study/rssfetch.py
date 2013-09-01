#coding=utf-8
import re


def getRSS():
  f = open("feedly.opml")
  rss = f.read()
  abstarct = re.compile(r'<outline type="rss".*?"/>',re.DOTALL).findall(rss)
  print abstarct
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
  
aa = getRSS()
print len(aa)/2
print aa[0]['title']