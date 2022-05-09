def inBangCuuChuong(soDong):
    for i in range(1, soDong + 1):
        print('CC' + str(i), end=": ")
        for e in range(1, 11):
            print(i*e, end=' ')
        print(end="\n")


# if __name__ == "__main__":
#     inBangCuuChuong(15)
