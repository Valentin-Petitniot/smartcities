# Projet Smartcities
## Contexte
Dans le cadre du cours de SmartCities & IoT, je dois réaliser différents petits projets qui ont pour objectif de me faire apprendre la programation embarqué en MicroPython.
Chaque projet se focalise sur un aspect bien précis, que ce soit l'emploi de méthodes de programmations différentes ou bien l'utilisation de divers composant tel que des moteurs, des buzzers, des potentiomètre, etc.

Les différents projet seront réalisé grâce à un kit de base Grove avec un Raspberry Pico W. 

## Répertoires
* [GPIO](GPIO)
* [AD-PWM](AD-PWM)
* [LCD](LCD)
* [LED-neo](LED-neo)
* [Network](Network)
* [Sensors](Sensors)

## Raspberry Pico W
Les Rapsberry Pico sont des micro-contrôleurs performant, ultra-léger et ultra-petit, ce qui en fait une solution idéal pour des projets de systèmes embarqués. Les Raspberry Pico embarque avec eux une multitude de pins et de connectivités différentes, les rendants très versatiles.
La spécificité du Raspberry Pico W est la présence d'une carte réseau ajoutant la dimension du réseau (WiFi ou Bluetooth) à la programmation sur micro-contrôleur.

### Pinout
![image](https://github.com/user-attachments/assets/4c444b69-47da-4f1a-ac3e-855ae2b69477)

## MicroPython
![image](https://github.com/user-attachments/assets/965a52dc-9101-4415-afc2-8dc6255b54ba)

Il s'agit d'une implémentation du language de programmation Python3 incluant une partie des librairie standard du Python et qui est optimisé pour fonctionner sur des micro-contrôleur.

MicroPython fournit un ensemble de modules spécifique au MicroPython pour faciliter l'utilisation des fonctionnalités et des périphériques comme les GPIOs, Timers, ADC, DAC, PWM, SPI, I²C, CAN, Bluetooth, et l'USB.

Dans le cadre de ce cours, je vais travailler sur un Raspberry Pico mais d'autres micro-contrôleur peuvent fonctionner avec le MicroPython. Les series ESP32 et ESP82 ainsi que les Arduino UNO peuvent être programmé en dans ce language.

## Visual Studio Code
![image](https://github.com/user-attachments/assets/684ad0a1-ee89-4bb7-978f-421cde276259)

Visual Studio Code est un IDE léger qui permet de programmer dans presque tous les languages de programmation existant. Grâce à sa communauté pro-active, VSCode peut se targer d'avoir l'une des plus grande bibliotèque d'extensions, le rendant ultra-modulable au besoin de chaque programmeur.

### MicroPico
MicroPico Visual Studio Code Extension est un extension de Visual Studio Code conçue par [https://github.com/paulober](#paulober) afin de simplifier et accélérer la développement des projets MicroPython sur Raspberry Pi Pico et Pico W. 

Cette extension ajoute le highlighting, auto-completion, code snippets, une intégration au terminal pour communiquer avec le Raspberry.



