# Automatic Dice Roller
# Written by: Abby Paquette

import time #importing the time module so that I can use commands like time.sleep
from random import randint #This is the module that lets me generate a random number, and I specifically imported the part that let me generate an integer

print ("Automatic Dice Roller") #Printing this is half to tell the user what the program is and half to test and make sure it is running

while True:
	time.sleep(.25) #Pause for 1/4 of a second so the pi doesn't overload from trying to print and process super quickly
	repeat = input("Press enter to roll or x and enter to quit.") #Instructions are printed for the user, and read as an input
	if repeat == (""): #If the user presses enter, roll the die
		print(randint(1,6)) #This prints a random integer between 1 and 6
	if repeat == ("x"): #If the user presses x and then enter,
		exit() #Exit the program 
