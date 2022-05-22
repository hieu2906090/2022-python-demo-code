def nhapThongTin(cauThongBao, danhSachKey):
    '''
        Hàm tổng quát cho quá trình nhập thông tin nhận vào 2 tham số:
        - cauThongBao: in ra thông báo cách nhập cho người dùng biết
        - danhSachKey: danh sách các key (khoá) dùng để tạo dictionary trả về. Vd:
        Trả về: {key1: input[0], key2: input[1]}
    '''
    print(cauThongBao)
    # dsNguoiDungNhap: ['tin', '12A3', '8']
    dsNguoiDungNhap = input().split(',')
    tempDict = {}
    # danhSachKey: ['ten', 'lop', 'diem_tb']
    for idx, key in enumerate(danhSachKey):
        tempDict[key] = dsNguoiDungNhap[idx]
    return tempDict


def nhapNhieuThongTinVoiWhile(cauThongBao, danhSachKey):
    tiepTucHayKhong = True
    thongTinList = []
    while tiepTucHayKhong:
        ttHsDict = nhapThongTin(cauThongBao, danhSachKey)
        thongTinList.append(ttHsDict)
        print('Bạn có muốn tiếp tục hay không? (C: Có, K: Không)')
        nguoiDungChon = input().upper()
        if (nguoiDungChon != 'C'):
            tiepTucHayKhong = False
    return thongTinList


if __name__ == '__main__':
    cauThongBaoDemo = 'Mời bạn nhập thông tin học sinh theo định dạng Họ Tên, Lớp, Điểm TB'
    danhSachKeyDemo = ['ten', 'lop', 'diem_tb']
    thongTinPhoDiem = nhapNhieuThongTinVoiWhile(
        cauThongBaoDemo, danhSachKeyDemo)
    print('Thông Tin Phổ Điểm Là: {0}'.format(thongTinPhoDiem.__str__()))
