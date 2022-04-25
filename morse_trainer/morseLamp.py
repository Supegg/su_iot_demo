'''
名称：morseLamp
版本：v1.0
日期：2022.4
作者：Supegg
说明：摩斯码闪灯
'''
from machine import Pin
from neopixel import NeoPixel
from morse import CODE
import time

BLUE=(0,0,255)
BLACK=(0,0,0)

class morseLamp:
    def __init__(self, pin, tdot=0.1):
        self.pin = pin
        self.tdot = tdot
        self.tdash = self.tdot * 3
        self.tspace = self.tdot * 3
        self.tword = self.tdot * 7
            
    def flash(self, led, t):
        led[0] = BLUE
        led.write()
        time.sleep(t)
        led[0] = BLACK
        led.write()

    def send(self, msg="SOS"):
        led = Pin(self.pin, Pin.OUT)
        led = NeoPixel(led, 1)
        

        led[0] = BLACK
        led.write()
        for l in msg:
            c = CODE.get(l.upper())
            for e in c:
               if e==".":
                   self.flash(led,self.tdot)
                   time.sleep(self.tdot)
               if e=="-":
                   self.flash(led, self.tdash)
                   time.sleep(self.tdot)
               if e==" ": # betwee words
                   time.sleep(self.tword)
            time.sleep(self.tspace) # between letters
        led[0] = BLACK
        led.write()
