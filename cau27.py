#Viết chương trình in ra hình tam giác có độ cao h được nhập từ bàn phím
#in ra tam giac deu
"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
for i in range(6):
    print(' '*(6-i-1), end='')
    for j in range(i+1):
        print('* ', end='')
    print('')
        

