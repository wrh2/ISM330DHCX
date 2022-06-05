from ISM330DHCX import ISM330DHCX_FTDI_SPI, ISM330DHCX_Scale_Selection
import time
import sys

def main():
    scale = ISM330DHCX_Scale_Selection['SCALE_2G']
    #imu = ISM330DHCX_FTDI_SPI(enable_xl=True, scale_xl=scale)
    imu = ISM330DHCX_FTDI_SPI(enable_xl=True)

    try:
        while 1:
            data_ready = imu.getStatus()[0] & 0x1
            if(data_ready):
                print('X Y Z = %s' % imu.getAccDataXYZ())
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()