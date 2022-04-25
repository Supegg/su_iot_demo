'''
名称：morseMixer
版本：v1.0
日期：2022.4
作者：Supegg
说明：摩斯码闪灯/蜂鸣器
'''
from machine import Pin, PWM
from neopixel import NeoPixel
from morse import CODE
import time


BLACK=(0,0,0)
ORANGE =(0xFF,0x7F,0x00) #橙色

class morseMixer:
    def __init__(self, pin0, pin1, duty=512, tdot=0.1):
        '''
        pin0 --> led灯珠
        pin1 --> buzzer
        '''
        self.pin0 = pin0
        self.pin1 = pin1
        self.duty = duty
        self.tdot = tdot
        self.tdash = self.tdot * 3
        self.tspace = self.tdot * 3
        self.tword = self.tdot * 7
            
    def flash(self, led, buzzer, t):
        led[0] = ORANGE
        led.write()
        buzzer.duty(self.duty)
        time.sleep(t)
        led[0] = BLACK
        led.write()
        buzzer.duty(0)

    def send(self, msg="SOS"):
        led = Pin(self.pin0, Pin.OUT)
        led = NeoPixel(led, 1)
        buzzer = PWM(Pin(self.pin1), freq=2349, duty=0) # 'D7':2349

        led[0] = BLACK
        led.write()
        buzzer.duty(0)
        for l in msg:
            c = CODE.get(l.upper())
            for e in c:
               if e==".":
                   self.flash(led, buzzer, self.tdot)
                   time.sleep(self.tdot)
               if e=="-":
                   self.flash(led, buzzer, self.tdash)
                   time.sleep(self.tdot)
               if e==" ": # betwee words
                   time.sleep(self.tword)
            time.sleep(self.tspace) # between letters
        led[0] = BLACK
        led.write()
        buzzer.duty(0)
