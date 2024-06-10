#Nhập vào 3 số a, b, c. Hãy sắp xếp 3 số a, b, c theo thứ tự tăng dần rồi in ra lại
a = int(input('Nhap a: '))
b = int(input('Nhap b: '))
c = int(input('Nhap c: '))

tangdan = sorted([a,b,c])
print('các số tăng dần: ', tangdan)