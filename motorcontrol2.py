import RPi.GPIO as GPIO          
from time import sleep

L1 = 24
L2 = 23
R1 = 27
R2 = 17
enA = 25
enB = 22
temp1=1

speed=50

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
WheelL=GPIO.PWM(enA,1000)
WheelR=GPIO.PWM(enB,1000)
WheelL.start(speed)
WheelR.start(speed)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=input()

    if x== 'w':
        print("forward")
        WheelL.ChangeDutyCycle(50)
        WheelR.ChangeDutyCycle(50)
        GPIO.output(L1,GPIO.HIGH)
        GPIO.output(L2,GPIO.LOW)
        GPIO.output(R1,GPIO.HIGH)
        GPIO.output(R2,GPIO.LOW)
        x='z'

    elif x=='s':
        print("stop")
        GPIO.output(L1,GPIO.LOW)
        GPIO.output(L2,GPIO.LOW)
        GPIO.output(R1,GPIO.LOW)
        GPIO.output(R2,GPIO.LOW)
        x='z'

    elif x=='q':
        print("left turn")
        WheelL.ChangeDutyCycle(25)
        WheelR.ChangeDutyCycle(50)
        GPIO.output(L1,GPIO.HIGH)
        GPIO.output(L2,GPIO.LOW)
        GPIO.output(R1,GPIO.HIGH)
        GPIO.output(R2,GPIO.LOW)
        x='z'

    elif x=='b':
        print("right turn")
        WheelL.ChangeDutyCycle(50)
        WheelR.ChangeDutyCycle(25)
        GPIO.output(L1,GPIO.HIGH)
        GPIO.output(L2,GPIO.LOW)
        GPIO.output(R1,GPIO.HIGH)
        GPIO.output(R2,GPIO.LOW)
        x='z'
"""
    elif x=='l':
        print("low")
        p.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        p.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        p.ChangeDutyCycle(75)
        x='z'
     
    
    elif x=='e':
        GPIO.cleanup()
        break
"""
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
