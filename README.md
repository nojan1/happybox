Happybox
=========

# 1. Getting up and running

To start using the happybox you need to connect it to a network (1.1) (internet access may or may not be requried). You may then need to write an implementation that takes the data from the buttons and forwards it to an external service (1.2).

## 1.1 Wifi
To configure the wifi create a file called `wpa_supplicant.conf` on the SD-Card boot partition (FAT32). 

Enter the following:
```
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 scan_ssid=1
 ssid="RouterName"
 psk="Security"
}
```

The example is for a standard WPA2-PSK network. For more exotic networks, refer to the wpa_supplicant man page.

## 1.2 Actual implementation

By default 

# 2 Hardware

The hardware inside the happybox is consists of a Raspberry Pi Zero W which acts as the brain.

To this the following things are connected:
 * Four buttons
 * Four 16 pixel Neopixel rings

# 3 Software

The base software is written in python using the Adafruit CircuitPython libraries to interface with the Pi hardware pins. 

To control the Neopixel rings it utilises the rpi_ws281x library by jgarff. This library makes use of the Pi's PWM and DMA functionality to handle the complex timing required.

The software is programmed to react to button presses from the four "happiness" buttons and to the forward this to an external service. See section 1.2 for more information about where the data ends up.

# 4 Setting up from scratch

These instructions are usefull if you have an blank SD-Card and wish to get Happybox up and running.

## 4.1 Install Rasbian

Install Rasbian according to instructions on the [official page](https://www.raspberrypi.org/documentation/installation/installing-images/README.md).

After install setup Wifi (section 1.1), SSH and/or Serial access.

### 4.1.1 Enabling SSH

Create a file called `ssh` on the "/boot" partition. This will automatically enable the SSH server on first startup.

You can now use a SSH-client like Putty to connect.

### 4.2.1 Enable serial terminal

Access to the pi can be made without networking by instead using an old school serial terminal. Please note that this requires use of a **3,3v** UART adapter.

Enable the serial console functionality by adding the following line to the file `/boot/config.txt`.

```
enable_uart=1
```

After this make sure that the line `serial0,11520` appears in the file `/boot/cmdline.txt`

You can now connect the UART adapter by attaching the pins according to the table below:

| UART Pin | Pi pin number |
|----------|---------------|
| GND  | 6  |
| RX  | 8   |
| TX  | 10  |

Connect USB-power to the PI and connect using a serial terminal on the correct port with a baudrate of 11520.

## 4.2 Installing Dependencies

Run the commands below to install python and all reguired dependencies.

```
sudo apt-get install python3 python3-pip git scons python3-dev swig
sudo pip3 install RPI.GPIO
sudo pip3 install adafruit-circuitpython-neopixel 
```

The following commands installs the library required for Neopixels to work.

```
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons
cd python
python3 ./setup.py build
sudo python3 ./setup.py install
```
## 4.3 Setting up the happybox software

```
git clone https://github.com/nojan1/happybox.git
cd happybox/Root
sudo cp -R * /
sudo systemctl enable happybox
sudo systemctl start happybox
```