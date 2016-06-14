# Projekt-Robot z systemem wizyjnym

Obecne zespoły i liderzy:

* Sterowanie - Jakub Dębksi, Filip Dąbrowski
* Joystick - Anna Knap, Piotr Kopa-Ostrowski
* Komunikacja - Patryk Przekwas, Adam Grzybkowski
* Przetwarzanie obrazu - Michał Żygowski, Wojciech Tokarski, Maciek Porzeżyński

Finał naszej pracy znajduję się w folderze Release i z nim powinniście się zapoznać do piątku.

w skrócie:

Są 3 podfoldery:
* ArduinoApp - aplikacje na arduino (są 2 - jedna do płytki sterującej robotem druga do płytki obsługującej Nunchuck od Wii)
* PcApp - aplikacja na komputer sterująca robotem za pomocą joysticka (Tu jest moduł komunikacji i joysticka)
* RaspberryApp:
** JoystickApp.py - Aplikacja do zdalnej jazdy robotem (używa modułu komunikacji)
** cameraPrevievApp.py - Czysty podgląd z kamery
** keyboardApp.py - Sterowanie strzałkami z klawiatury komputera (pierwsze demo-używa jeszcze innego modułu komunikacji)
** selfDriveApp.py - Główna aplikacja, czyli robot jadący sam przez korytarz 


