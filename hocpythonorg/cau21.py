#Nhập điểm toán, văn, anh.

# Nếu điểm đúng quy tắc (trong khoảng từ 0 - 10), ta tính điểm trung bình rồi tiến hành xét:

# Nếu điểm trung bình lớn hơn hoặc bằng 8, toán hoặc văn lớn hơn hoặc bằng 8 và không có điểm nào dưới 6.5 thì in ra “Học sinh giỏi”
# Nếu không đủ điều kiện học sinh giỏi ta xét nếu điểm trung bình lớn hơn hoặc bằng 6.5, toán hoặc văn lớn hơn hoặc bằng 6.5 và không có điểm nào dưới 5 thì in ra “Học sinh khá”
# Nếu không đủ điều kiện học sinh khá ta xét nếu điểm trung bình lớn hơn hoặc bằng 5, toán hoặc văn lớn hơn hoặc bằng 5 và không có điểm nào dưới 3.5 thì in ra “Học sinh trung bình”
# Nếu không đủ điều kiện học sinh trung bình ta xét nếu điểm trung bình lớn hơn hoặc bằng 3.5, toán hoặc văn lớn hơn hoặc bằng 3.5 và không có điểm nào dưới 2 thì in ra “Học sinh yếu”
# Nếu không đủ điều kiện học sinh yếu ta in ra “Học sinh kém”
toan = float(input('Điểm Toán: '))
van = float(input('Điểm Văn: '))
anh = float(input('Điểm Anh: '))

diemtrungbinh = (toan + van + anh)/3
print('Điểm trung binh: ',diemtrungbinh)
if diemtrungbinh >= 8 and toan >= 8 and van >= 8 and anh >= 6.5:
            print('Học Sinh Giỏi')
elif diemtrungbinh >= 6.5 and toan >= 6.5 or van >=6.5 and anh >= 5:
            print('Học Sinh Khá')
elif diemtrungbinh >= 5 and toan >= 5 or van >=5 and anh >= 3.5:
            print('Học Sinh Trung Bình')
elif diemtrungbinh >= 3.5 and toan >= 3.5 or van >=3.5 and anh >= 2:
            print('Học Sinh Yếu')
else:
      print('Học Sinh Kém')
