#Test sound detector module digital output
from machine import Pin
from time import sleep

Mic = Pin(14, Pin.IN) #D5
while True:
    sound = Mic.value()
    print(sound)
    sleep(0.1)