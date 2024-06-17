'''
Nhập vào A, tìm n nhỏ nhất sao cho

1 + 1/2 + 1/3 + 1/4 + ... + 1/n > A
'''
a = float(input('Nhập số nguyên dương a: '))
n =0
tong = 0 
while tong <=a:
     n = n +1
     tong = tong + 1/n
print(f'{n} nhỏ nhất là: ', n)
     