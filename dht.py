import dht
from machine import Pin
from time import sleep


sensor = dht.DHT11(Pin(14)) 


while True:
    sensor.measure()
    print('temperature: ', sensor.temperature())
    print('humidity: ', sensor.humidity())
    sleep(0.5)
