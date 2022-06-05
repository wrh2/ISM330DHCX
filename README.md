# ISM330DHCX

Highly configurable ISM330DHCX module for Python. Developed with Python3, FTDI FT2232H Mini Module (requires Python3 v3.7+), and Raspberry Pi (requires Python3 v3.4+). Includes unit tests and examples.

## Materials Used

* [FT2232H Mini Module](https://ftdichip.com/products/ft2232h-mini-module/)
* [Raspberry Pi 3B+](https://www.sparkfun.com/products/15361)
* [STEVAL-MKI207V1](https://www.st.com/en/evaluation-tools/steval-mki207v1.html)

## Dependencies

### For Raspberry Pi
- [py-smbus](https://github.com/pimoroni/py-smbus)
- [spidev](https://pypi.org/project/spidev/)

### For FTDI Mini Module
- [PyFtdi](https://eblot.github.io/pyftdi/)

## Features

* Independent use of Accelerometer and Gyro
* Support for I2C or SPI for Raspberry Pi and FTDI FT2232H Mini Module
* 2g, 4g, 8g, 16g scales for Accelerometer
* 250DPS, 500DPS, 1000DPS, 2000DPS scales for Gyro

## Installation

### FTDI Mini Module

cd to modules folder then

```pip3 install .```

## Examples

### FTDI Mini Module

Simple [polling example](./modules/ISM330DHCX_FTDI_SPI/examples/example_poll.py) provided

## Tests

### FTDI Mini Module

A [unit test for the module using python's unittest module](./modules/ISM330DHCX_FTDI_SPI/tests/tests.py) is included.

## TODO

* Finish raspberry pi support
* Finish I2C support for FTDI
* Configure interrupts
* Embedded functions
* Support for daisy chaining
* Clean up packaging for PyPi