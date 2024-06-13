#Nhập vào số nguyên dương a, đếm số ước của a
a = int(input('Nhập a: '))
dem = 0
for i in range (1,a+1):
    if a % i == 0:
        dem = dem + 1
        # print(i, end=' ')
print(a,' có  ',dem,' ước')

#cách 2
'''a = int(input('Nhập a: '))
dem = 0
for i in range (1,a//2+1):
    if a % i == 0:
        dem = dem + 1
        # print(i, end=' ')
print(a,' có  ',dem+1,' ước')
'''