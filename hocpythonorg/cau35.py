'''
Nhập n

Cho S(k) = 1 + 2 + 3 + … + k

Tìm k sao cho S(k) lớn nhất nhưng nhỏ hơn n
'''

n = int(input('Nhập n: '))
sk=0
k=0
while True:
    k +=1
    sk +=k
    if sk >=n:
        k -=1
        break
print(f'Giá trị {k} lớn nhất sao cho {sk} nhỏ hơn {n} là: {k}')
