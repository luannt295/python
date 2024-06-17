#Nhập vào 3 số thực dương a, b, c. Kiểm tra xem a, b, c có cấu thành độ dài của 1 tam giác được không
#1)Tổng của hai cạnh bất kỳ phải lớn hơn cạnh còn lại.
#2)Mỗi cạnh phải lớn hơn 0.
a = float(input('Nhap a: '))
b = float(input('Nhap b: '))
c = float(input('Nhap c: '))
if a > 0 and b > 0 and c >0:
    if a+b > c and a+c>b and b+c>a:
        print("Có thể cấu thành độ dài của một tam giác.")
    else:
        print("Không thể cấu thành độ dài của một tam giác.")
else:
    print("Ba số phải là số thực dương để cấu thành độ dài của một tam giác.")
