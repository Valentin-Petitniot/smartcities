from machine import Pin, Timer
import utime

led = Pin(18, Pin.OUT)
button = Pin(16, Pin.IN)

global Mode
Mode = 0

def tick(timer):
    if button.value() == 1:
        utime.sleep_ms(200)
        changeSpeed()
        global Mode 
        Mode += 1        
        
def changeSpeed():
    i = 0
    for i in range(10):
        led.value(not led.value())
        utime.sleep_ms(40)
        
        
Timer().init(freq=10000, mode=Timer.PERIODIC, callback=tick)
        
while True:
    if Mode == 1:        
        led.value(not led.value())
        utime.sleep_ms(1000)
    elif Mode == 2:        
        led.value(not led.value())
        utime.sleep_ms(250)
    elif Mode > 2 & Mode != 0:        
        led.value(0)
        Mode = 0