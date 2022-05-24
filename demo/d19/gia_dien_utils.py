
def tinhGiaTienDienTheoBieuGia(bieuGia=[], danhSachDienTieuThu=[]):
    def hamTinhGiaDien(soChuDien):
        soChuDien = int(soChuDien)
        gia01ChuDien = 0
        for thongTinKhoangGia in bieuGia:
            chanDuoi = int(thongTinKhoangGia['chan_duoi'])
            # chanTren = int(thongTinKhoangGia['chan_tren']) if len(
            #     thongTinKhoangGia['chan_tren']) > 0 else 0
            chanTren = 0
            if (len(thongTinKhoangGia['chan_tren']) > 0):
                chanTren = int(thongTinKhoangGia['chan_tren'])

            giaDien = int(thongTinKhoangGia['gia_dien'])
            # LOGIC tính giá điện phải trả theo biểu giá nhập vào
            if (soChuDien >= chanDuoi and soChuDien < chanTren):
                gia01ChuDien = giaDien
                break
            else:
                gia01ChuDien = giaDien

        return soChuDien * gia01ChuDien

    tienDienHangThangList = list(
        map(hamTinhGiaDien, danhSachDienTieuThu))

    return tienDienHangThangList
