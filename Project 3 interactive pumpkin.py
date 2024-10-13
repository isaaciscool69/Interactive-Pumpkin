from machine import TouchPad
from machine import Pin
import neopixel
import time
from time import sleep

t1 = TouchPad(Pin(4))

NUM_LEDS = 12
NEO_PIXEL_DATA_PIN = 14

leds = neopixel.NeoPixel(Pin(NEO_PIXEL_DATA_PIN), NUM_LEDS)

def lights_red():
    leds[0] = (255, 0, 0)
    leds[1] = (255, 0, 0)
    leds[2] = (255, 0, 0)
    leds[3] = (255, 0, 0)
    leds[4] = (255, 0, 0)
    leds[5] = (255, 0, 0)
    leds[6] = (255, 0, 0)
    leds[7] = (255, 0, 0)
    leds[8] = (255, 0, 0)
    leds[9] = (255, 0, 0)
    leds[10] = (255, 0, 0)
    leds[11] = (255, 0, 0)
    
    leds.write()

def leds_green():
    leds[0] = (0, 255, 0)
    leds[1] = (0, 255, 0)
    leds[2] = (0, 255, 0)
    leds[3] = (0, 255, 0)
    leds[4] = (0, 255, 0)
    leds[5] = (0, 255, 0)
    leds[6] = (0, 255, 0)
    leds[7] = (0, 255, 0)
    leds[8] = (0, 255, 0)
    leds[9] = (0, 255, 0)
    leds[10] = (0, 255, 0)
    leds[11] = (0, 255, 0)
    
    leds.write()
    
def leds_blue():
    leds[0] = (0, 0, 255)
    leds[1] = (0, 0, 255)
    leds[2] = (0, 0, 255)
    leds[3] = (0, 0, 255)
    leds[4] = (0, 0, 255)
    leds[5] = (0, 0, 255)
    leds[6] = (0, 0, 255)
    leds[7] = (0, 0, 255)
    leds[8] = (0, 0, 255)
    leds[9] = (0, 0, 255)
    leds[10] = (0, 0, 255)
    leds[11] = (0, 0, 255)
    
    leds.write()
    
def leds_orange():
    leds[0] = (255, 165, 0)
    leds[1] = (255, 165, 0)
    leds[2] = (255, 165, 0)
    leds[3] = (255, 165, 0)
    leds[4] = (255, 165, 0)
    leds[5] = (255, 165, 0)
    leds[6] = (255, 165, 0)
    leds[7] = (255, 165, 0)
    leds[8] = (255, 165, 0)
    leds[9] = (255, 165, 0)
    leds[10] = (255, 165, 0)
    leds[11] = (255, 165, 0)
    
    leds.write()
    
def leds_yellow():
    leds[0] = (255, 255, 0)
    leds[1] = (255, 255, 0)
    leds[2] = (255, 255, 0)
    leds[3] = (255, 255, 0)
    leds[4] = (255, 255, 0)
    leds[5] = (255, 255, 0)
    leds[6] = (255, 255, 0)
    leds[7] = (255, 255, 0)
    leds[8] = (255, 255, 0)
    leds[9] = (255, 255, 0)
    leds[10] = (255, 255, 0)
    leds[11] = (255, 255, 0)
    
    leds.write()

import time
from time import sleep

if t1.read() < 40000:
    lights_red()
    
while True:
    print(t1.read)
    if t1.read() < 40000:
        lights_red()
        sleep(0.5)
        leds_orange()
        sleep(0.5)
    elif t1.read() > 40000:
        leds_blue()
        sleep(0.5)
        leds_green()
        sleep(0.5)
    else:
        lights_red()
            
            
        
     
        
