from machine import Pin
from neopixel import NeoPixel
import time

headlight_pin = 4 # D2
headlight_toggle = 14  # D5
np_pin = 5 # D1
np_toggle = 12 # D6
np_change = 13 # D7

# Setup outputs
headlight_pin_v = Pin(headlight_pin, Pin.OUT)
np = NeoPixel(Pin(np_pin), 1)

# Setup inputs
headlight_toggle_v = Pin(headlight_toggle, Pin.IN, Pin.PULL_UP)
np_toggle_v = Pin(np_toggle, Pin.IN, Pin.PULL_UP)
np_change_v = Pin(np_change, Pin.IN, Pin.PULL_UP)

np_value = 'green'

colors = {
	'red': (255,0,0),
	'green': (0,153,0),
	'yellow': (255,100,51),
	'white': (255,255,255),
	'off': (0,0,0)
}

def light_pixel(color):
	global np
	np[0] = colors['off']
	np.write()
	if(not color == 'off'):
		np[0] = colors[color]
		np.write()

def switch():
	global np_value
	if(np_value == 'green'):
		np_value = 'yellow'
	elif(np_value == 'yellow'):
		np_value = 'red'
	else:
		np_value = 'green'

def run():
	global headlight_toggle_v
	global headlight_pin_v
	global np_toggle_v
	global np_change_v
	if(headlight_toggle_v.value()):
		headlight_pin_v.value(1)
	else:
		headlight_pin_v.value(0)
	if(np_toggle_v.value()):
		if(not np_change_v.value()):
			switch()
		light_pixel(np_value)
	else:
		light_pixel('off')
	time.sleep(0.15)

while True:
	run()