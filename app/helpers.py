

def read_reg(reg_no):
    # bus.write_byte(bufallo, reg_no)
    # val = "{0:08b}".format(bus.read_byte(bufallo))
    val = bus.read_byte_data(bufallo, reg_no)
    ret_val = BitArray(bin(val))
    return ret_val