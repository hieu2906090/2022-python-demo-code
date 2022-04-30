def tinhTongChanLe(soCanTinh, soCanChia):
    tongChan = 0
    tongLe = 0
    danhSachSoChan = []
    danhSachSoLe = []

    for i in range(0, soCanTinh+1):
        if (i % 2 == 0):
            danhSachSoChan.append(i)
            tongChan += i
        else:
            danhSachSoLe.append(i)
            tongLe += i

    print('Danh sách chẵn: ' + danhSachSoChan.__str__())
    print('Danh sách lẻ: ' + danhSachSoLe.__str__())
    print('Tổng số chẵn {0}, tổng số lẻ {1}'.format(tongChan, tongLe))


tinhTongChanLe(11, 3)
