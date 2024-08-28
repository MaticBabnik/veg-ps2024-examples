from machine import Pin, PWM
from time import sleep

speaker_pwm = PWM(Pin(14, Pin.OUT), freq=440, duty=0)

def ton(freq, t):
    speaker_pwm.duty(512)
    speaker_pwm.freq(freq)
    sleep(t)
    speaker_pwm.duty(0)
    
ton(440, 1)
ton(400, .5)

