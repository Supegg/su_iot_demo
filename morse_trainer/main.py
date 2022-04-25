'''
名称：摩斯码训练器
版本：v1.0
日期：2022.4
作者：Supegg
说明：摩斯码声光识别训练
1. 顺序字符训练
2. 随机字符训练
3. 字符串训练
4. 字符识别竞赛
5. 字符串识别竞赛
'''
from morseLamp import morseLamp
from morseBuzzer import morseBuzzer
from morseMixer import morseMixer
from morse import CODE
from PageMgr import *
from pages import *
import time

# lamp = morseLamp(3, tdot = 0.2)  # 3 led灯珠
# buzzer = morseBuzzer(4, tdot = 0.2) # 4 buzzer
mixer = morseMixer(3, 4, tdot=0.2)

# lamp.send()
# buzzer.send()
# mixer.send()


# 初始化页面管理
mgr = PageMgr()

mgr.add(PageMain())
mgr.add(PageTrainAlpha(mixer))
mgr.add(PageTrainRandom(mixer))
mgr.add(PageScreensaver())


mgr.paging('MORSE') # 指定页面
mixer.send()

d0 = [0]
while True:
    time.sleep_ms(200) #触摸响应间隔  
    mgr.tick()
    data = mgr.t.read() #获取触摸屏坐标
    if data[0] == d0[0]:
        continue
    d0=data
    print(data) 
    
    #当产生触摸时
    if data[0]!=2: #0：按下； 1：移动； 2：松开
        mgr.touched(data[1], data[2])

        #触摸坐标画圆
        mgr.d.drawCircle(data[1], data[2], 5, BLACK, fillcolor=BLACK)
        # mgr.d.printStr('(X:'+str('%03d'%data[1])+' Y:'+str('%03d'%data[2])+')',10,10,RED,size=1)
    
          
