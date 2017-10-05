#Wilfred Githuka
#LED Control Code. This piece of code controls a blinking LED to show my code is running. Just a test.
#I will merge it with the main  code later

import RPi.GPIO as GPIO
import time

LedPin = 11

def setup():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(LedPin, GPIO.OUT)
        GPIO.output(LedPin, GPIO.HIGH)

def blink():
        while True:
                GPIO.output(LedPin, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(LedPin, GPIO.LOW)
                time.sleep(0.5)

setup()
blink()
 
