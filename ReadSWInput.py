#Blink built-in blue LED
import machine
import time

sw = machine.Pin(5, machine.Pin.IN)	#D1

while True:  
    value = sw.value() #turn LED on
    print("Switch = ", value)
    time.sleep(0.5) #delay 1 second
    
