

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255, 255, 255)
ORANGE =(0xFF,0x7F,0x00) #橙色
    
    
class PageBase:
    def __init__(self, name, backgroud = WHITE):
        self.name = name # 页面名
        self.prev = None # 前一页名
        self.d = None # display
        self.ticks = 0 # 调用计数标记
        self.bg = backgroud
        self.eles = { # ui元素
            'text': {
                # key:[str, x, y, color, backcolor, size],
                },
            'rect': {
                # key:[x, y, w, h, color],
                },
            }
        self.events = { # 矩形框touched事件检测，执行第一个匹配函数，暂只检测self.eles[rect]
            # rect.key:fun1,
            }
        
    def tick(self):
        self.ticks += 1
        
    def fresh(self):
        '''
        刷新屏幕    
        '''
        self.ticks = 0 # 重置计数器
        
        self.d.fill(self.bg)
        
        # drawRect
        for v in self.eles['rect'].values():
            self.d.drawRect(v[0], v[1], v[2], v[3], v[4], border=1) # [x, y, w, h, color]
            
        # printStr
        for v in self.eles['text'].values():
            self.d.printStr(v[0], v[1], v[2], v[3], backcolor = v[4], size = v[5]) # key:[str, x, y, color, backcolor, size]

          
    def touched(self, x, y):
        '''
        触摸检测
        '''
        self.ticks = 0 # 重置计数器
        
        for k in self.events:
            rect = self.eles['rect'][k]
            if x > rect[0] and x< rect[0] + rect[2] and \
                y > rect[1] and y < rect[1] + rect[3]:
                return self.events[k]()
                break
            
    
from touch import XPT2046    
from tftlcd import LCD32
class PageMgr:
    def __init__(self):
        self.d = LCD32(portrait=1) #默认竖屏
        self.t = XPT2046(portrait=1)
        self.pages = {} # 页面集合
        self.p = None # 当前页，PageBase
        
    def add(self, page:PageBase):
        page.d = self.d 
        self.pages[page.name] = page
        
        
    def touched(self, x, y):
        '''触摸事件'''
        if self.p:
            name = self.p.touched(x, y)
            if name:
                self.paging(name)
    
    
    def paging(self, name):
        '''翻页'''
        if self.pages.get(name):
            if self.p:
                self.pages[name].prev = self.p.name
            self.p = self.pages[name]
            self.p.fresh()
        else:
            print(f'no page({name}). \r\npages:{self.pages.keys()}')
        
       
    def tick(self):
        if self.p:
            name = self.p.tick()
            if name:
                self.paging(name)
        