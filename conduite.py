# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 18:06:59 2018
@author: SIMPLYCASH
"""

import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()


#‘Forward’=Ven1.C1.D1.Ven2.C2.D2
#‘Reverse’=Ven1.C1.D1.Ven2.C2.D2
#‘Left’=Ven1.(C1=D1).Ven2.C2.D2
#‘Right’=Ven1.C1.D1.Ven2.(C2=D2)
#‘Stop’=Ven1.(C1=D1).Ven2.C2=D2)


#Ven1=12
#Ven2=6
#C1=16
#D1=19
#C2=20
#D2=26

pin=(11,12,15,16,31,32)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

Frwd=(1,1,0,1,1,0)
Rvrs=(1,0,1,1,0,1)
Lft=(0,0,0,1,1,0)
Rgt=(1,1,0,0,0,0)
Stp=(1,0,0,1,0,0)
Free=(0,0,0,0,0,0)

def forward(x):
    GPIO.output(pin,Frwd)
    time.sleep(x)
    GPIO.output(pin,Free)
    
def reverse(x):
    GPIO.output(pin,Rvrs)
    time.sleep(x)
    GPIO.output(pin,Free)
    
def left(x):
    GPIO.output(pin,Lft)
    time.sleep(x)
    GPIO.output(pin,Free)
def right(x):
    GPIO.output(pin,Rgt)    
    time.sleep(x)
    GPIO.output(pin,Free)
    
def stop(x):
    GPIO.output(pin,Stp)
    time.sleep(x)
    GPIO.output(pin,Free)


while (1):

    forward(5)

    reverse(5)
GPIO.cleanup()
