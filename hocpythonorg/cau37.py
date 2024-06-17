'''#Nhập vào một dãy số nguyên, ngưng nhập khi người dùng nhập -1.

Sau khi nhập xong, in số lớn nhất, số nhỏ nhất trong những số vừa nhập'''
#tạo list
danhsach = []
#KIỂM TRA điều kiện
while True:
    songuyen = int(input('Nhập số nguyên: '))
    if songuyen == -1:
        break
    danhsach.append(songuyen)
#kiểm tra danh sách có rỗng không
if len(danhsach) > 0:
    snn = min(danhsach)
    sln = max(danhsach)
    print(f"Số lớn nhất trong dãy số vừa nhập là: {sln}")
    print(f"Số nhỏ nhất trong dãy số vừa nhập là: {snn}")
else:
    print('Sai')