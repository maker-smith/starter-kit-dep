from machine import Pin, PWM
from time import sleep

# ARGS
PWM_PIN = 14
CLOCKWISE_PIN = 27
COUNTER_CLOCKWISE_PIN = 26
MAX_DUTY_CYCLE = 65535
PWM_FREQUENCY = 50


# Drive function
def drive(speed, direction, pwm_pin, clockwise_pin, counter_clockwise_pin):
    if speed > 100 or speed < 0:
        raise Exception("Speed must be between 0 - 100")

    pwm = PWM(Pin(pwm_pin))
    pwm.freq(PWM_FREQUENCY)
    pwm.duty_u16(int(speed / 100 * MAX_DUTY_CYCLE))
    clockwise = Pin(clockwise_pin, Pin.OUT)
    counter_clockwise = Pin(counter_clockwise_pin, Pin.OUT)

    if direction < 0:
        clockwise.value(0)
        counter_clockwise.value(1)
    elif direction > 0:
        clockwise.value(1)
        counter_clockwise.value(0)
    else:
        clockwise.value(0)
        counter_clockwise.value(0)


# Run script
print("Rotating clockwise...")
drive(50, 1, PWM_PIN, CLOCKWISE_PIN, COUNTER_CLOCKWISE_PIN)
sleep(2)
print("Rotating counter clockwise...")
drive(50, -1, PWM_PIN, CLOCKWISE_PIN, COUNTER_CLOCKWISE_PIN)
sleep(2)
print("Done")
drive(50, 0, PWM_PIN, CLOCKWISE_PIN, COUNTER_CLOCKWISE_PIN)
