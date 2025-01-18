import tkinter as tk
from random import randrange

# spis kolorów
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

devpath = ""  # Ścieżka urządzenia
blink_active = False
blink_interval = 1000  # Domyślny czas ON/OFF w milisekundach

def changeColor(color='white'):
    global devpath

    if not devpath:
        tk.messagebox.showerror("Error", "Device path is not set. Please select a device.")
        return

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
        error_message = f"Can't access {devpath}. Please check the device path."
        tk.messagebox.showerror("Error", error_message)

def blink_color(color):
    global blink_active, blink_interval

    if blink_active:
        changeColor(color)
        main_window.after(blink_interval // 2, lambda: changeColor('black'))
        main_window.after(blink_interval, lambda: blink_color(color))

def select_device():
    global devpath

    device_window = tk.Toplevel()
    device_window.title("Select Device")

    tk.Label(device_window, text="Enter device path:").pack(pady=5)

    device_entry = tk.Entry(device_window, width=30)
    device_entry.insert(0, "/dev/hidraw0")
    device_entry.pack(pady=5)

    def save_device_path():
        global devpath
        devpath = device_entry.get()
        if devpath:
            device_window.destroy()
        else:
            tk.messagebox.showerror("Error", "Device path cannot be empty.")

    save_button = tk.Button(device_window, text="SAVE", command=save_device_path, bg="green", fg="white")
    save_button.pack(pady=10)

    cancel_button = tk.Button(device_window, text="CANCEL", command=device_window.destroy, bg="red", fg="white")
    cancel_button.pack(pady=5)

def create_main_menu():
    global main_window
    main_window = tk.Tk()
    main_window.title("DELL Chromebook 11 LED CONTROL PANEL")

    device_button = tk.Button(
        main_window,
        text="SELECT DEVICE",
        command=select_device,
        bg="blue",
        fg="white"
    )
    device_button.pack(pady=10, padx=10, fill=tk.X)

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
    global blink_interval
    color_window = tk.Toplevel()
    color_window.title("CONTROL PANEL OF CANDY LED - BLINK")

    for color in colors:
        fg_color = 'black' if color in ['yellow', 'white'] else 'white'
        button = tk.Button(
            color_window,
            text=color.capitalize(),
            command=lambda c=color: start_blinking(c),
            bg=tk_colors[color],
            fg=fg_color
        )
        button.pack(pady=5, padx=10, fill=tk.X)

    def update_interval(value):
        global blink_interval
        blink_interval = int(value)

    tk.Label(color_window, text="Set Blink Interval (ms):").pack(pady=5)
    interval_slider = tk.Scale(
        color_window,
        from_=100,
        to=2000,
        orient='horizontal',
        length=300,
        command=update_interval
    )
    interval_slider.set(blink_interval)
    interval_slider.pack(pady=5)

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

def start_blinking(color):
    global blink_active
    blink_active = True
    blink_color(color)

if __name__ == "__main__":
    create_main_menu()
