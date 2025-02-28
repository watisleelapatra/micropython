from machine import Pin, ADC
from time import sleep

LED = Pin(2, Pin.OUT) #Builtin LED GPIO2
LDR = ADC(0)
while True:
    Light = LDR.read()
    print(Light)
    sleep(1)
    