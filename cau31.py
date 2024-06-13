#Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b
def uocchungab(a,b):
    d = dict()
    vitri = 0
    if a <b:
        for i in range (1,a):
            if a%i == 0 and b % i == 0:
                d[vitri]=i
                vitri = vitri+1
        return d  
print(uocchungab(10,20))