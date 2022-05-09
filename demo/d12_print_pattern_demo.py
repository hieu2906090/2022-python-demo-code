def inBangCuuChuong(soDong):
    for i in range(1, soDong + 1):
        print('CC' + str(i), end=": ")
        for e in range(1, 11):
            print(i*e, end=' ')
        print(end="\n")


def inXuoi(soDongCanIn):
    for i in range(1, soDongCanIn + 1):
        for e in range(1, i):
            print(end="* ")
        print(end="\n")


def inNguoc(soDongCanIn):
    for i in range(soDongCanIn, 0, -1):
        for e in range(1, i):
            print(end="* ")
        print(end="\n")


def hamInXuoiNguoc(soDongCanIn):
    if (soDongCanIn % 2 == 0):
        print('Số nhập vào không hợp lệ, hãy nhập số lẻ')
        return
    soTrungVi = round((soDongCanIn + 1) / 2)
    inXuoi(soTrungVi)
    inNguoc(soTrungVi-1)


print('Biến __name__ trong file này là: {}'.format(__name__))

if __name__ == "__main__":
    hamInXuoiNguoc(15)

# inBangCuuChuong(100)
# CC1: 1 2 3 4 5 6 7 8 9 10

# ...
# CC10: 10 20 30 40 50 60 70 80 90 100


# 1 *
# 2 * *
# 3 * * *
# 4 * * * *
# 5 * * * * *
# 6 * * * * * *
# 7 * * * * * * *
# 8 * * * * * * * *
# 9 * * * * * * *
# 10 * * * * * *
# 11 * * * * *
# 12 * * * *
# 13 * * *
# 14 * *
# 15 *
