from pyftdi.spi import SpiController

ISM330DHCX_DEFAULT_BITRATE = int(1e6)

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

class ISM330DHCX_FTDI_SPI(SpiController):

    def __init__(self, cs_count: int = 1, turbo: bool = True, bitrate: int = ISM330DHCX_DEFAULT_BITRATE):
        super().__init__(cs_count, turbo)
        self.configure('ftdi:///1')

        ISM330DHCX_DEFAULT_PYFTDI_SPI_MODE = 3
        self.__slave = self.get_port(0, freq=bitrate, mode=ISM330DHCX_DEFAULT_PYFTDI_SPI_MODE)

        self.__setupRegisterMap()
        self.__getWhoAmI()

    def __setupRegisterMap(self):
        
        # register map for LSM6DS3
        self.__regs = ISM330DHCX_Registers

        # embedded function registers for LSM6DS3
        self.__embed_func_regs = ISM330DHCX_Embedded_Function_Registers

    def __writeRegister(self, reg, d):
        msg = [reg]
        to_send = msg + d
        self.__slave.exchange(to_send, len(to_send))

    def __readRegister(self, reg, l):
        READ_BIT = 1
        READ_BIT_SHIFT = 7
        msg = [(READ_BIT << READ_BIT_SHIFT) | reg]
        return self.__slave.exchange(msg, l)

    def __getWhoAmI(self):
        whoAmIRegisterAddress = self.__regs['WHO_AM_I']
        whoAmIReadLength = 1
        self.__whoAmI = self.__readRegister(whoAmIRegisterAddress, whoAmIReadLength)[0] # turn bytearray to int

    @property
    def whoAmI(self):
        return self.__whoAmI