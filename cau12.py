#Nhập vào 3 số a, b, c. Tính và in ra d = (a + b)^c
#Nếu d là số trong khoảng từ 100 - 200 thì in ra True, ngược lại in ra False
a = int(input('Nhap a: '))
b = int(input('Nhap b: '))
c = int(input('Nhap c: '))
d = (a + b)**c
if d in range (100,200):
    print(True)
else:
    print(False)

