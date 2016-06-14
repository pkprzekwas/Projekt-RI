# Projekt-Robot z systemem wizyjnym

![alt tag](https://github.com/pkprzekwas/Projekt-RI/blob/master/Resources/robot.jpg)

##Obecne zespoły i liderzy:

* Sterowanie - Jakub Dębksi, Filip Dąbrowski
* Joystick - Anna Knap, Piotr Kopa-Ostrowski
* Komunikacja - Patryk Przekwas, Adam Grzybkowski
* Przetwarzanie obrazu - Michał Żygowski, Wojciech Tokarski, Maciek Porzeżyński

Finał naszej pracy znajduję się w folderze Release.

##Przewodnik po plikach:

Katalog 'Release' zawiera trzy podfoldery:
* ArduinoApp - aplikacje na arduino (są 2 - jedna do płytki sterującej robotem druga do płytki obsługującej Nunchuck od Wii)
* PcApp - aplikacja na komputer sterująca robotem za pomocą joysticka (Tu jest moduł komunikacji i joysticka)
* RaspberryApp - najważniejszy podfolder z podzielonymi na funkcjonalności modułami
  1. JoystickDriven - Aplikacja do zdalnej jazdy robotem (używa modułu komunikacji)
  2. CamPreview - Czysty podgląd z kamery
  3. KeyboardDriven - Sterowanie strzałkami z klawiatury komputera (pierwsze demo-używa jeszcze innego modułu komunikacji)
  4. SelfDriven - Główna aplikacja, czyli robot jadący sam przez korytarz 


