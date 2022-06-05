from ISM330DHCX import ISM330DHCX_FTDI_SPI
import time
import sys

def main():
    imu = ISM330DHCX_FTDI_SPI(enable_xl=True, enable_gyro=True)

    try:
        while 1:
            status = imu.getStatus()[0]
            data_ready_xl = status & 0x1
            data_ready_gyro = status & 0x2
            if(data_ready_xl):
                print('Acc: X Y Z = %s' % imu.getAccDataXYZ())
            if(data_ready_gyro):
                print('Gyro: X Y Z = %s' % imu.getGyroDataXYZ())
            time.sleep(1)
    except KeyboardInterrupt:
        imu.disableAcc()
        imu.disableGyro()
        sys.exit()

if __name__ == '__main__':
    main()