encodeDict = {'TE': 5, 'CH': 4, 'NG': 3, 'PN': 2, 'DO': 1}


def hoiThongTinVaTraVe01HSDict():
    print('Mời bạn nhập thông tin nguời bị nạn theo định dạng Họ Tên, phân loại trẻ em (TE),chó (CH),người già (NG),phụ nữ (PN),đàn ông (DO)')
    ttHs = input().split(',')
    return {'ten': ttHs[0], 'phan_loai_uu_tien': ttHs[1], 'thu_tu_uu_tien': encodeDict[ttHs[1]]}


def nhapThongTincuanhieunguoibinan():
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


thongTinHSList = nhapThongTincuanhieunguoibinan()

# doDaiMang = len(thongTinHSList)
# if doDaiMang < 2:
#     print('phải nhập số phần tử lớn hơn hai')
#     thongTinHSList = nhapThongTincuanhieunguoibinan()


tempTTHSList = []

tempTTHSList = list(thongTinHSList)

tempTTHSList.sort(reverse=True, key=lambda x: x['thu_tu_uu_tien'])

for nguoiDung in tempTTHSList:
    print('Tên bạn nhập vào là: {0}, thứ tự là {1}'.format(
        nguoiDung['ten'], nguoiDung['thu_tu_uu_tien']))
