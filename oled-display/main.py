from machine import Pin, SoftI2C
import ssd1306

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text("Hello Line 1!", 0, 0)
oled.text("Hello Line 2!", 0, 10)
oled.text("Hello Line 3!", 0, 20)

oled.show()
