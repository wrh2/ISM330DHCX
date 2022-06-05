from pyftdi.spi import SpiController
from ctypes import c_int16

ISM330DHCX_Registers = {
    'FUNC_CFG_ACCESS': 0x1,
    'PIN_CTRL': 0x2,
    'FIFO_CTRL1': 0x7,
    'FIFO_CTRL2': 0x8,
    'FIFO_CTRL3': 0x9,
    'FIFO_CTRL4': 0xA,
    'COUNTER_BDR_REG1': 0xB,
    'COUNTER_BDR_REG2': 0xC,
    'INT1_CTRL': 0xD,
    'INT2_CTRL': 0xE,
    'WHO_AM_I': 0xF,
    'CTRL1_XL': 0x10,
    'CTRL2_G': 0x11,
    'CTRL3_C': 0x12,
    'CTRL4_C': 0x13,
    'CTRL5_C': 0x14,
    'CTRL6_C': 0x15,
    'CTRL7_G': 0x16,
    'CTRL8_XL': 0x17,
    'CTRL9_XL': 0x18,
    'CTRL10_C': 0x19,
    'ALL_INT_SRC': 0x1A,
    'WAKE_UP_SRC': 0x1B,
    'TAP_SRC': 0x1C,
    'D6D_SRC': 0x1D,
    'STATUS_REG': 0x1E,
    'OUT_TEMP_L': 0x20,
    'OUT_TEMP_H': 0x21,
    'OUTX_L_G': 0x22,
    'OUTX_H_G': 0x23,
    'OUTY_L_G': 0x24,
    'OUTY_H_G': 0x25,
    'OUTZ_L_G': 0x26,
    'OUTZ_H_G': 0x27,
    'OUTX_L_A': 0x28,
    'OUTX_H_A': 0x29,
    'OUTY_L_A': 0x2A,
    'OUTY_H_A': 0x2B,
    'OUTZ_L_A': 0x2C,
    'OUTZ_H_A': 0x2D,
    'EMB_FUNC_STATUS_MAINPAGE': 0x35,
    'FSM_STATUS_A_MAINPAGE': 0x36,
    'FSM_STATUS_B_MAINPAGE': 0x37,
    'MLC_STATUS_MAINPAGE': 0x38,
    'STATUS_MASTER_MAINPAGE': 0x39,
    'FIFO_STATUS1': 0x3A,
    'FIFO_STATUS2': 0x3B,
    'TIMESTAMP0': 0x40,
    'TIMESTAMP1': 0x41,
    'TIMESTAMP2': 0x42,
    'TIMESTAMP3': 0x43,
    'TAP_CFG0': 0x56,
    'TAP_CFG1': 0x57,
    'TAP_CFG2': 0x58,
    'TAP_THS_6D': 0x59,
    'INT_DUR2': 0x5A,
    'WAKE_UP_THS': 0x5B,
    'WAKE_UP_DUR': 0x5C,
    'FREE_FALL': 0x5D,
    'MD1_CFG': 0x5E,
    'MD2_CFG': 0x5F,
    'INTERNAL_FREQ_FINE': 0x63,
    'INT_OIS': 0x6F,
    'CTRL1_OIS': 0x70,
    'CTRL2_OIS': 0x71,
    'CTRL3_OIS': 0x72,
    'X_OFS_USR': 0x73,
    'Y_OFS_USR': 0x74,
    'Z_OFS_USR': 0x75,
    'FIFO_DATA_OUT_TAG': 0x78,
    'FIFO_DATA_OUT_X_L': 0x79,
    'FIFO_DATA_OUT_X_H': 0x7A,
    'FIFO_DATA_OUT_Y_L': 0x7B,
    'FIFO_DATA_OUT_Y_H': 0x7C,
    'FIFO_DATA_OUT_Z_L': 0x7D,
    'FIFO_DATA_OUT_Z_H': 0x7E,
}

ISM330DHCX_Embedded_Function_Registers = {

}

