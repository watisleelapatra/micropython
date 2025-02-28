from machine import Pin, SoftI2C
from i2c_lcd import I2cLcd
from time import sleep
import dht 
# Define the LCD I2C address and dimensions
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
sensor = dht.DHT11(Pin(13))
i2c = SoftI2C(sda=Pin(4), scl=Pin(5), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
lcd.clear()
while True:
  try:
      
      sensor.measure()
      temp = sensor.temperature()
      humid = sensor.humidity()
      lcd.move_to(0,0)
      lcd.putstr("Temperature:")
      lcd.move_to(13,0)
      lcd.putstr(str(temp))
      #print("Temperature:",temp, end=' ')
      lcd.move_to(0, 1)
      lcd.putstr("Humidity:")
      lcd.move_to(10,1)
      lcd.putstr(str(humid))
      #print("°C Humidity:",humid,"%")
      sleep(2)
  except OSError as e:
      print('Failed to read sensor.')