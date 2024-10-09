from machine import I2C, Pin, ADC, PWM, Timer
import utime
import _thread
from lcd1602 import LCD1602
from dht11 import DHT


# Initialize
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
d=LCD1602(i2c, 2, 16)
buzzer = PWM(Pin(27))
potar = ADC(0)
led = Pin(16, Pin.OUT)

d.display()
dht = DHT(18)


# declaration
Running = True
consTemp = 15
temp = 0
diffConsTemp = 0
alarm = 0
    
def LedBlinking():            
    while Running == True:
        print('alarm: ' + str(alarm))
        if alarm == 1:
            led.value(1)
            utime.sleep_ms(500)
            led.value(0)
            utime.sleep_ms(500)
        if alarm == 2:
            led.value(1)
            utime.sleep_ms(250)
            led.value(0)
            utime.sleep_ms(250)
        if alarm == 0:
            led.value(0)
            utime.sleep_ms(1000)


        
        
_thread.start_new_thread(LedBlinking, ())

try:
    while Running == True:           
        # Lecture Potentiomètre
        consTemp = potar.read_u16()
        consTemp = ((consTemp/65535)*20)+15
        consTemp = round(consTemp, 0)  
        
        # Lecture Temperature        
        temp,humid = dht.readTempHumid()  

        diffConsTemp = temp - consTemp
        print('diff: ' + str(diffConsTemp))
        if diffConsTemp < 0:
            if diffConsTemp <= 3:
                alarm = 2
            if diffConsTemp <= 0:
                alarm = 0
            else:
                alarm = 1


        # Affichage
        d.setCursor(0,1)
        d.print('Ambient: ' + str(round(temp,2)))  
        d.setCursor(0,0)
        d.print('Set: ' + str(consTemp))    
        utime.sleep_ms(1000)

except KeyboardInterrupt:
    print('Program Finished')
finally:
    Running = False    