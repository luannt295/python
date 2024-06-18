'''Viết chương trình làm tròn số thập phân A đến B chữ số sau dấu phẩy. A và B được nhập bất kỳ từ bàn phím. 
Hiển thị số A sau khi được làm tròn ra màn hình (Có xử lý ngoại lệ đầu vào).'''
nhapso = input('Nhập 1 số: ')
nhapso1 = input('Làm tròn tới bao nhiêu số: ')
try:
    so = float(nhapso)
    lamtron = int(nhapso1)
    solamtron = float(round(so,lamtron))
    print(solamtron)
except:
    print('Nhập sai, nhập lại')