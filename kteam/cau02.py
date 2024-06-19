#Tính tổng hai số nguyên bất kỳ (Có xử lý ngoại lệ đầu vào).
giatri1 = input('Nhap gia tri 1: ')
giatri2 = input('Nhap gia tri 2: ')

try:
    so1 = int(giatri1)
    so2 = int(giatri2)
    tong = so1 + so2
    print(tong)
except:
    print('sai gia tri nhập')