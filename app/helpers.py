
from smbus2 import SMBus, SMBusWrapper, i2c_msg
from bitstring import BitArray, BitStream

bus = SMBus(1)
bufallo = 0x48

def read_reg(reg_no):
    # bus.write_byte(bufallo, reg_no)
    # val = "{0:08b}".format(bus.read_byte(bufallo))
    try:
        val = bus.read_byte_data(bufallo, reg_no)
    except Exception as err:
        print(err)
        return 1, err
    else:
        ret_val = BitArray(bin(val))
        return 0, ret_val

def write_reg(reg_no, data):
    try:
        bus.write_byte_data(bufallo, reg_no, data)
    except:
        return 1
    return 0

def change_reg(reg_no, data, pos_start):
    bit_array = BitStream(bin(read_reg(reg_no)))
    bit_array.pos = pos_start
    bit_array.overwrite = ('0b0101')
    return bit_array
