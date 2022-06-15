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


def xacDinhSoHoanHao(a):
    s = 0
    for i in range(1, a):
        if a % i == 0:
            s += i

    if s == a:
        return True

    return False


# --------------------------------------------------------------
nguoidungnhap = int(input())
print(nguoidungnhap)
for i in range(2, nguoidungnhap + 1):
    if (xacDinhSoHoanHao(i)):
        print('Số {} là số hoàn hảo'.format(i))
