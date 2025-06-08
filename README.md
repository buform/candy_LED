## KOD ŹRÓDŁOWY
* https://github.com/hgeg/candy-led

## POMYSŁ NA PROGRAM
* https://blog.nanax.fr/post/2018-05-01-chromebook-linux

## INSPIRACJA
* https://forum.endeavouros.com/t/dell-chromebook-3180-activity-light/33895

## PROGRAM
Programy są w języku Python, które umożliwiają sterowanie lampką LED na klapie laptopa. Główna część kodu pochodzi ze źródeł. Interfejs graficzny został napisany za pomocą AI (ChatGPT).

Po uruchomieniu programu (wersja GUI) należy ustawić urządzenie (jego położenie w katalogu ```/dev/```). Następnie znajdują się dwie kategorie: ```CONST``` - opcja stałego wyświetlania danego koloru, oraz ```BLINK``` - ustawienie koloru migającego oraz jego częstotliwośći w formie suwaka, jednostką są milisekundy.

1 Hz -> 1000 ms -> 1s

Katalog ```GUI``` zawiera wszystkie wersje rozwojowe interfejsu graficznego. Dodatkowo znajdują się katalogi ```const``` oraz ```blink```, w których są pierwsze, proste wersje programu.

* katalog ```const``` = programy, które powodują ciągłe świecenie się lampki

* katalog ```blink``` = programy, które powodują miganie lampki

* katalog ```gui``` = wersje programów GUI

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

W wersji GUI można wpisać ścieżkę do urządzenia.

W dystrybucji Arch Linux może dochodzić do zmiany numeru urządzenia po aktualizacji systemu.

```/dev/hidraw```

## URUCHOMIENIE
Plik wymaga uprawnień roota do uruchomienia! Polecam używać ```sudo```.
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

## ROZWÓJ
Obecnie planowane jest stworzenie paczki dla systemu Debian GNU/Linux. Problemem jest wykorzystanie ```pkexec```, nie chce współpracować podczas uruchamiania atywatora w DE XFCE.

Przed każdym uruchomieniem skryptu ma wyświetlać się GUI do wpisania hasła aby skrypt miał dostęp do katalogu ```/dev/```. Ma to na celu zastąpienie ręcznego uruchamiania programu w terminalu za każdym razem.
