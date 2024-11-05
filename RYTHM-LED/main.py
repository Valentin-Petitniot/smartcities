import neopixel
from machine import I2C, ADC, Pin
import utime
import random

# Colors Couple
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 100, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)        
WHITE = (255, 255, 255)

COLORS = [BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]

SOUND_SENSOR = ADC(1)

p = Pin.board.GP18
led = neopixel.NeoPixel(p, 1)

while True:
    average = 0
    for i in range (50):
        noise = SOUND_SENSOR.read_u16()
        average = average + noise        
    average = average/50        

    if average > 15500:
        print(average)
        led.fill(random.choice(COLORS))
        led.write()        
        utime.sleep_ms(100)

    
        





