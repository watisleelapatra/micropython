from machine import Pin
from time import sleep
buzzerPin = 12 #D6
buzzer = Pin(buzzerPin, Pin.OUT)
while True:
    buzzer.value(1)
    sleep(0.5)
    buzzer.value(0)
    sleep(0.5)
    