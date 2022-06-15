'''
def XacDinhSoHoanHao(a):
    s=0
    for i in range(1,a):
        if a%i==0:
            s+=i
            if s==a:


                print(s)
    
XacDinhSoHoanHao(6)
'''


def XacDinhSoHoanHao(a):
    s = 0
    for i in range(1, a):
        if a % i == 0:
            s += i
            if s == a:
                print(s)

# 1 2 3 4 6 8 12


1+2+3+4+6+8

nguoidungnhap = int(input())
print(nguoidungnhap)
for i in range(2, nguoidungnhap):
    XacDinhSoHoanHao(i)
