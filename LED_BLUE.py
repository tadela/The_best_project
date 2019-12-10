import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)

def blue_led():
    while True:
        GPIO.output(12, GPIO.HIGH)
        sleep(1)
        GPIO.output(12, GPIO.LOW)
        sleep(1)
        return

def red_led():
    while True:
        GPIO.output(16, GPIO.HIGH)
        sleep(1)
        GPIO.output(16, GPIO.LOW)
        sleep(1)
        return