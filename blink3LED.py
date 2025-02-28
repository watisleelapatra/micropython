#Blink built-in blue LED
import machine
import time

red = machine.Pin(14, machine.Pin.OUT)	#D5
yellow = machine.Pin(12, machine.Pin.OUT) #D6
green = machine.Pin(13, machine.Pin.OUT) #D7
while True:
    red.value(0)
    yellow.value(0)
    green.value(0) #turn LED on
    time.sleep(0.1) #delay 0.5 second
    red.value(1)
    yellow.value(1)
    green.value(1) #turn LED off
    time.sleep(0.1) #delay 0.5 second
