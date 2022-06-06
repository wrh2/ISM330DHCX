from ISM330DHCX_FTDI_SPI import ISM330DHCX_FTDI_SPI
import unittest

class TestISM330DHCX_FTDI_SPI(unittest.TestCase):
    def test_who_am_i(self):
        ISM330DHCX_WHO_AM_I_VAL = 0x6b
        imu = ISM330DHCX_FTDI_SPI()
        self.assertEqual(imu.whoAmI, ISM330DHCX_WHO_AM_I_VAL)

    def test_acc_enabled_init(self):
        imu = ISM330DHCX_FTDI_SPI(enable_xl=True)
        self.assertEqual(imu.accEnabled, True)

    def test_acc_enabled_after_init(self):
        imu = ISM330DHCX_FTDI_SPI()
        imu.enableAcc()
        self.assertEqual(imu.accEnabled, True)

    def test_acc_interrupt_enabled_init(self):
        imu = ISM330DHCX_FTDI_SPI(enable_xl=True, enable_xl_interrupt=True, xl_interrupt_pin='INT1')
        self.assertEqual(imu.accInterruptEnabled, True)
        self.assertEqual(imu.accInterruptPin, 'INT1')

    def test_acc_interrupt_enabled_after_init(self):
        imu = ISM330DHCX_FTDI_SPI(enable_xl=True)
        imu.enableAccInterrupt('INT1')
        self.assertEqual(imu.accInterruptEnabled, True)
        self.assertEqual(imu.accInterruptPin, 'INT1')

    def test_acc_interrupt_disable(self):
        imu = ISM330DHCX_FTDI_SPI(enable_xl=True, enable_xl_interrupt=True, xl_interrupt_pin='INT1')
        imu.disableAccInterrupt()
        self.assertEqual(imu.accInterruptEnabled, False)

    def test_acc_disabled(self):
        imu = ISM330DHCX_FTDI_SPI(enable_xl=True)
        imu.disableAcc()
        self.assertEqual(imu.accEnabled, False)

    def test_gyro_enabled_init(self):
        imu = ISM330DHCX_FTDI_SPI(enable_gyro=True)
        self.assertEqual(imu.gyroEnabled, True)

    def test_gyro_enabled_after_init(self):
        imu = ISM330DHCX_FTDI_SPI()
        imu.enableGyro()
        self.assertEqual(imu.gyroEnabled, True)

    def test_gyro_interrupt_enabled_init(self):
        imu = ISM330DHCX_FTDI_SPI(enable_gyro=True, enable_gyro_interrupt=True, gyro_interrupt_pin='INT1')
        self.assertEqual(imu.gyroInterruptEnabled, True)
        self.assertEqual(imu.gyroInterruptPin, 'INT1')

    def test_gyro_interrupt_enabled_after_init(self):
        imu = ISM330DHCX_FTDI_SPI(enable_gyro=True)
        imu.enableGyroInterrupt('INT1')
        self.assertEqual(imu.gyroInterruptEnabled, True)
        self.assertEqual(imu.gyroInterruptPin, 'INT1')

    def test_gyro_interrupt_disable(self):
        imu = ISM330DHCX_FTDI_SPI(enable_gyro=True, enable_gyro_interrupt=True, gyro_interrupt_pin='INT1')
        imu.disableGyroInterrupt()
        self.assertEqual(imu.gyroInterruptEnabled, False)

    def test_gyro_disabled(self):
        imu = ISM330DHCX_FTDI_SPI(enable_gyro=True)
        imu.disableGyro()
        self.assertEqual(imu.gyroEnabled, False)

if __name__ == '__main__':
    unittest.main()