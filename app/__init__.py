from smbus2 import SMBus, SMBusWrapper, i2c_msg
from bitstring import BitArray

from .helpers import read_reg

bus = SMBus(1)
bufallo = 0x48

a = read_reg(10)
print(a)
print(a.bin)
print(a[0:2])
print(a[2:4])
print(a[4:6])
print(a[6:8])
