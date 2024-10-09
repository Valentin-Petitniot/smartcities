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
RunningTh = True
consTemp = 15
temp = 0
diffConsTemp = 0
global alarm
alarm = 0
buzzer.freq(698)
buzzer.duty_u16(0)
    
def LedBlinking():            
    while RunningTh == True:
        # print('[TH]alarm: ' + str(alarm))
        if alarm == 1:
            buzzer.duty_u16(0) #  Mute le buzzer
            led.value(1)
            utime.sleep_ms(500)
            led.value(0)
            utime.sleep_ms(500)                        
        if alarm == 2:
            buzzer.duty_u16(32500) # Fais sonner le buzzer
            led.value(1)
            utime.sleep_ms(150)
            led.value(0)
            utime.sleep_ms(150)
        if alarm == 0:
            buzzer.duty_u16(0) #  Mute le buzzer
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
        # print('diff: ' + str(diffConsTemp))
        if diffConsTemp > 0:
            if diffConsTemp >= 3:
                alarm = 2
                # print('[Main] alarm = 2')  
                d.clear()              
                d.setCursor(0,0)
                d.print('ALARM !!!!!')    
            else :
                alarm = 1
                # print('[Main] alarm = 1')
                d.clear()
                d.setCursor(0,1)
                d.print('Ambient: ' + str(round(temp,2)))  
                d.setCursor(0,0)
                d.print('Set: ' + str(consTemp))    
        else:
            alarm = 0
            # print('[Main] alarm = 0')
            # Affichage        
            d.clear()
            d.setCursor(0,1)
            d.print('Ambient: ' + str(round(temp,2)))  
            d.setCursor(0,0)
            d.print('Set: ' + str(consTemp))    
            
        utime.sleep_ms(1000)        

    _thread.exit()

except KeyboardInterrupt:        
    Running = False
    
except SystemExit:
    RunningTh = False

finally:
    print('Program finished')    