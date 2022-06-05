from ISM330DHCX import ISM330DHCX_FTDI_SPI
import unittest

class TestISM330DHCX_FTDI_SPI(unittest.TestCase):
    def test_who_am_i(self):
        ISM330DHCX_WHO_AM_I_VAL = 0x6b
        imu = ISM330DHCX_FTDI_SPI()
        self.assertEqual(imu.whoAmI, ISM330DHCX_WHO_AM_I_VAL)

    def test_acc_enabled(self):
        imu = ISM330DHCX_FTDI_SPI(enable_xl=True)
        self.assertEqual(imu.accEnabled, True)

    def test_acc_disabled(self):
        imu = ISM330DHCX_FTDI_SPI(enable_xl=True)
        imu.disableAcc()
        self.assertEqual(imu.accEnabled, False)

    def test_gyro_enabled(self):
        imu = ISM330DHCX_FTDI_SPI(enable_gyro=True)
        self.assertEqual(imu.gyroEnabled, True)

    def test_gyro_disabled(self):
        imu = ISM330DHCX_FTDI_SPI(enable_gyro=True)
        imu.disableGyro()
        self.assertEqual(imu.gyroEnabled, False)

if __name__ == '__main__':
    unittest.main()