import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

def dec2bin(val):
    return [int(elem) for elem in bin(val)[2:].zfill(8)]

def adc():
    lqw = -1
    r = 256

    while(lqw+1<r):
        mid = (lqw+r)//2
        GPIO.output(dac, dec2bin(mid))
        time.sleep(0.1)
        cval = GPIO.input(comp)
        #print(mid)
        if(cval == 0):
            r = mid  
        else:
            lqw = mid
   
    return mid

try:
    while 1:
        val = adc()
        GPIO.output(leds, dec2bin(val))
        print(GPIO.input(troyka))
        if val != 0:
            print(val)
            print(val*3.3/256)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
