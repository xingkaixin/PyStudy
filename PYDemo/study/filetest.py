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
  f.writefile("�Ϻ�����ã������ǵ�{0}��".encode("gbk").format(i))
#f.openfile()