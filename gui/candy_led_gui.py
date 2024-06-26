import tkinter as tk
from random import randrange
import sys

# Available colors
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

# Map tkinter color names to color values
tk_colors = {
    'red': 'red',
    'green': 'green',
    'blue': 'blue',
    'yellow': 'yellow',
    'magenta': 'magenta',
    'cyan': 'cyan',
    'white': 'white',
    'black': 'black'
}

devpath = '/dev/hidraw0'

def changeColor(color='white'):
    """ Change Dell Chromebook 11 led color """

    # Checksum function
    chsum = lambda b0, b1, b3: (21 * b0**2 + 19 * b1 - 3 * b3) % 255

    # Build command
    cmd = bytearray.fromhex('ff' * 64)
    cmd[0] = 0x11
    cmd[1] = colors[color]
    cmd[3] = randrange(255)
    cmd[2] = chsum(cmd[0], cmd[1], cmd[3])

    # Send command
    try:
        with open(devpath, 'wb') as d:
            d.write(cmd)
    except IOError:
        print("Can't access " + devpath)
        raise

def create_gui():
    window = tk.Tk()
    window.title("CANDY LED")

    for color in colors:
        fg_color = 'black' if color in ['yellow', 'white'] else 'white'
        button = tk.Button(
            window, 
            text=color.capitalize(), 
            command=lambda c=color: changeColor(c),
            bg=tk_colors[color],
            fg=fg_color
        )
        button.pack(pady=5, padx=10, fill=tk.X)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
