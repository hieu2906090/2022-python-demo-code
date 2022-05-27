import math


def khoangCachGiua2Diem(diemSo1, diemSo2):
    khoangCach = math.sqrt(
        (diemSo1[0] - diemSo2[0])**2 + (diemSo1[1] - diemSo2[1])**2)

    return khoangCach


def duyetQuaListToaDoDeTinhKhoangCach(listToaDo):
    listKhoangCach = []
    doDaiMang = len(listToaDo)
    for idx in range(0, doDaiMang):
        for idy in range(idx+1, doDaiMang):
            khoangCach = khoangCachGiua2Diem(listToaDo[idx], listToaDo[idy])
            listKhoangCach.append(khoangCach)

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
