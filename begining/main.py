from machine import Pin, Timer
import utime


led = Pin(16, Pin.IN)
print('Blinking LED example')

def onButtonClicked():
    print('Button clicked')

led.irq(trigger=Pin.IRQ_FALLING, handler=onButtonClicked)    

while True:
    print('Hello World')
    led.value(not led.value())
    utime.sleep(0.5)
    

    