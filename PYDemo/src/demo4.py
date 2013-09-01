class Monk:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def net(self):
        print 'I love weibo'
    
    def play(self,str1):
        print "play with",str1

m1 = Monk("yancan",18)
print (m1.name)
m1.net()
m1.play('monkey')