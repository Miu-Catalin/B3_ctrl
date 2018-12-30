from smbus2 import SMBus, SMBusWrapper, i2c_msg

bus = SMBus(1)
bufallo = 0x48

def read_reg(reg_no):
    # bus.write_byte(bufallo, reg_no)
    # val = "{0:08b}".format(bus.read_byte(bufallo))
    val = bus.read_byte_data(bufallo, reg_no)
    return val

print(read_reg(10))