#Nhập tháng, năm. Hãy cho biết tháng đó có bao nhiêu ngày
#Bước 1: nhập dữ liệu
thang=int(input('Nhập Tháng: '))
nam=int(input('Nhập Năm: '))
#Bước 2: xác định tháng đó có bao nhiêu ngày và in ra
if thang==1:
    print('Tháng 1 có: ',31 +' Ngày')
elif thang == 2:
    if (nam % 400 == 0) or ((nam % 4 == 0) and (nam % 100 != 0)):
        print('Tháng 2 có 29 Ngày')
    else:
        print('Tháng 2 có 28 Ngày')
elif thang == 3:
    print('Tháng 3 có 31 ngày')
elif thang == 4:
    print('Tháng 4 có 30 ngày')
elif thang == 5:
    print('Tháng 5 có 31 ngày')
elif thang == 6:
    print('Tháng 6 có 30 ngày')
elif thang == 7:
    print('Tháng 7 có 31 ngày')
elif thang == 8:
    print('Tháng 8 có 31 ngày')
elif thang == 9:
    print('Tháng 9 có 30 ngày')
elif thang == 10:
    print('Tháng 10 có 31 ngày')
elif thang == 11:
    print('Tháng 11 có 30 ngày')
elif thang == 12:
    print('Tháng 12 có 31 ngày')