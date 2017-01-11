# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import math

#設定GPIO相關設定
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT) 
GPIO.setup(13,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)  
GPIO.setup(19,GPIO.OUT)  
GPIO.setup(21,GPIO.OUT)  
GPIO.setup(22,GPIO.OUT)

#不明究理的地方
#主要參考http://www.cnblogs.com/ttssrs/p/4890635.html
#方向的輸出高低電壓可能還要在做修改

#重設所有腳位電位
GPIO.output(11,GPIO.LOW)
GPIO.output(12,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
GPIO.output(16,GPIO.LOW)
GPIO.output(18,GPIO.LOW)  
GPIO.output(19,GPIO.LOW)
GPIO.output(21,GPIO.LOW)  
GPIO.output(22,GPIO.LOW)

#設定所有馬達的轉動方向
class MotorController:
    def __init__(self, direction):
        if direction == 'F':
            GPIO.output(11,GPIO.HIGH)
            GPIO.output(12,GPIO.LOW)
            GPIO.output(13,GPIO.HIGH)
            GPIO.output(16,GPIO.LOW)
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(19,GPIO.LOW)     
            GPIO.output(21,GPIO.LOW)
            GPIO.output(22,GPIO.HIGH)
        if direction == 'L':
            GPIO.output(11,GPIO.LOW)
            GPIO.output(12,GPIO.HIGH)
            GPIO.output(13,GPIO.LOW)
            GPIO.output(16,GPIO.HIGH)
            GPIO.output(18,GPIO.HIGH)  
            GPIO.output(19,GPIO.LOW)  
            GPIO.output(21,GPIO.LOW)  
            GPIO.output(22,GPIO.HIGH) 
        if direction == 'R':
            GPIO.output(11,GPIO.HIGH)
            GPIO.output(12,GPIO.LOW)
            GPIO.output(13,GPIO.HIGH)
            GPIO.output(16,GPIO.LOW)
            GPIO.output(18,GPIO.LOW)  
            GPIO.output(19,GPIO.HIGH)  
            GPIO.output(21,GPIO.HIGH)  
            GPIO.output(22,GPIO.LOW) 
        if direction == 'B':
            GPIO.output(11,GPIO.LOW)
            GPIO.output(12,GPIO.HIGH)
            GPIO.output(13,GPIO.LOW)
            GPIO.output(16,GPIO.HIGH)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(19,GPIO.HIGH)     
            GPIO.output(21,GPIO.HIGH)
            GPIO.output(22,GPIO.LOW) 
        if direction == 'S':
            GPIO.output(11,GPIO.LOW)
            GPIO.output(12,GPIO.LOW)
            GPIO.output(13,GPIO.LOW)
            GPIO.output(16,GPIO.LOW)
            GPIO.output(18,GPIO.LOW)  
            GPIO.output(19,GPIO.LOW)  
            GPIO.output(21,GPIO.LOW)  
            GPIO.output(22,GPIO.LOW)
