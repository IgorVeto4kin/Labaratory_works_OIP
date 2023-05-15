import time
import RPi.GPIO as GPIO
dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(val):
    return [int(elem) for elem in bin(val)[2:].zfill(8)]

try:
    while(1):
        a = float(input())/512
        for i in range(256):
            GPIO.output(dac, dec2bin(i))
            time.sleep(a)
        for i in range(255, -1, -1):
            GPIO.output(dac, dec2bin(i))
            time.sleep(a)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
