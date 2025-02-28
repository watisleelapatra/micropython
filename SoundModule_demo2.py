#Test sound detector module analog output
from machine import Pin, ADC
from time import sleep

Mic = ADC(0)
while True:
    sound = Mic.read()
    print(sound)
    sleep(0.05)