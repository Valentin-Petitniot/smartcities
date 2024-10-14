from machine import Pin, PWM
import utime
from servo import SERVO

servo = SERVO(Pin(20))
a = 180

while True:
    a = a == 0 and 180 or a - 1
    servo.turn(a)
    utime.sleep_ms(100)