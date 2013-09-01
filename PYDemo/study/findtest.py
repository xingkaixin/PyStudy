#coding=utf-8
import imp

from demo import fortest1

class test():
  
  def __init__(self):
    print imp.find_module("demo")
    print "init"
    fortest1()
    
    
  def abc(self,name):
    for i,c in enumerate(name):
        print "s[{0}] = {1}".format(i,c)
  
  
 
if __name__ == "__main__":
  t = test()
  t.abc("abc")