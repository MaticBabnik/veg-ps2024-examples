from machine import ADC, Pin
from time import sleep

adc = ADC(Pin(39), atten=ADC.ATTN_11DB)


while True:
    print(adc.read_u16() >> 8)
    sleep(0.5)