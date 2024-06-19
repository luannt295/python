'''
Viết chương trình nhập vào từ bàn phím một dãy số nguyên với độ dài bất kỳ,
dãy số nằm trên 1 dòng, các số cách nhau bởi khoảng trắng.
Tính tổng của dãy số và hiển thị ra màn hình.
'''

daygiatri = input()
dayso = daygiatri.split()
daysokhoangtrang = map(int,dayso)
print(daysokhoangtrang)
tong = sum(daysokhoangtrang)
print(tong)