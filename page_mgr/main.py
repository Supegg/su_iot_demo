import time
from PageMgr import *

class MyPage(PageBase):
    def __init__(self, name):
        super().__init__(name)
        
        self.eles['rect']['r0'] = [5, 45, 105, 40, GREEN] # key:[x, y, w, h, color]
        
        self.eles['text']['hi'] = ['Hello world', 0, 0, WHITE, GREEN,1] # key:[str, x, y, color, size]
        self.eles['text']['btn'] = ['Button', 10, 50, RED, BLUE, 3] # key:[str, x, y, color, size]
        
        self.events['r0'] = self.fun1
        
    def fun1(self):
        print(f'call MyPage({self.name})')
        self.fresh()
        

# 初始化页面管理
mgr = PageMgr()

page = MyPage('hi')
mgr.add(page)

mgr.paging(page.name) # 指定页面


d0 = [0]
while True:
    data = mgr.t.read() #获取触摸屏坐标
    if data[0] == d0[0]:
        continue
    d0=data
    print(data) 
    
    #当产生触摸时
    mgr.touched(data[1], data[2])
    if data[0]!=2: #0：按下； 1：移动； 2：松开

        #触摸坐标画圆
        mgr.d.drawCircle(data[1], data[2], 5, BLACK, fillcolor=BLACK)
        mgr.d.printStr('(X:'+str('%03d'%data[1])+' Y:'+str('%03d'%data[2])+')',10,10,RED,size=1)

    time.sleep_ms(200) #触摸响应间隔        