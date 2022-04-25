from morse import CODE
from PageMgr import *
from urandom import randint

class PageMain(PageBase):
    '''菜单页'''
    def __init__(self, name = 'MORSE'):
        super().__init__(name)
        
        self.eles['text']['name'] = [name, 60, 10, WHITE, BLUE, 4] # key:[str, x, y, color, size]

        self.eles['rect']['p1'] = [30, 150, 160, 40, GREEN] # key:[x, y, w, h, color]
        self.eles['text']['p1'] = ['Alpha Train', 40, 160, WHITE, BLUE, 2]
        
        self.eles['rect']['p2'] = [30, 210, 160, 40, GREEN] 
        self.eles['text']['p2'] = ['Random Train', 40, 220, WHITE, BLUE, 2]

        self.events['p1'] = self.toTrainAlpha
        self.events['p2'] = self.toTrainRandom
        
    def toTrainAlpha(self):
        print('toTrainAlpha')
        return 'TrainAlpha'
    
    
    def toTrainRandom(self):
        print('toTrainRandom')
        return 'TrainRandom'
        
        
    def tick(self):
        super().tick()
        
        # to Screensaver
        if self.ticks > 150:
            return 'Screensaver'
    

class PageTrainAlpha(PageBase):
    '''顺序训练页'''
    def __init__(self, mixer, name = 'TrainAlpha'):
        super().__init__(name)
        self.mixer = mixer
        self.index = 0
        self.keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' #list(CODE.keys()) # 列表形式的keys
        
        self.eles['text']['name'] = [name, 60, 20, WHITE, BLUE,2]
        self.eles['text']['code'] = [f'{self.keys[self.index]} {CODE[self.keys[self.index]]}',
                                     40, 120, WHITE, ORANGE, 4]
        
        self.eles['rect']['repeat'] = [10, 200, 100, 60, GREEN] 
        self.eles['text']['repeat'] = ['repeat', 30, 220, WHITE, BLUE,2]
        
        self.eles['rect']['next'] = [130, 200, 100, 60, GREEN] 
        self.eles['text']['next'] = ['next', 140, 220, WHITE, BLUE,2]
        
        self.events['repeat'] = self.repeat
        self.events['next'] = self.gonext
    
        
    def fresh(self):
        self.eles['text']['code'][0] = f'{self.keys[self.index]} {CODE[self.keys[self.index]]}'
        super().fresh()
        self.repeat()
        
    def repeat(self):
        self.mixer.send(self.keys[self.index])
        
    def gonext(self):
        self.index+=1
        if self.index== len(self.keys):
            self.index = 0
        self.fresh()
    
    def tick(self):
        super().tick()
        
        # to Screensaver
        if self.ticks > 150:
            return 'Screensaver'
        
    
class PageTrainRandom(PageTrainAlpha):
    '''随机训练页'''
    def __init__(self, mixer, name = 'TrainRandom'):
        super().__init__(mixer, name = name)
        
        # shuffle the keys
        keys = list(self.keys)
        self.keys=[]
        for _ in range(len(keys)):
            self.keys.append(keys.pop(randint(0, len(keys) - 1)))
        print(self.keys)
    
    
class PageScreensaver(PageBase):
    def __init__(self, name = 'Screensaver'):
        super().__init__(name)
        
        self.eles['rect']['quit'] = [0, 0, 240, 320, GREEN] 
        self.events['quit'] = self.quit
        
        
    def quit(self):
        return self.prev
        
    def setbg(self):
        # self.d.fill((randint(0,255), randint(0,255), randint(0,255)))
        self.d.Picture(0, 0, f'/pics/{randint(0, 17)}.jpg')
        
    def tick(self):
        super().tick()
        
        if self.ticks > 25:
            self.setbg()
            self.ticks = 0
    
