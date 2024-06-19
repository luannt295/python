#Viết chương trình nhập vào từ bàn phím một số bất kỳ ở hệ thập phân và hiển thị ra màn hình số đó ở hệ bát phân (Có xử lý ngoại lệ đầu vào).
so = input('Nhập 1 số: ')
try:
    sothapphan = int(so)
    print(' Số thập phân %d có số bát phân là %o' %(sothapphan,sothapphan) )
except:
    print('Nhập sai giá trị')