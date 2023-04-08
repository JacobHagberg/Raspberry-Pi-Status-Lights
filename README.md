# Raspberry-Pi-Status-Lights
This program is intended to be used on the Raspberry Pi to with a ws281x LED strip to be used as a status light for a computer program. 

It works by reading from its JSON file and then setting the lights on the LED strip to the values in the JSON file. To link a program to the status lights jsut have it change the value in the JSON file that matches up with its LED on the strip. 

Libraries Used:
1. rpi_ws281x: For interacting with ws281x led lights on Raspberry Pi with GPIO pins.
2. time: For adding delay.
3. json: For interaction with JSON files.


