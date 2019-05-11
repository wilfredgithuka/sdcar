Wilfred Githuka RC Self Driving Car
Project Documentation

## Project Structure
![image](https://raw.githubusercontent.com/wilfredgithuka/sdcar/master/struct.png)

## Project Objectives
* Learn how to design a working autonomous vehicle
* Implement a deep neural network that will drive the vehicle
* Adjust parameters to improve vehicle performance
* Implement various algorithms that drive autonomous vehicles
* Have fun.

## Project Deliverables
* A fully autonomous vehicles
* Deep learning models

## Project Timeline
* May 2018 Programming
* June 2019 Testing of various neural networks
* July 2019 Testing and more testing

## Vehicle Details
* Wheels: 4
* Weight: 900g
* Power SOurce: Power Bank 5V 1.2A LiPo Battery 2200mAh 7.4V 30C
* Control: Raspbery Pi 2 Model B

## IIC BUS

I2C (Inter-Intergrated Ciruit) is a serial protocol for 2 wire interface to connect low speed devices like microcontrollers,
EEPROMS, Analogue-Digital and Digital-Analogue converters, I/O interfaces and other peripheral
embeeded systems.

The I²C bus was developed in 1982; its original purpose was to provide an easy way to connect a CPU to peripherals chips in a TV set.
Peripheral devices in embedded systems are often connected to the microcontroller as memory-mapped I/O devices. One
common way to do this is connecting the peripherals to the microcontroller parallel address and data busses.

This results in lots of wiring on the PCB (printed circuit board) and additional ‘glue logic’ to decode the address bus on which
all the peripherals are connected. In order to spare microcontroller pins, additional logic and make the PCBs simpler – in order
words, to lower the costs – Philips labs in Eindhoven (The Netherlands) invented the ‘Inter-Integrated Circuit’, IIC or I²C protocol
that only requires 2 wires for connecting all the peripheral to a microcontroller.

The original specification defined a bus speed of 100 kbps (kilo bits per second). The specification was reviewed several times,
notably introducing the 400 kbps speed in 1995 and – since 1998, 3.4 Mbps for even faster peripherals.

![i2c-image](https://www.byteparadigm.com/pictures/figure4.jpg)

I2C bus protocol is simple beacause there can be more than one master, also only upper bus speed and only
2 wires with pull up resistors are needed to connect almost unlimited number of I2C devices.

Each device has a unique address. Transfer to and fro master device is serial and its split into 8 packets.

I2C uses only 2 wires:

* SCL - Serial Clock
* SDA - Serial Data

Both need to be pulled up with a resistor to +Vdd. There are also I2C **Level Shifters** which can be used to
connect to 2 I2C busses with different voltages.

### I2C Principle of Operation

First, the master will issue a START condition. This acts as an ‘Attention’ signal to all of the connected devices.
All ICs on the bus will listen to the bus for incoming data.

Then the master sends the ADDRESS of the device it wants to access, along with an indication whether the access
is a Read or Write operation (Write in our example). Having received the address, all IC’s will compare it
with their own address. If it doesn’t match, they simply wait until the bus is released by the stop condition.
If the address matches, however, the chip will produce a response called the ACKNOWLEDGE signal.

Once the master receives the acknowledge, it can start transmitting or receiving DATA. In our case, the master will transmit data.
When all is done, the master will issue the STOP condition. This is a signal that states the bus has been released and
that the connected ICs may expect another transmission to start any moment.

When a master wants to receive data from a slave, it proceeds the same way, but sets the RD/nWR bit at a logical one.
Once the slave has acknowledged the address, it starts sending the requested data, byte by byte. After each data byte,
it is up to the master to acknowledge the received data.

### I2C Evolution

* Version 0 - 100kHz
* Version 1 - Fast mode 400kHz, 10 bit addressing
* Version 2 - High Speed 3.4 mHz
* Version 3 - Fast Mode +
* Version 4 - Ultrafast mode 5 mHz
* Version 5 - Correction
* Version 6 - Correction

## Raspberry Pi  - Arduino Handshake

To enable the pi speak to the arduino, we first need to do some configuration to each before proceeded to initiate the handshake.

### Enabling I2C and raspi-config menu

##### Installing required packages

```
sudo pacman -Syy i2c-tools python-pip
```
##### Install Rpi.GPIO

```
sudo pip install Rpi.GPIO
```

##### Install raspi-config menu

```
sudo pacman -S xorg-xrandr libnet
git clone https://aur.archlinux.org/raspi-config.git
cd raspi-config
makepkg -i
```

##### Use Rpi-config tool to enable I2C

```
sudo taspi-config
Select Interfacing Options to enable I2C
sudo reboot
```
##### Test the I2C setup

```
sudo i2cdetect -y 1
```
##### Now just connect an I2C device, be it an arduino or whatever device you wish and you should get a hex address of where the device may be found. Finally install the following python tools which shall come in handy.

```
yay python-smbus
```
### Arduino Configuration

##### Install Arduino and related packages

```
sudo pacman -S arduino arduino-docs arduino-avr-core
```
##### Add yourself to the uucp and lock user groups

```
sudo gpasswd -a wilfred uucp
sudo gpasswd -a wilfred lock
```

##### Users and rights in the above groups (optional)

```
sudo usermod -a -G uucp wilfred
sudo usermod -a -G lock wilfred
```
##### Load the cdc_acm module

```
sudo modrobe cdc_acm
```
##### Reboot

### Configuring Arduino as a SLAVE device for I2C

To do this I define an address for the slave which shall be 4. Then I define callback fuctions for dending data and receiving it.
When the arduino receives a digit it acknowledges it and resends it back to the pi. If the digits happens to be 1 it shall switch
on an LED.

### Configuring Pi as a MASTER Device for I2C

This is just a python program that asks you to enter a digit which it sends back to the arduino, the arduino acknowledges the data
which it resends back.

## References

* [i2C Infosite](https://i2c.info)
* [Byte Paradigm](https://www.byteparadigm.com/applications/introduction-to-i2c-and-spi-protocols/)
* [OscarLiang](https://oscarliang.com/raspberry-pi-arduino-connected-i2c/)
