#Hiển thị từ cách nhau bởi ký tự "--" ra màn hình
'''
Viết chương trình hiển thị các từ theo yêu cầu ra màn hình: “Xin”, “chao!", “Toi", “ten", “la”, “{Tên của bạn}”. Các từ cách nhau bởi “--” và {Tên của bạn} được nhập từ bàn phím.
Cách 1 
dau = '--'
a = str('Luan')
kytu = ['xin', 'chao', 'toi', 'ten', 'la', a]
b = dau.join(kytu) 
print(b)
'''
#cách 2 
ten = input()
print('Xin', 'Chao', 'toi','ten', 'la', ten, sep='--')