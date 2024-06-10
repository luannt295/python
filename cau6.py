#Nhập vào số nguyên a, nếu a là số chia hết cho 5 nhưng KHÔNG nằm trong khoảng từ 20 - 70 thì in ra True, ngược lại in ra False
a = int(input('Nhập số nguyên a: '))
if a%5 == 0 and (a < 20 or a > 70):
    print(True)
else:
    print(False)