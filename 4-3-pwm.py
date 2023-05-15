
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

comp_pin = 24
GPIO.setup(comp_pin, GPIO.OUT)
GPIO.output(comp_pin, 1)
pwm_pin = 15
GPIO.setup(pwm_pin, GPIO.OUT)
p = GPIO.PWM(pwm_pin, 1000)
p.start(0)
try:
    while(1):
        a = int(input())
        p.start(a)

finally:
    GPIO.output(pwm_pin, 0)
    GPIO.output(comp_pin, 0)
    GPIO.cleanup()

