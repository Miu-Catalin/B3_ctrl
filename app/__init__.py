from smbus2 import SMBus, SMBusWrapper, i2c_msg

with SMBusWrapper(1) as bus:
    reg_value = bus.read_byte_data(1, 10)
    print(reg_value)