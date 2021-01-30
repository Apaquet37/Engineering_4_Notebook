#LED Blink
#Written by: Abby Paquette

import RPi.GPIO as GPIO
import time

x = 0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

while True:
	if x <= 10:
		GPIO.output(21,GPIO.HIGH)
		GPIO.output(26,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(21,GPIO.LOW)
		GPIO.output(26,GPIO.LOW)
		time.sleep(1)
		x = x+1
	else:
		exit()
