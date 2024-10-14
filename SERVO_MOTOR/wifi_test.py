import network
import socket
import utime
import machine
import time
import ntptime

ssid = "Pixel Val"
password = "bienvenu"

def connect():
    #connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection ...')
        utime.sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'connected on {ip}')
    return ip

try:
    ip = connect()   
    print("Local time before synchronization %s" %str(time.localtime()))
    ntptime.settime()
    ltime = time.localtime()
    # localtime + 2 because the api don't provide france's timestamp. +2 is an offset to get Belgian time
    Hour = ltime[3] + 2
    tuTime = (ltime[0], ltime[1], ltime[2], Hour, ltime[4], ltime[5])    
    print("Local time after synchronization %s" %str(tuTime))
except KeyboardInterrupt:
    machine.reset()
