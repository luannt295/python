'''
Viết chương trình nhập vào từ bàn phím một dãy số nguyên với độ dài bất kỳ, dãy số nằm trên 1 dòng, các số cách nhau bởi khoảng trắng.
Tính tổng của dãy số và hiển thị ra màn hình (Có xử lý ngoại lệ đầu vào).
'''

nhap = input('Nhap: ')
so = nhap.split()
try:
    dayso = map(int,so)
    tong=sum(dayso)
    print(tong)
except:
    print('Bạn cần nhập số, không phải kí tự')