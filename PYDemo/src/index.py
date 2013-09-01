import web
import sys
sys.path.append("D:\Apache2.2\htdocs")
import hello


urls = ('/index','index',
        '/','index',
        '/hi',hello.hi,
        '/hi/(.+)',hello.hi_name,
        '/error', 'redirect',
        '/author','author',
        '/test[0-9]','homepage',
        '/hello/(.+)','hello_name',
        '/hello/(.+)/(.+)','hello_name_age',
        '/example','example',
        '/ctx','ctx',
        '/proc','proc',
        '/.','notfound')

class index:
  def GET(self):
    return "hello index!"

class hello:
  def GET(self):
    return "hello hello!"

class redirect:
  def GET(self):
    web.seeother('/index')

class author:
  def GET(self):
    web.seeother('./static/author.jpg')

class homepage:
  def GET(self):
    return "hello home!"

class hello_name:
  def GET(self,name):
    return "your name is {0}".format(name)

class hello_name_age:
  def GET(self,name,age):
    return "your name is {0},age {1}".format(name,age)

class example:
  def GET(self):
    referer = web.ctx.env.get('HTTP_REFERER', './static/author.jpg')
    raise web.seeother(referer)

class ctx:
  def GET(self):
    ctx = web.ctx.env.get('HTTP_USER_AGENT')
    return ctx


class notfound:
  def get(self):
    return "NOOOOOOOOOOOOOOOO!"

app = web.application(urls, locals())
application = app.wsgifunc()
