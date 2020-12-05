from machine import Pin
from neopixel import NeoPixel
import time

headlight_pin = 16 # D0
headlight_toggle = 0 # D3
np_pin = 5 # D1
np_toggle = 2 # D4
np_change = 4 # D2

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
	'yellow': (255,255,51),
	'white': (255,255,255),
	'off': (0,0,0)
}

def light_pixel(color):
	np[1] = colors['off']
	np.write()
	if(not color == 'off'):
		np[1] = colors[color]
		np.write()

while True:
	if(headlight_toggle_v.value()):
		headlight_pin_v.on()
	else():
		headlight_pin_v.off()
	if(np_toggle_v.value()):
		if(np_change_v.value()):
			if(np_value == 'green'):
				np_value = 'yellow'
			elif(np_value == 'yellow'):
				np_value = 'red'
			else:
				np_value = 'green'
		light_pixel(np_value)
	else:
		light_pixel('off')
	time.sleep(0.01)