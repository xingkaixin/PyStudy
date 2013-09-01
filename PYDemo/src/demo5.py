import webbrowser
import time
import os

j = 0
while j<=1:
    i = 0
    while i <= 20:
        webbrowser.open('http://weibo.com/xingkaixin/profile')
        i = i +1
        time.sleep(0.5)
    else:
        time.sleep(5)
        os.system('killall -9 firefox')
j = j + 1
