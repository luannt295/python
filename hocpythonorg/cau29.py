#Nhập vào số nguyên dương a, in toàn bộ ước của a
a = int(input('Nhập a: '))
for i in range (1,a):
    if a % i == 0:
        print(i, end=' ')
