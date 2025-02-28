from machine import Pin, ADC
from time import sleep

Pot = ADC(0) #A0
LED = Pin(2, Pin.OUT) #Buildin LED @ GPIO2
while True:
    pot_value = Pot.read()
    #print(pot_value)
    LED.value(1)
    sleep(pot_value/800)
    LED.value(0)
    sleep(pot_value/800)