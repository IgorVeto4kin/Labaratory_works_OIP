import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

def dec2bin(val):
    return [int(elem) for elem in bin(val)[2:].zfill(8)]

def adc():
    for i in range(255):
        dac_new = dec2bin(i)
        GPIO.output(dac, dac_new)
        cval = GPIO.input(comp)
        time.sleep(0.01)

        if(cval == 0):
            return i
try:
    while 1:
        val = adc()
        if val != 0:
            print(val)
            print(val*3.3/256)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
