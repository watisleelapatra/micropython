from machine import Pin
from time import sleep
import dht 

sensor = dht.DHT11(Pin(13))

while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    humid = sensor.humidity()
    print("Temperature:",temp, end=' ')
    print("°C Humidity:",humid,"%")
  except OSError as e:
    print('Failed to read sensor.')