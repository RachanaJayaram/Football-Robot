import RPi.GPIO as GPIO
from time import sleep



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

motor1a=23
motor1b=24
motor1e=25

motor2a=17
motor2b=27
motor2e=22

pi=22.0/7.0
dia=7
axl=21
r=dia/2

GPIO.setup(motor1a,GPIO.OUT)
GPIO.setup(motor1b,GPIO.OUT)
GPIO.setup(motor1e,GPIO.OUT)

GPIO.setup(motor2a,GPIO.OUT)
GPIO.setup(motor2b,GPIO.OUT)
GPIO.setup(motor2e,GPIO.OUT)


def stopmotors():

        GPIO.output(motor1e,GPIO.LOW)
        GPIO.output(motor2e,GPIO.LOW)
        sleep(1)
def forward(dist,e=1,f=0):
        r=dia/2
        if (f==1):
                dist-=10.2

        pwm1=GPIO.PWM(25,100)
        pwm1.start(82)

        GPIO.output(motor1a,GPIO.LOW)
        GPIO.output(motor1b,GPIO.HIGH)
        GPIO.output(motor1e,GPIO.HIGH)

        GPIO.output(motor2a,GPIO.HIGH)
        GPIO.output(motor2b,GPIO.LOW)
        GPIO.output(motor2e,GPIO.HIGH)
        time_req=(dist/(2*pi*r))*(60.0/200.0)*e
        print(time_req)
        sleep(time_req)

        pwm1.stop()
        stopmotors()

def backward(dist,e=1,f=0):
        r=dia/2
        if (f==1):
                dist-=10.2

        GPIO.output(motor1a,GPIO.HIGH)
        GPIO.output(motor1b,GPIO.LOW)
        GPIO.output(motor1e,GPIO.HIGH)

        GPIO.output(motor2a,GPIO.LOW)
        GPIO.output(motor2b,GPIO.HIGH)
        GPIO.output(motor2e,GPIO.HIGH)
        time_req=(dist/(2*pi*r))*(60.0/200.0)*e
        sleep(time_req)
        stopmotors()

def clockwise(angle,e=1):
        t_req=angle*axl*e/(2400.0*r)
        pwm1=GPIO.PWM(25,100)


        pwm1.start(82)

        GPIO.output(motor1a,GPIO.LOW)
        GPIO.output(motor1b,GPIO.HIGH)
        GPIO.output(motor1e,GPIO.HIGH)


        GPIO.output(motor2a,GPIO.LOW)
        GPIO.output(motor2b,GPIO.HIGH)
        GPIO.output(motor2e,GPIO.HIGH)

        sleep(t_req)

        pwm1.stop()
        stopmotors()

def anticlockwise(angle,e=1):
        t_req=angle*axl*e/(2400.0*r)
        pwm1=GPIO.PWM(25,100)


        pwm1.start(82)

        GPIO.output(motor1a,GPIO.HIGH)
        GPIO.output(motor1b,GPIO.LOW)
        GPIO.output(motor1e,GPIO.HIGH)

        GPIO.output(motor2a,GPIO.HIGH)
        GPIO.output(motor2b,GPIO.LOW)
        GPIO.output(motor2e,GPIO.HIGH)

        sleep(t_req)

        pwm1.stop()
        stopmotors()
