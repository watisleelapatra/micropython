#Blink built-in blue LED
import machine
import time
#ESP32 Gravitech Nano32 board built-in LED is at GPIO16
#ESP8266 NodeMCU V1,2,3 Blue LED on ESP8266 board is at GPIO2
blue = machine.Pin(2, machine.Pin.OUT)
while True:
    blue.value(0) #turn LED on
    time.sleep(0.1) #delay 0.5 second
    blue.value(1) #turn LED off
    time.sleep(0.1) #delay 0.5 second
