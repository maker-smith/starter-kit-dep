import time
from machine import Pin

PIN = 2
SLEEP_MS = 500

p2 = Pin(PIN, Pin.OUT)

while True:
    p2.on()
    time.sleep_ms(SLEEP_MS)
    p2.off()
    time.sleep_ms(SLEEP_MS)
