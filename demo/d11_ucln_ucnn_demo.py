def timSoLonNhatNhoNhatTuDanhSach(danhSach):
    soLonNhat = 0
    soNhoNhat = danhSach[0]
    for item in danhSach:
        if (item > soLonNhat):
            soLonNhat = item
        if (item < soNhoNhat):
            soNhoNhat = item
    return soNhoNhat, soLonNhat


def traVeDanhSachUocCua2So(a, b):
    danhSach = []
    #
    soNhoNhat, soLonNhat = timSoLonNhatNhoNhatTuDanhSach(danhSach)
    return timSoLonNhatNhoNhatTuDanhSach(danhSach)


danhSach = traVeDanhSachUocCua2So(12, 10)
soNhoNhat, soLonNhat = timSoLonNhatNhoNhatTuDanhSach(danhSach)
