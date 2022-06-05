import setuptools
import os

# TODO: figure out a way to differentiate between modules for pip install
# config_var_raspi = os.environ.get("ISM330DHCX_INSTALL", None)

NAME_FTDI = 'ISM330DHCX_FTDI_SPI'
VERSION_FTDI = '0.1.0'
AUTHOR = 'wrh2'
DESCRIPTION = 'Highly configurable ISM330DHCX module for Python'
PACKAGES_FTDI = ['ISM330DHCX_FTDI_SPI']
INSTALL_REQUIRES_FTDI = ['pyftdi >= 0.54.0']
PYTHON_REQUIRES_FTDI = '>=3.7'

name_to_install = NAME_FTDI
version_to_install = VERSION_FTDI
packages_to_install = PACKAGES_FTDI
install_requires_install = INSTALL_REQUIRES_FTDI
python_requires_install = PYTHON_REQUIRES_FTDI

# if config_var_raspi:
#     print('Raspi')
#     # change to raspi package
#     pass

setuptools.setup(
    name = name_to_install,
    version = version_to_install,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = packages_to_install,
    install_requires = install_requires_install,
    python_requires = python_requires_install
)