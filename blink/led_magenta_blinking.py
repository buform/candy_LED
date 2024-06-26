#!/usr/bin/python

from random import randrange
import sys
from time import sleep

devpath = '/dev/hidraw0'

colors = {
    'red': 0x01,
    'green': 0x02,
    'blue': 0x03,
    'yellow': 0x04,
    'magenta': 0x05,
    'cyan': 0x06,
    'white': 0x07,
    'black': 0x08
}

def changeColor(color='white'):
    chsum = lambda b0, b1, b3: (21 * b0**2 + 19 * b1 - 3 * b3) % 255

    cmd = bytearray.fromhex('ff' * 64)
    cmd[0] = 0x11
    cmd[1] = colors[color]
    cmd[3] = randrange(255)
    cmd[2] = chsum(cmd[0], cmd[1], cmd[3])

    try:
        with open(devpath, 'wb') as d:
            d.write(cmd)
    except IOError:
        print("no dostep " + devpath)
        raise
        
for i in range (1000):
	changeColor('magenta')
	sleep(0.5)
	changeColor('black')
	sleep(0.5)
