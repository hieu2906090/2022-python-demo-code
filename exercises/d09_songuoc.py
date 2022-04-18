# Thuật toán kiểm tra soCanCheck có phải số soi gương
# Nếu là số soi gương thì giữ nguyên cờ (flag) isSoSoiGuong
# Nếu không phải thì đổi cờ thành False và thoát vòng lặp
def checkCoPhaiLaSoSoiGuongKhongV1(soCanCheck):
    isSoSoiGuong = True
    chuoiDaoNguoc = str(soCanCheck)[::-1]  # 'abc1234'[1:4]
    if (int(chuoiDaoNguoc) != soCanCheck):
        isSoSoiGuong = False
    return isSoSoiGuong
    # return về True nếu là số soi gương (121, 111, 131, 11), False nếu là trường hợp còn lại (23)

# -------------------------------------------------------------


def checkCoPhaiLaSoSoiGuongKhongV3(soCanCheck):
    isSoSoiGuong = True
    soDaoNguoc = 0
    phanNguyen = soCanCheck
    while soDaoNguoc < soCanCheck:  # 123
        if (phanNguyen == 0):
            break
        soDaoNguoc = soDaoNguoc * 10 + phanNguyen % 10
        phanNguyen = phanNguyen // 10
    if (soDaoNguoc != soCanCheck):
        isSoSoiGuong = False
    return isSoSoiGuong
# -------------------------------------------------------------


def checkCoPhaiLaSoSoiGuongKhongV2(soCanCheck):
    isSoSoiGuong = True
    chuoiDaoNguoc = ''
    soDaoNguoc = 0
    phanNguyen = soCanCheck
    phanDu = 0
    while soDaoNguoc < soCanCheck:  # 123 -> 3 < 123 -> 32 < 123
        if (phanNguyen == 0):
            break
        phanDu = phanNguyen % 10  # 3 - 2 - 1
        phanNguyen = phanNguyen // 10  # 12 - 1 - 0

        # '' + 3 -> '3' --> '3' + '2' --> '32' + '1' -> '321'
        chuoiDaoNguoc = chuoiDaoNguoc + str(phanDu)

        # int('3') -> 3 --> '32' -> 32 --> '321' -> 321
        soDaoNguoc = int(chuoiDaoNguoc)

    # chuoiDaoNguoc = str(soCanCheck)[::-1]
    if (int(chuoiDaoNguoc) != soCanCheck):
        isSoSoiGuong = False

    return isSoSoiGuong
    # return về True nếu là số soi gương (121, 111, 131, 11), False nếu là trường hợp còn lại (23)


# -------------------------------------------------------------


def inDanhSachSoSoiGuongTrongKhoang(khoangDuocNhapVao):
    dsSoSoiGuong = []
    for soCanCheck in range(1, khoangDuocNhapVao + 1):
        if (checkCoPhaiLaSoSoiGuongKhongV3(soCanCheck)):
            dsSoSoiGuong.append(soCanCheck)
    return dsSoSoiGuong


soCanNhap = 1000
ds = inDanhSachSoSoiGuongTrongKhoang(soCanNhap)  # --> [...].

print(
    'Danh sách số là số soi gương trong khoảng 0 -> {0}: {1}'.format(soCanNhap, ds.__str__()))
