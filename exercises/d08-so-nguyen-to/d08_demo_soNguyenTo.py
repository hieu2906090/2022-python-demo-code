soCanCheck = 11

chiaHet = False

# TH1: Trường hợp là số âm thì chạy for giật lùi
if (soCanCheck < 0):
    for i in range(soCanCheck + 1, -1):
        if (soCanCheck % i == 0):
            print(i)
            chiaHet = True
            break
# TH2: Trường hợp là số dương thì chạy for tới
else:
    for i in range(2, soCanCheck):
        if (soCanCheck % i == 0):
            print(i)
            chiaHet = True
            break

if (chiaHet):
    print('So {0} khong phai so nguyen to'.format(soCanCheck))
else:
    print('So {0} la so nguyen to'.format(soCanCheck))


# print(str(type(soCanCheck)).__contains__('float'))
