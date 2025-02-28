from machine import Pin, SoftI2C
from i2c_lcd import I2cLcd
from time import sleep

# Define the LCD I2C address and dimensions
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = SoftI2C(sda=Pin(4), scl=Pin(5), freq=400000)

lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.putstr("It's working :)")
sleep(4)

try:
    while True:
        # Clear the LCD
        lcd.clear()
        # Display two different messages on different lines
        # By default, it will start at (0,0) if the display is empty
        lcd.putstr("MicroPython")
        sleep(2)
        lcd.clear()
        # Starting at the second line (0, 1)
        lcd.move_to(0, 1)
        lcd.putstr("is fun!")
        sleep(2)

except KeyboardInterrupt:
    # Turn off the display
    print("Keyboard interrupt")
    lcd.backlight_off()
    lcd.display_off()