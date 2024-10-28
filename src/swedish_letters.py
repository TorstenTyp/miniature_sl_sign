from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 40)

a_with_ring = bytearray([0x04, 0x0A, 0x0E, 0x01, 0x0F, 0x11, 0x0F, 0x00])
a_with_dots = bytearray([0x0A, 0x00, 0x0E, 0x01, 0x0F, 0x11, 0x0F, 0x00])
o_with_dots = bytearray([0x0A, 0x00, 0x0E, 0x11, 0x11, 0x11, 0x0E, 0x00])
capital_a_with_ring = bytearray([0x0E, 0x11, 0x0E, 0x11, 0x11, 0x1F, 0x11, 0x00])
capital_a_with_dots = bytearray([0x11, 0x0E, 0x11, 0x11, 0x11, 0x1F, 0x11, 0x00])
capital_o_with_dots = bytearray([0x11, 0x0E, 0x11, 0x11, 0x11, 0x11, 0x0E, 0x00])

lcd.custom_char(0, a_with_ring)
lcd.custom_char(1, a_with_dots)
lcd.custom_char(2, o_with_dots)
lcd.custom_char(3, capital_a_with_ring)
lcd.custom_char(4, capital_a_with_dots)
lcd.custom_char(5, capital_o_with_dots)

def swedify_string(string):
    swedish_string = string.replace("å", chr(0)).replace("ä", chr(1)).replace("ö", chr(2)).replace("Å", chr(3)).replace("Ä", chr(4)).replace("Ö", chr(5))
    return swedish_string