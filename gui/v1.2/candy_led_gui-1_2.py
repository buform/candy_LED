import tkinter as tk
from random import randrange

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
blink_active = False

def changeColor(color='white'):
    """ Change Dell Chromebook 11 led color """
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
        error_message = f"Can't access {devpath}"
        tk.messagebox.showerror("Error", error_message)

def blink_color(color):
    """ Blink the LED with the specified color """
    global blink_active

    if blink_active:
        changeColor(color)
        main_window.after(500, lambda: changeColor('black'))
        main_window.after(1000, lambda: blink_color(color))

def create_main_menu():
    global main_window
    main_window = tk.Tk()
    main_window.title("MENU")

    const_button = tk.Button(
        main_window,
        text="CONST",
        command=lambda: create_color_menu(main_window),
        bg="grey",
        fg="white"
    )
    const_button.pack(pady=10, padx=10, fill=tk.X)

    blink_button = tk.Button(
        main_window,
        text="BLINK",
        command=lambda: create_blink_menu(main_window),
        bg="grey",
        fg="white"
    )
    blink_button.pack(pady=10, padx=10, fill=tk.X)

    main_window.mainloop()

def create_color_menu(main_window):
    color_window = tk.Toplevel()
    color_window.title("CONTROL PANEL OF CANDY LED - CONST")

    for color in colors:
        fg_color = 'black' if color in ['yellow', 'white'] else 'white'
        button = tk.Button(
            color_window,
            text=color.capitalize(),
            command=lambda c=color: changeColor(c),
            bg=tk_colors[color],
            fg=fg_color
        )
        button.pack(pady=5, padx=10, fill=tk.X)

    def back_and_set_black():
        changeColor('black')
        color_window.destroy()

    back_button = tk.Button(
        color_window,
        text="BACK",
        command=back_and_set_black,
        bg="grey",
        fg="white"
    )
    back_button.pack(pady=10, padx=10, fill=tk.X)

def create_blink_menu(main_window):
    global blink_active
    blink_active = True

    color_window = tk.Toplevel()
    color_window.title("CONTROL PANEL OF CANDY LED - BLINK")

    for color in colors:
        fg_color = 'black' if color in ['yellow', 'white'] else 'white'
        button = tk.Button(
            color_window,
            text=color.capitalize(),
            command=lambda c=color: blink_color(c),
            bg=tk_colors[color],
            fg=fg_color
        )
        button.pack(pady=5, padx=10, fill=tk.X)

    def stop_blinking():
        global blink_active
        blink_active = False
        changeColor('black')

    def back_and_set_black():
        global blink_active
        blink_active = False
        changeColor('black')
        color_window.destroy()

    back_button = tk.Button(
        color_window,
        text="BACK",
        command=back_and_set_black,
        bg="grey",
        fg="white"
    )
    back_button.pack(pady=10, padx=10, fill=tk.X)

    stop_button = tk.Button(
        color_window,
        text="STOP",
        command=stop_blinking,
        bg="red",
        fg="white"
    )
    stop_button.pack(pady=10, padx=10, fill=tk.X)

if __name__ == "__main__":
    create_main_menu()
