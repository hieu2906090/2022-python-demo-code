# String slicing
# print('abc1234'[::-1])

import math

diaChi = (123, 321)
diaChiList = [1234, 321]

# dsSo = [1, 23, 5, 2, 5, 5, 1, 34, 5, 34, 53, 45, 34, 534, 53, 42, 34, 234]
# dictionary = {'A': (1, 2), 'B': (3, 4), 'C': (12, 35), 'D': (11, 77)}

listToaDo = [(1, 2), (3, 4), (12, 35), (11, 77), (33, 56)]


def khoangCachGiua2Diem(diemSo1, diemSo2):
    diemSo1[0][0]  # --> 1
    diemSo1[1]  # --> 2
    diemSo2[0]  # --> 3
    diemSo2[1]  # --> 4
    khoangCach = math.sqrt()
    return khoangCach


def duyetQuaListToaDoDeTinhKhoangCach(listToaDo):
    listKhoangCach = []
    doDaiMang = len(listToaDo)
    for idx in range(0, doDaiMang):
        for idy in range(idx+1, len(doDaiMang) + 1):

            print(idx, listToaDo[idx])  # idx: 0 -> listToaDo[idx]: (1,2)

    return listKhoangCach


def timSoLonNhatNhoNhatTuDanhSach(danhSach):
    soLonNhat = 0
    soNhoNhat = danhSach[0]
    for item in danhSach:
        if (item > soLonNhat):
            soLonNhat = item
        if (item < soNhoNhat):
            soNhoNhat = item
    return soNhoNhat, soLonNhat


danhSach = duyetQuaListToaDoDeTinhKhoangCach(listToaDo)
soNhoNhat, soLonNhat = timSoLonNhatNhoNhatTuDanhSach(danhSach)
print('Khoảng cách lớn nhất: {0}. Khoảng cách nhỏ nhất: {1}'.format(
    soLonNhat, soNhoNhat))
# print(max(dsSo), min(dsSo))

# print('Dia Chi Tuple La: ' + str(diaChi[0]))
# print('Dia Chi List La: ' + str(diaChiList[0]))
# print('Dictionary La: {0}'.format(dictionary))
