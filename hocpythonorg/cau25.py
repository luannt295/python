#Nhập vào số nguyên dương a, in ra bảng cửu chương của a
a = int(input('Nhập bảng cửu chương: '))
if a < 1 or a >= 10:
    print('Nhập Sai')
else:
    for i in range (1,10):
        print('{} x {} = {}'.format(a,i,a*i))