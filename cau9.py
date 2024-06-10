#Nhập vào số nguyên a, kiểm tra xem a có phải là số chính phương hay không, nếu có thì in ra True, ngược lại in ra False
a = int(input("Nhập số nguyên a: "))

if a >= 0 and int(a ** 0.5) ** 2 == a:
    print(True)
else:
    print(False)
#Trong đoạn mã này, 
#a ** 0.5 tính căn bậc hai của a.
#Nếu căn bậc hai của a là một số nguyên (số chính phương), thì kết quả của phép lấy mũ int(a ** 0.5) ** 2 sẽ bằng a. Nếu không, a không phải là số chính phương.


