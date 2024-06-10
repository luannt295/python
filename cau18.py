#Giải và biện luận phương trình ax + b = 0
def giai_phuong_trinh(a, b):
    if a == 0:
        if b == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -b / a
        print("Nghiệm của phương trình là:", x)

# Nhập giá trị của a và b từ người dùng
a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))

# Giải và biện luận phương trình
giai_phuong_trinh(a, b)
