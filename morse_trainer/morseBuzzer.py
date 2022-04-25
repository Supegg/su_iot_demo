'''
名称：morseSpeaker
版本：v1.0
日期：2022.4
作者：Supegg
说明：摩斯码蜂鸣器
'''
from machine import Pin, PWM
from morse import CODE
import time

class morseBuzzer:
    def __init__(self, pin, duty=512, tdot=0.1):
        self.pin = pin
        self.duty = duty
        self.tdot = tdot
        self.tdash = self.tdot * 3
        self.tspace = self.tdot * 3
        self.tword = self.tdot * 7
            
    def beep(self, buzzer, t):
        buzzer.duty(self.duty)
        time.sleep(t)
        buzzer.duty(0)

    def send(self, msg="SOS"):
        buzzer = PWM(Pin(self.pin), freq=2349, duty=0) # 'D7':2349

        buzzer.duty(0)
        for l in msg:
            c = CODE.get(l.upper())
            for e in c:
               if e==".":
                   self.beep(buzzer,self.tdot)
                   time.sleep(self.tdot)
               if e=="-":
                   self.beep(buzzer, self.tdash)
                   time.sleep(self.tdot)
               if e==" ": # betwee words
                   time.sleep(self.tword)
            time.sleep(self.tspace) # between letters
        buzzer.duty(0)
