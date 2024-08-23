import machine
import time
import dht
import lcd128_32_fonts
from lcd128_32 import lcd128_32

clock_pin = 22
data_pin = 21
bus = 0
i2c_addr = 0x3f
use_i2c = True

DHT = dht.DHT11(machine.Pin(15))

def scan_for_devices():
    i2c = machine.I2C(bus,sda=machine.Pin(data_pin),scl=machine.Pin(clock_pin))
    devices = i2c.scan()
    if devices:
        for d in devices:
            print(hex(d))
    else:
        print('no i2c devices')

if use_i2c:
    scan_for_devices()
    lcd = lcd128_32(data_pin, clock_pin, bus, i2c_addr)
lcd.Clear()
while True:
    DHT.measure() 
    temp= str(DHT.temperature())
    humi = str(DHT.humidity())

    time.sleep_ms(1000)
    
    lcd.Cursor(0, 0)
    lcd.Display("xh_0.2")
    lcd.Cursor(1, 0)
    lcd.Display("temperature: " + temp + " C")
    lcd.Cursor(2, 0)
    lcd.Display("")
    lcd.Cursor(3, 0)
    lcd.Display("humidity: " + humi + " %")
    

while True:
    time.sleep(0.5)
