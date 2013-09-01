#coding=utf-8
#from itertools import  combinations
import itertools

class PrisonException(Exception):
    pass


class Data(object):
    def __init__(self):
        self._data = []
    
    def add(self,x):
        self._data.append(x)
        
    def data(self):
        return iter(self._data)

def fortest1():
    for i in xrange(3):
        print "世界末日,第{0}天" .format(i)
        
def fortest2(name):
    for i,c in enumerate(name):
        print "s[{0}] = {1}".format(i,c)

def while1():
    try:
        while True:
            while True:
                raise PrisonException()
    except PrisonException:
        print "Prison OK"

def if1():
    if 1 == 0:
        print "True"
    else:
        print "False"
        
def input1():
    input("abc")

if __name__ == "__main__":
    fortest1()
    print "\n"
    fortest2("ab")
    print "\n"
    while1()
    print "\n"
    if1()
    d = Data()
    d.add(1)
    d.add(2)
    d.add(3)
    for x in d.data():
        print x
    d.add(4)
    for x in d.data():
        print x
    it = itertools.combinations("abcd",2)
    print list(it)
    it = itertools.combinations_with_replacement("abcd",2)
    print list(it)
    it = itertools.chain(xrange(3),"abc")
    print list(it)
    
    for x in itertools.count(10,step = 10):
        print x
        if x >1000:break
    for i,x in enumerate(itertools.cycle("a")):
      print x
      if i > 7:break
    print __file__
    print __name__
    
    
    
    