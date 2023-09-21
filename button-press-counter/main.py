from machine import Pin

button_pressed_count = 0


def button1_pressed(change):
    global button_pressed_count
    button_pressed_count += 1


button = Pin(19, Pin.IN, Pin.PULL_DOWN)
button.irq(handler=button1_pressed, trigger=Pin.IRQ_FALLING)

button_pressed_count_old = 0
while True:
    if button_pressed_count_old != button_pressed_count:
        print("Button press count:", button_pressed_count)
        button_pressed_count_old = button_pressed_count
