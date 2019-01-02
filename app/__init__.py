from app.helpers import read_reg

ret_code, a = read_reg(10)
if ret_code == 0:
    print(a)
    print(a.bin)
    print(a[0:2])
    print(a[2:4])
    print(a[4:6])
    print(a[6:8])
else:
    print('error')