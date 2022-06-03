from ISM330DHCX import ISM330DHCX_FTDI_SPI
import unittest

class TestISM330DHCX_FTDI_SPI(unittest.TestCase):
    def test_who_am_i(self):
        ISM330DHCX_WHO_AM_I_VAL = 0x6b
        imu = ISM330DHCX_FTDI_SPI()
        self.assertEqual(imu.whoAmI, ISM330DHCX_WHO_AM_I_VAL)

if __name__ == '__main__':
    unittest.main()