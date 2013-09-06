#coding=utf-8
import re
import urllib2



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
    re_cdata=re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I) #匹配CDATA
    re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)#Script
    re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)#style
    re_p=re.compile('<P\s*?/?>')#处理换行
    re_h=re.compile('</?\w+[^>]*>')#HTML标签
    re_comment=re.compile('<!--[^>]*-->')#HTML注释
    s=re_cdata.sub('',htmlstr)#去掉CDATA
    s=re_script.sub('',s) #去掉SCRIPT
    s=re_style.sub('',s)#去掉style
    s=re_p.sub('\r\n',s)#将<p>转换为换行
    s=re_h.sub('',s) #去掉HTML 标签
    s=re_comment.sub('',s)#去掉HTML注释  
    blank_line=re.compile('\n+')#去掉多余的空行
    s=blank_line.sub('\n',s)
    return s


# with open("test.txt","a") as f:
#   artice = getURL("http://blog.asia.playstation.com/community/feeds/blogs?community=2068")
#   f.writelines(name + "\n")
aa  = getURL("http://blog.asia.playstation.com/community/feeds/blogs?community=2068")
for i in range(0,len(aa)):
  title =  str(i)+"_title:" + aa[i]['title']
  link =  str(i)+"_link:" +aa[i]['link']
  description =  str(i)+"_description:" +filter_tags(aa[i]['description'])
  pubDate = str(i)+"_pubDate:" +aa[i]['pubDate']
  with open("test.txt","a") as f:
    f.writelines(title + "\n")
    f.writelines(link + "\n")
    f.writelines(description + "\n")
    f.writelines(pubDate + "\n")
