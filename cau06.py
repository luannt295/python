#Viết chương trình làm tròn số thập phân A đến B chữ số sau dấu phẩy. A và B được nhập bất kỳ từ bàn phím. Hiển thị số A sau khi được làm tròn ra màn hình.
a = float(input('Nhập a: '))
dauphayb = int(input('Nhập số thập phân cần làm tròn: '))
lamtron = float(round(a, dauphayb))
print(lamtron)