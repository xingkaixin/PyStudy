# encoding: utf-8
 
#!/usr/bin/env python
#coding=utf-8
import urllib2
import re
import MySQLdb

#抓取函数
def fetch(sid=1,debug=False):
    urlbase = 'http://i.youku.com/u/UMjI4NTcyMDQ4/videos/'
    url = urlbase + 'order_1_view_1_page_' + str(sid) + '/'
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
  
def fetch_page():
    urlbase = 'http://i.youku.com/u/UMjI4NTcyMDQ4/videos/'
    url = urlbase + 'order_1_view_1_page_1/'
    res = urllib2.urlopen(url).read()
    abstarct = re.compile(r'<li class="last" title="最后".*?</li>',re.DOTALL).findall(res)
    print abstarct
    
    for i in range(0,len(abstarct)):
        page1 = re.compile(r'</em>\d</a>',re.DOTALL).findall(abstarct[i])
        page2 = re.compile(r'\d',re.DOTALL).findall(page1[0])
    return page2[0]

#插入数据库
def insert_db(page):
    #执行抓取函数
    vid_date = fetch(page,False)
    sql = "insert into ykgame (title,href,date) values (%s,%s,%s)"
    #插入数据，一页20条
    for i in range(0,len(vid_date)):
        param = (vid_date[i]['title'],vid_date[i]['href'],
                    vid_date[i]['date'])
        cursor.execute(sql,param)
        conn.commit()
                
if __name__ == "__main__":
    #连接数据库
    conn = MySQLdb.connect(host="localhost",user="root",
            passwd="root",db="test",charset="utf8")
    cursor = conn.cursor()
    conn.select_db('test')
    #创建表
#     sql = "CREATE TABLE IF NOT EXISTS \
#         ykgame(id int PRIMARY KEY AUTO_INCREMENT, title varchar(50), \
#         href varchar(50), date varchar(25))"        
#    cursor.execute(sql)
    #插入数据库
    for i in range(1,int(fetch_page())+1):
        print i
        insert_db(str(i))
    #关闭数据库
    cursor.close()
    conn.close()