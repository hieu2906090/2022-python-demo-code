
# I. FIRST CLASS FUNCTION
# arrList = [1, 2, 3, 4, 5]
# varA = 'Bien A'


# def inTungSoFunc(so):
#     print('Số nhận vào là: {0}'.format(so))


# def inDanhSachSo(danhSach, cb):
#     # print('So A la: {0}'.format(bienCoTenLaA))
#     for so in danhSach:
#         cb(so)


# inDanhSachSo(arrList, varA)

# II. DEMO MAP() TRÊN BÀI TOÁN TIỀN ĐIỆN

# giaMotChuDien = 2500

# soChuDienHangThang = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# def hamTinhTienDienMotThang(soChuDienTieuThuTrongThang):
#     return 'Điện năng tiêu thụ: {0}, tiền điện là: {1}'.format(soChuDienTieuThuTrongThang, giaMotChuDien * soChuDienTieuThuTrongThang)


# tienDienHangThang = list(map(hamTinhTienDienMotThang, soChuDienHangThang))
# print(tienDienHangThang)

# III. DEMO FILTER()
arrList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

arrList2 = [3, 6, 11, 111, 222]

# IV. CLOSURE DEMO


def traVeDanhSachTrung(listA, listB):
    # C1: Cách bình thường
    # tempList = []
    # for item in listA:
    #     if(item in listB):
    #         tempList.append(item)

    # C2: Cách dùng filter + lambda
    # tempList = list(filter(lambda item: item in listB, listA))

    # C3: Cách dùng filter + closure (hàm được defined trong thân hàm khác)
    def checkItemTrongListB(item):
        return item in listB

    tempList = list(filter(checkItemTrongListB, listA))
    return tempList


listTrung = traVeDanhSachTrung(arrList, arrList2)
print(listTrung)

# def soChiaHetCho2(so):
#     return so % 3 == 0


# newList = list(filter(lambda x: x > 6, arrList))
# print(301 in arrList2)
