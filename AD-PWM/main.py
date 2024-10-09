from machine import Pin, PWM, ADC, Timer
import utime


potar = ADC(0)
buzzer = PWM(Pin(27))
mute = False

# Octave 6
def DO6(time):
    buzzer.freq(1046)    
    utime.sleep_ms(time)

def RE6(time):
    buzzer.freq(1175)       
    utime.sleep_ms(time)

def MI6(time):
    buzzer.freq(1318) 
    utime.sleep_ms(time)

def FA6(time):
    buzzer.freq(1397)     
    utime.sleep_ms(time)

def SO6(time):
    buzzer.freq(1568)    
    utime.sleep_ms(time)

def LA6(time):
    buzzer.freq(1760)
    utime.sleep_ms(time)

def SI6(time):
    buzzer.freq(1997)
    utime.sleep_ms(time)

def SIb6(time):
    buzzer.freq(1865)
    utime.sleep_ms(time)

# Octave 5
def DO5(time):
    buzzer.freq(523)
    utime.sleep_ms(time)

def RE5(time):
    buzzer.freq(587)  
    utime.sleep_ms(time)

def MI5(time):
    buzzer.freq(659) 
    utime.sleep_ms(time)

def FA5(time):
    buzzer.freq(698)     
    utime.sleep_ms(time)

def SO5(time):
    buzzer.freq(784)   
    utime.sleep_ms(time)

def LA5(time):
    buzzer.freq(880)
    utime.sleep_ms(time)

def SI5(time):
    buzzer.freq(988)
    utime.sleep_ms(time)

def SIb5(time):
    buzzer.freq(932)
    utime.sleep_ms(time)

# Octave 7
def LA7(time):
    buzzer.freq(3520)
    utime.sleep_ms(time)

def N(time):
    global mute
    mute = True
    utime.sleep_ms(time)
    mute = False

def Volume(Mario):    
    if mute == False:
        volume = potar.read_u16()
        if volume < 75:
            volume = 0
        buzzer.duty_u16(volume)
    else :
        buzzer.duty_u16(0)


Timer().init(freq=1000, mode=Timer.PERIODIC, callback=Volume)


MarioBis = [1318, 100, 130, 1318, 100, 200, 1318, 100, 200, 1046, 100, 130, 
            1318, 100, 200, 1568, 100, 400, 784, 100, 300, 1046, 100, 300,
            784, 100, 300, 659, 100, 300, 880, 100, 200, 988, 100, 200,
            932, 100, 100, 880, 100, 1000]

i=0
j = 0

while j < 10:        
    mute = False    
    while i < len(MarioBis):
        buzzer.freq(MarioBis[i])        
        utime.sleep_ms(MarioBis[i+1])
        N(MarioBis[i+2])     
        i = i + 3        
        print('i = ', +  i)
    i = 0    
    j = j + 1
    mute = True
    utime.sleep_ms(1000)
    