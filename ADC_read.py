from machine import Pin, ADC
from time import sleep

Pot = ADC(0)
while True:
    pot_value = Pot.read()
    print(pot_value)
    sleep(0.5)