ISM330DHCX_Output_Data_Rates = {
    'ODR_POWER_DOWN': 0,
    'ODR_1_6HZ': 0xB, # Only works when high performance mode disabled
    'ODR_12_5HZ': 0x1,
    'ODR_26HZ': 0x2,
    'ODR_52HZ': 0x3,
    'ODR_104HZ': 0x4,
    'ODR_208HZ': 0x5,
    'ODR_416HZ': 0x6,
    'ODR_833HZ': 0x7,
    'ODR_1_66KHZ': 0x8,
    'ODR_3_33KHZ': 0x9,
    'ODR_6_66KHZ': 0xA,
}

ISM330DHCX_Scale_Selection = {
    'SCALE_2G': (0, 2),
    'SCALE_16G': (1, 16),
    'SCALE_4G': (2, 4),
    'SCALE_8G': (3, 8),
}

ISM330DHCX_DEFAULT_FTDI_SPI_INTERFACE_NUM = '1'
ISM330DHCX_DEFAULT_SPI_BITRATE = int(1e6)
ISM330DHCX_MAX_SPI_BITRATE = int(10e6)
ISM330DHCX_DEFAULT_ODR = ISM330DHCX_Output_Data_Rates['ODR_416HZ']
ISM330DHCX_DEFAULT_SCALE_SELECTION = ISM330DHCX_Scale_Selection['SCALE_8G']
ISM330DHCX_DEFAULT_XL_SENSITIVITY = .061 * 1e-3 #mg/LSB
ISM330DHCX_DEFAULT_GYRO_SENSITIVITY = 4.375 * 1e-3 # mdps/LSB


