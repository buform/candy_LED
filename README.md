## KOD ŹRÓDŁOWY
https://github.com/hgeg/candy-led


## DELL 3120 Chromebook

Programy w języku Python, który umożliwiają sterowanie lampką LED na klapie laptopa.

katalog const = programy, które powodują ciągłe świecenie się lampki

katalog blink = programy, które powodują miganie lampki

## KOLORY
* czerowny
* zielony
* niebieski
* żółty
* fiolet
* turkus
* biały

## NIE DZIAŁA
W przypadku braku zaświecenia się lampki należy wejść w plik i w 7. linijce zmienić przy nazwie hidraw cyfrę na 0 / 1 / 2.

W dystrybucji Arch Linux może dochodzić do zmiany numeru urządzenia po aktualizacji.

## URUCHOMIENIE
* Debian GNU/Linux

  ```$ sudo python3 filename.py```
* Arch Linux

  ```$ sudo python filename.py```
* Fedora Linux

  powinno działać ale nie było sprawdzane

## PRZYSZŁOŚĆ
Planowane jest stworzenie GUI!
