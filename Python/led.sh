#!/bin/bash 
#Allows the script to be run just by calling its name

for i in {1..10} #For loop that runs ten times
do #Bash specific syntax
	/usr/bin/gpio -1 toggle 40 #Toggles pin 40 (turning it on)
	/usr/bin/gpio -1 toggle 37 #Toggles pin 37
	sleep .5 #Pause for half a second so you can notice the blink
	/usr/bin/gpio -1 toggle 40 #Toggles pin 40 (turning it off)
	/usr/bin/gpio -1 toggle 37 #Toggles pin 37
	sleep .5 #Pause for half a second
done #Bash specific syntax
