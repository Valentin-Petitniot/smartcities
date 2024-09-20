from machine import Pin
from time import sleep


led = Pin(16, Pin.OUT)
print('Blinking LED example')

while True:
    led.value(not led.value())
    sleep(0.5)

    