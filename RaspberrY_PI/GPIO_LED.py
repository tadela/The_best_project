import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
    if GPIO.input(10) == GPIO.HIGH:
        GPIO.output(12, GPIO.HIGH)
    elif GPIO.input(10) == GPIO.LOW:
                GPIO.output(12, GPIO.HIGH)
    else:
        GPIO.output(16, GPIO.HIGH)
#    GPIO.output(12, GPIO.HIGH)
#    sleep(1)
#    GPIO.output(12, GPIO.LOW)
#    sleep(1)
#    GPIO.output(22, GPIO.LOW)
#    sleep(1)
#    GPIO.output(22, GPIO.HIGH)
#    sleep(1)
