#coding=utf-8
import re


def getRSS():
  """
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
    url = 'http://i.youku.com/u/UMjI4NTcyMDQ4/videos/'
    res = urllib2.urlopen(url).read()
    abstarct = re.compile(r'<ul class="v".*?</ul>',re.DOTALL).findall(res)
    
    vid_list = []
    for i in range(0,len(abstarct)):
        title = re.compile(r'title="(.*?)"',re.DOTALL).findall(abstarct[i])
        href = re.compile(r'href="(.*?)"',re.DOTALL).findall(abstarct[i])
        date = re.compile(r'<span>(.*?)</span>',re.DOTALL).findall(abstarct[i])
        if debug == True:
            print title[0]+href[0]+date[0]
        vid = {
            'title' : title[0],
            'href'  : href[0],
            'date'  : date[0]
        }
        vid_list.append(vid)  
    return vid_list