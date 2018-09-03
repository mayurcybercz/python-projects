import RPi.GPIO as GPIO  #general purpose input output library
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)  #pin 4 is output pin
while true:
    GPIO.output(4,True) #high voltage at pin 4
    time.sleep(1)  #wait for 1 sec
    GPIO.output(4,False)  #no voltage at pin 4
    time.sleep(1) #wait for 1 sec(4