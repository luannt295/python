#Nhập vào lương tháng này nhận được, ta phải đưa cho vợ 90% số tiền lương đó. Hãy in ra lương ta giữ lại
luong = int(input('Lương Tháng Này: '))
tienduavo = int(luong*90/100)
tienconlai = int(luong - tienduavo)
print('Số tiền bạn còn lại:', tienconlai) 
