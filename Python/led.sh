#!/bin/bash

for i in {1..10}
do
	/usr/bin/gpio -1 toggle 40
	sleep .5
	/usr/bin/gpio -1 toggle 40
	sleep .5
done
