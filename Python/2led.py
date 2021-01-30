#LED Blink
#Written by: Abby Paquette

import RPi.GPIO as GPIO #The imports needed to use the GPIO pins
import time #The time module

x = 0 #Starting my variable for the number of times through the loop at 10
GPIO.setmode(GPIO.BCM) #Setting the system that will be used to identify the pins
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT) #Each pin on the pi's gpio pinout is set to an output
GPIO.setup(26,GPIO.OUT)

while True: #So that this keeps going until I tell it to exit
	if x <= 10: #The leds only blink ten times
		GPIO.output(21,GPIO.HIGH) #Sending power to each pin, turning on the leds
		GPIO.output(26,GPIO.HIGH)
		time.sleep(1) #Waiting
		GPIO.output(21,GPIO.LOW) #Stop sending power, turning of the leds
		GPIO.output(26,GPIO.LOW)
		time.sleep(1) #Sleeps so that you can see the blink, and so that the leds don't go crazy
		x = x+1 #Add one to the counter
	else: #If it's been more than 10 times
		exit() #End the program
