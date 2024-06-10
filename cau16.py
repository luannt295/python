#Từ bài số 15, nếu a, b, c cấu tạo thành được một tam giác, kiểm tra xem đó là tam giác gì (tam giác đều, tam giác vuông cân, tam giác vuông, tam giác cân hay tam giác thường)
a = float(input("Nhập số thực dương a: "))
b = float(input("Nhập số thực dương b: "))
c = float(input("Nhập số thực dương c: "))

# Kiểm tra điều kiện cạnh
if a > 0 and b > 0 and c > 0:
    if a + b > c and b + c > a and a + c > b:
        if a == b == c:
            print("Tam giác đều.")
        elif a == b or b == c or a == c:
            if a == b == c / 2**0.5 or b == c == a / 2**0.5 or c == a == b / 2**0.5:
                print("Tam giác vuông cân.")
            else:
                print("Tam giác cân.")
        elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            print("Tam giác vuông.")
        else:
            print("Tam giác thường.")
    else:
        print("Ba số không thể cấu thành độ dài của một tam giác.")
else:
    print("Ba số phải là số thực dương để cấu thành độ dài của một tam giác.")