class ISM330DHCX_FTDI_SPI(SpiController):

    def __init__(self, cs_count: int = 1, turbo: bool = True, ftdi_interface_num: str = ISM330DHCX_DEFAULT_FTDI_SPI_INTERFACE_NUM, bitrate: int = ISM330DHCX_DEFAULT_SPI_BITRATE,
                       enable_xl: bool = False, odr_xl: int = ISM330DHCX_DEFAULT_ODR, scale_xl: int = ISM330DHCX_DEFAULT_SCALE_SELECTION, sensitivity_xl: float = ISM330DHCX_DEFAULT_XL_SENSITIVITY,
                       enable_gyro: bool = False, odr_gyro: int = ISM330DHCX_DEFAULT_ODR, scale_gyro: int = ISM330DHCX_DEFAULT_SCALE_SELECTION, sensitivity_gyro: float = ISM330DHCX_DEFAULT_GYRO_SENSITIVITY):

        super().__init__(cs_count, turbo)

        if ftdi_interface_num != '1' and ftdi_interface_num != '2':
            raise ValueError('ftdi_interface_num invalid')

        self.configure('ftdi:///' + ftdi_interface_num)

        ISM330DHCX_DEFAULT_PYFTDI_SPI_MODE = 3
        self.__slave = self.get_port(0, freq=bitrate, mode=ISM330DHCX_DEFAULT_PYFTDI_SPI_MODE)

        self.__setupRegisterMap()
        self.__getWhoAmI()

        self.__acc_enabled = False
        self.__gyro_enabled = False

        if enable_xl:
            self.__setupXL(odr_xl, scale_xl)

        if enable_gyro:
            self.__setupGyro(odr_gyro, scale_gyro)


    def __setupRegisterMap(self):
        
        # register map for LSM6DS3
        self.__regs = ISM330DHCX_Registers

        # embedded function registers for LSM6DS3
        self.__embed_func_regs = ISM330DHCX_Embedded_Function_Registers

    def __writeRegister(self, reg, d):
        msg = [reg]
        to_send = msg + d
        #print(len(to_send))
        #self.__slave.exchange(to_send, len(to_send))
        self.__slave.exchange(to_send)

    def __readRegister(self, reg, l):
        READ_BIT = 1
        READ_BIT_SHIFT = 7
        msg = [(READ_BIT << READ_BIT_SHIFT) | reg]
        return self.__slave.exchange(msg, l)

    def __getWhoAmI(self):
        whoAmIRegisterAddress = self.__regs['WHO_AM_I']
        whoAmIReadLength = 1
        self.__whoAmI = self.__readRegister(whoAmIRegisterAddress, whoAmIReadLength)[0] # turn bytearray to int

    def __setupXL(self, odr, scale):
        ctrl1XLRegisterAddress = self.__regs['CTRL1_XL']
        ODR_XL_SHIFT = 4
        FS_XL_SHIFT = 2
        ctrl1XLSetting = (odr << ODR_XL_SHIFT) | (scale[0] << FS_XL_SHIFT)
        d = [ctrl1XLSetting]
        self.__writeRegister(ctrl1XLRegisterAddress, d)
        if self.__readRegister(ctrl1XLRegisterAddress, 1)[0] == ctrl1XLSetting:
            self.__acc_enabled = True
            self.__odr_xl = odr
            self.__scale_xl = scale

    def __powerDownXL(self):
        ctrl1XLRegisterAddress = self.__regs['CTRL1_XL']
        ODR_XL_SHIFT = 4
        FS_XL_SHIFT = 2
        if self.__acc_enabled:
            ctrl1XLSetting = (0x0 << ODR_XL_SHIFT) | (self.__scale_xl[0] << FS_XL_SHIFT)
            d = [ctrl1XLSetting]
            self.__writeRegister(ctrl1XLRegisterAddress, d)
            if self.__readRegister(ctrl1XLRegisterAddress, 1)[0] == ctrl1XLSetting:
                self.__acc_enabled = False

    def __setupGyro(self, odr, scale):
        pass

    def __getStatusRegister(self):
        statusRegisterAddress = self.__regs['STATUS_REG']
        return self.__readRegister(statusRegisterAddress, 1)

    def __getDataXLX(self):
        outXRegisterAddress = self.__regs['OUTX_L_A']
        return self.__readRegister(outXRegisterAddress, 2)

    def __getDataXLY(self):
        outXRegisterAddress = self.__regs['OUTY_L_A']
        return self.__readRegister(outXRegisterAddress, 2)

    def __getDataXLZ(self):
        outXRegisterAddress = self.__regs['OUTZ_L_A']
        return self.__readRegister(outXRegisterAddress, 2)

    def __calcAccData(self, d):
        return c_int16(d).value*ISM330DHCX_DEFAULT_XL_SENSITIVITY*(self.__scale_xl[1] >> 1)*9.81

    def disableAcc(self):
        self.__powerDownXL()

    def getAccDataX(self, raw=False):
        result = None
        if self.__acc_enabled:
            result = self.__getDataXLX()
            if not raw:
                result = self.__calcAccData(result[1] << 8 | result[0])
        return result

    def getAccDataY(self, raw=False):
        result = None
        if self.__acc_enabled:
            result = self.__getDataXLY()
            if not raw:
                result = self.__calcAccData(result[1] << 8 | result[0])
        return result

    def getAccDataZ(self, raw=False):
        result = None
        if self.__acc_enabled:
            result = self.__getDataXLZ()
            if not raw:
                result = self.__calcAccData(result[1] << 8 | result[0])
        return result

    def getAccDataXYZ(self, raw=False):
        result = None
        if self.__acc_enabled:
            result_x = self.__getDataXLX()
            result_y = self.__getDataXLY()
            result_z = self.__getDataXLZ()
            result = result_x + result_y + result_z
            if not raw:
                result = [self.__calcAccData(result_x[1] << 8 | result_x[0]),
                        self.__calcAccData(result_y[1] << 8 | result_y[0]),
                        self.__calcAccData(result_z[1] << 8 | result_z[0])]
        return result

    def getStatus(self):
        return self.__getStatusRegister()

    @property
    def whoAmI(self):
        return self.__whoAmI
    
    @property
    def accEnabled(self):
        return self.__acc_enabled