from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
btn = Pin(12, Pin.IN, pull=Pin.PULL_DOWN)

prev = 0

while True:
    cur = btn.value()
    
    if cur == 1 and prev == 0: #tipko smo ravnokar pritisnili
        led.value(not led.value())
    
    prev = cur
    sleep(0.1)

