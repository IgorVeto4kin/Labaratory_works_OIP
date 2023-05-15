import RPi.GPIO as GPIO
dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def dec2bin(val):
    return [int(elem) for elem in bin(val)[2:].zfill(8)]
try:
    while(True):
        a = input()
        if "." in a:
            print("only integer values")
            continue
        a = int(a)
        if(a>=0 and a<=255):
            GPIO.output(dac, dec2bin(a))
            print(dec2bin(a))
        elif(a<0):
            print("No negative values")
        elif(a>255):
            print("too big value")
        
        

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
