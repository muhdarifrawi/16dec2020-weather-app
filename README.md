# Weather Application for Raspberry Pi (RPi) Zero W
## Preface
This project is just a small hobby project that I will be creating for my girlfriend. 
The Goal of this was to create a weather app that would link to Singapore's weather API 
and change the LED lights attached to the RPi to warmer colours in colder weathers and 
cooler colours in warmer weathers. 

## Pre-requisites
Other than having the knowledge in Python, HTML, CSS and JavaScript, it would be better 
for anyone to have some level of knowledge to tinker stuff. If you have ever worked with RPi 
or have an engineering background, I think this project would be too simple for you. 

Coding Languages:
- Python
- HTML
- CSS
- JavaScript

Softwares:
- Visual Studio Code (VSC). I primarily use this editor to code.
- Anaconda. To isolate Python environments.
- RPi debian. You can buy this off shelf or download it from RPi main webpage. Make sure to update the softwares and stuff in it on first usage. Read more here: [Updating and upgrading Raspberry Pi OS](https://www.raspberrypi.org/documentation/raspbian/updating.md).

Hardwares:
- [RPi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/]. You can get the WH as well. It's the same just that WH comes with the pin Headers.
- [PiTFT Capacitive Screen](https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi). You can use any other screens you like. I preferred this.
- LED lights of your choice.

Optional Items:
- [RPi power plug](https://www.raspberrypi.org/products/raspberry-pi-universal-power-supply/). I highly recommend getting one so that it gets constant stable power. 
- [Mini HDMI cable or Mini HDMI convertor](https://tethertools.com/blog/what-are-hdmi-hdmi-mini-hdmi-micro-cables/). The RPi Zero W uses Mini HDMI as an output.
- [Micro USB](https://www.androidauthority.com/different-types-of-usb-cables-804432/) to USB converter. To use your mouse on your RPi Zero.

**IMPORTANT NOTE: I do not make any profit from anything you purchase**


## Initial Setup
Before you put in any codes into the RPi, update the RPi by following the instructions here: [Updating and upgrading Raspberry Pi OS](https://www.raspberrypi.org/documentation/raspbian/updating.md).

Once you have achieved that, setup the PiTFT screen by following the instructions here: [PiTFT Capacitive Easy Install](https://learn.adafruit.com/adafruit-2-8-pitft-capacitive-touch/easy-install-2).

To be able to display the RPi GUI, you would need to follow the instructions on `FBCP Install Commands`. Make your life easier, copy that title and find it in the webpage. It should work like a charm. From my experience, it's harder to do the interactive installation.