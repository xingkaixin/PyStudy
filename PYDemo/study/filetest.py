#coding=gbk


class fileoper():
  def writefile(self,name):
    with open("test.txt","a") as f:
      #print isinstance(f, file)
      f.writelines(name + "\n")
    
    
  def openfile(self):
      fileconn = open("test.txt","r").read()
      print fileconn
    
    
f = fileoper()
for i in range(1,10):
  f.writefile("上海，你好，今天是第{0}天".encode("gbk").format(i))
#f.openfile()