## KOD ŹRÓDŁOWY
* https://github.com/hgeg/candy-led

* https://blog.nanax.fr/post/2018-05-01-chromebook-linux/#chromebook-keyboard-layout

* https://forum.endeavouros.com/t/dell-chromebook-3180-activity-light/33895

## PROGRAM

Programy w języku Python, który umożliwiają sterowanie lampką LED na klapie laptopa.

katalog const = programy, które powodują ciągłe świecenie się lampki

katalog blink = programy, które powodują miganie lampki

katalog gui = wersje programów GUI

## KOLORY
* czerowny
* zielony
* niebieski
* żółty
* fiolet
* turkus
* biały

Kolor czarny to pozycja wyłączenia lampki LED.

## NIE DZIAŁA
W przypadku braku zaświecenia się lampki należy wejść w plik, w 7. linijce zmienić przy nazwie ```hidraw``` cyfrę na 0 lub 1 lub 2.

W dystrybucji Arch Linux może dochodzić do zmiany numeru urządzenia po aktualizacji systemu.

## URUCHOMIENIE
Plik wymaga uprawnień roota do uruchomienia!
* Debian GNU/Linux
  ```sh
  sudo python3 filename.py
  ```

* Arch Linux
  ```sh
  sudo python filename.py
  ```

* Fedora Linux
  ```sh
  sudo python filename.py
  ```

## GUI
Do uruchomienia pliku ```candy_led_gui.py``` potrzebna jest bibioteka Pythona ```tkinter```.

**INSTALACJA**

* Debian GNU/Linux

  ```sh
  sudo apt install python3-tk
  ```
  
* Arch Linux

  ```sh
  sudo pacman -S tk
  ```

* Fedora Linux

  ```sh
  sudo dnf install python3-tkinter
  ```

Uruchomienie wykonuje się tak samo jak przy podstawowych programach. Dodatkowo GUI obsługuje ciągłe świecenie się lampki oraz miganie.
