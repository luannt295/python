from math import sqrt

#Giải và biện luận phương trình ax^2 + bx + c = 0
a = float(input("Nhập số thực dương a: "))
b = float(input("Nhập số thực dương b: "))
c = float(input("Nhập số thực dương c: "))
#xét điều kiện các nghiệm: a,b,c
if a == 0:
    if b == 0:
        if c == 0:
            print('Phương Trình có vô số nghiệm')
        else:
            print('Phương Trình Vô Nghiệm')
    else:
        if c == 0:
            print('Phương Trình Có 1 Nghiệm x = 0')
        else:
            print('Phương Trình Có 1 Nghiệm x = ', -c/b)
else:    
# Bước 1: Tính Δ=b2-4ac
    delta = b*b - 4*a*c
#Bước 2: So sánh Δ với 0
#Δ < 0 => phương trình (1) vô nghiệm
    if delta <= 0:
        print('Phương Trình Vô Nghiệm')
#Δ = 0 => phương trình (1) có nghiệm kép x_{1} =x_{2} = - \frac{b}{2a}
    elif delta == 0:
        print('Phương Trình Có 1 Nghiệm: ', -b/(2*a))
    else:
        print('Phương Trình Có 2 Nghiệm Phân Biệt: ')
        print('x1 = ', float((-b - sqrt(delta))/(2*a)))
        print('x1 = ', float((-b - sqrt(delta))/(2*a)))