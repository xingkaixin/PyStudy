# -*- encoding: utf-8 -*-  
from M2Crypto.EVP import Cipher  
#from M2Crypto import m2  
 
iv = '\0' * 16   #任意设置  
passKey = "53336997883550638292882666861798" 
text = "K]j;skWKKCa;k[w<ibt;zddK?s?" 
 
def encrypt(buf):  
    #ecb 模式不受iv影响  
    cipher = Cipher(alg='aes_128_ecb', key=passKey, iv=iv, op=1) # 1 is encrypt  
    # padding 有时设置为1  
    cipher.set_padding(1)  
    v = cipher.update(buf)  
    v = v + cipher.final()  
    del cipher  #需要删除  
 
    out = ""  
    for i in v:  
        out += "%02X" % (ord(i))  
    print out  
    return v  
#
def decrypt(buf):  
    cipher = Cipher(alg='aes_128_ecb', key=passKey, iv=iv, op=0) # 0 is decrypt  
    cipher.set_padding(1)  
    v = cipher.update(buf)  
    v = v + cipher.final()  
    del cipher  #需要删除  
    print v 
    return v  


decrypt(encrypt(text))
