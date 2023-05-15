import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.OUT)

def dec2bin(val):
    return [int(elem) for elem in bin(val)[2:].zfill(8)]

def adc():
    l = -1
    r = 256

    while(l+1<r):
        mid = (l+r)//2
        GPIO.output(dac, dec2bin(mid))
        time.sleep(0.1)
        cval = GPIO.input(comp)
        
        if(cval == 0):
            r = mid
        else:
            l = mid
   
    return r

try:
    while 1:
        val = adc()
        if val != 0:
            print(val)
            print(val*3.3/256)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
