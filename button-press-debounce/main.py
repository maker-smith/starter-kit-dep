import utime
from machine import Pin

# ARGS
DEBOUNCE_TIMEOUT = 200

button_pressed_count = 0
button_pressed_time = 0


def button1_pressed(change):
    global button_pressed_count, button_pressed_time
    button_pressed_time_new = utime.ticks_ms()

    if (button_pressed_time_new - button_pressed_time) > DEBOUNCE_TIMEOUT:
        button_pressed_count += 1
        button_pressed_time = button_pressed_time_new


button = Pin(19, Pin.IN, Pin.PULL_DOWN)
button.irq(handler=button1_pressed, trigger=Pin.IRQ_FALLING)

button_pressed_count_old = 0
while True:
    if button_pressed_count_old != button_pressed_count:
        print("Button press count:", button_pressed_count)
        button_pressed_count_old = button_pressed_count
