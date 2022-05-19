def hoiThongTinVaTraVe01HSDict():
    '''
        Hàm sẽ hỏi người dùng input vào thông tin dưới dạng chuỗi "Hieu,18,12A1"
        sau đó thực hiện split chuỗi theo ký tự "," \n
        - Thông tin sẽ được chuyển thành list: ['Hieu', ' 18', ' 12A1']
        - Và được trả về dưới dạng dict: {'name': ..., 'age': ..., 'class': ...}
    '''
    print('Mời bạn nhập thông tin học sinh theo định dạng Họ Tên, Lớp, Điểm TB')
    ttHs = input().split(',')
    return {'name': ttHs[0], 'lop': ttHs[1], 'diem_tb': float(ttHs[2])}


def nhapThongTinCuaNhieuHocSinh():
    tiepTucHayKhong = True
    thongTinHSList = []
    while tiepTucHayKhong:
        ttHsDict = hoiThongTinVaTraVe01HSDict()
        thongTinHSList.append(ttHsDict)
        print('Bạn có muốn tiếp tục hay không? (C: Có, K: Không)')
        nguoiDungChon = input().upper()
        if (nguoiDungChon != 'C'):
            tiepTucHayKhong = False
    return thongTinHSList
