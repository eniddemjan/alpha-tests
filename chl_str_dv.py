#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
from AlphaBot2 import AlphaBot2
from TRSensors import TRSensor
import time
import math

if __name__ == '__main__':
    TR = TRSensor()
    TR.calibrate()
    Ab=AlphaBot2()
    
    Ab.setPWMA(50)
    Ab.setPWMB(55)
    while True:
        Ab.forward()
        time.sleep(0.01)
        sval = TR.AnalogRead()
        #If the robot is directly at the border
        if(sval[4] <300 and sval[0] <300):
            Ab.stop()
            Ab.forward()
            time.sleep(1.35)
        else:
            # left sensor(0) on the black line
            if(sval[0] <300):
                while(sval[2] >300):
                    sval = TR.AnalogRead()
                    Ab.forward()
                Ab.stop()
                #Distance between the middle sensor and the sensor that is on the edge
                a= 0.25
                #Robot speed
                v=0.13
                #Distance between first and last point on the line 
                b=a*v
                #the distance between the line and the angle of incidence
                distance = math.atan(a/b)
                #t=d/v
                Time=distance/v
                #Change direction
                Ab.right()
                time.sleep(Time)
            # right sensor(4) on the black line
            elif(sval[4] <300):
                while(sval[2] >300):
                    sval = TR.AnalogRead()
                    Ab.forward()
                Ab.stop()
                #Distance between the middle sensor and the sensor that is on the edge
                a= 0.25
                #Robot speed
                v=0.13
                #Distance between first and last point on the line 
                b=a*v
                #the distance between the line and the angle of incidence
                distance = math.atan(a/b)
                #t=d/v
                Time=distance/v
                #Change direction
                Ab.left()
                time.sleep(Time)
