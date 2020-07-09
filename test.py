import RPi.GPIO as GPIO
import time

A=15
CNT=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(A,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)

while 1:
    if GPIO.input(A) == GPIO.HIGH:
        #print("button on!")
        time.sleep(0.3)
        
        #MOTOR
        
        CNT=CNT+1
        print("COUNT =",CNT)
        
        
        if CNT >= 60:
            print("!!Please replace!!")
       
GPIO.cleanup()