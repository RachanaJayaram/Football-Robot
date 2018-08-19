import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT) #1st servo
#GPIO.setup(n,GPIO.OUT) #2nd servo (just put pin no.acc. to what's convenient)
#p1=GPIO.PWM(n, 50)
p = GPIO.PWM(4, 50) 
p.start(7.5)
p1.start(7.5)

def lowerarm():
    p.ChangeDutyCycle(7.5)
    p1.ChangeDutyCycle(7.5) # turn towards 90 degree
    time.sleep(1) # sleep 1 second

def raisearm():
    p.ChangeDutyCycle(2.5)
    p1.ChangeDutyCycle(2.5) # turn towards 0 degree
    time.sleep(1) # sleep 1 second
