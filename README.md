
# Candy LED
## Introduction
This program allows of control LED indicator on laptop flap. Main code comes from sources. Graphical user interface (GUI) has been made/improved by SI (vibe coding).

* [source code](https://github.com/hgeg/candy-led)
* [idea](https://blog.nanax.fr/post/2018-05-01-chromebook-linux)
* [inspiration](https://forum.endeavouros.com/t/dell-chromebook-3180-activity-light/33895)

## Folders
| folder name |  description |
| ------------- | ------------- |
| const | simple programs to set colour of light  |
| blink  | simple programs to set blinking  |
| gui | gui version of main program |
| other | other staff |

## Colorus
* red
* green
* blue
* yellow
* magenta
* cyan
* white
* black

> [!NOTE]
> Black colour turns off LED indicator.

## Necessary packages
If you want to start the gui version of program, you need a tinker package for python.
* **Debian GNU/Linux**

  ```sh
  sudo apt install python3-tk
  ```
  
* **Arch Linux**

  ```sh
  sudo pacman -S tk
  ```

* **Fedora Linux - The Fedora Project**

  ```sh
  sudo dnf install python3-tkinter
  ```

## How to start a python program?
* **Debian GNU/Linux**
  ```sh
  sudo python3 filename.py
  ```

* **Arch Linux**
  ```sh
  sudo python filename.py
  ```

* **Fedora Linux - The Fedora Project**
  ```sh
  sudo python filename.py
  ```

> [!IMPORTANT]
> After program started (GUI version) you <ins> **have to**</ins> set the devpath (path to the LED indicator in system folders) and <ins> **save it**</ins>.

> [!TIP]
> 1 Hz -> 1000 ms -> 1s

## Issues...
If you have a issue with turing on your LED indicator, you need to change the device in devpath. For example in Arch Linux sometimes after system (packages) update, number of device may change.
Then you need to open the file.py by any text editor and modify 7. line of code, there is ```hidraw``` - you need to change the number to 0 or 1 or 2 or even 3 (maybe).
> [!NOTE]
> In gui version there is special menu to easy set device.

## To do
- [x] make gui
- [ ] eliminate terminal from starting the program

## Screenshots
![screenshot](other/candy_led-screenshot-1.png?raw=true)
![screenshot](other/candy_led-screenshot-4.png?raw=true)
![screenshot](other/candy_led-screenshot-2.png?raw=true)
![screenshot](other/candy_led-screenshot-3.png?raw=true)
