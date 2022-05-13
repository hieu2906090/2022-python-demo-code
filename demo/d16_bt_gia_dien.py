print('Mời bạn nhập giá điện các tháng cách nhau bởi dấu cách')
userInput = input().split()
userInputTemp = []

for i in userInput:
    # tempI = int(i)
    # userInputTemp.append(tempI)
    try:
        tempI = int(i)
        userInputTemp.append(tempI)
    except:
        continue

print('Người dùng nhập vào: {}'.format(userInputTemp))

# -------------------------------------------------------------
# Bài 1: Giả sử giá điện là 3000đ/chữ -> tính và in ra giá điện theo tháng nhập vào

# giaDienList = list(
#     map(lambda giaDien01Thang: giaDien01Thang*3000, userInputTemp))


def hamTinhGiaDien(soChuDien):
    return soChuDien * 3000


giaDienList = list(
    map(hamTinhGiaDien, userInputTemp))

# print('Danh sách giá điện theo tháng: {}'.format(giaDienList))

# BTVN1: với giá điện là 300000 thì in ra theo kiểu 300.000

# -------------------------------------------------------------
# Bài 2: Cho biểu giá điện như sau:
# 1 -> 50 chữ đầu: 1000
# 51 -> 100: 1500
# 101 -> 200: 2000
# >= 201: 2500
# Tính giá điện luỹ kế theo biểu trên


def hamTinhGiaDien(soChuDien):
    '''
        Biểu giá điện là:
            - 1 -> 50 chữ đầu: 1000
            - 51 -> 100: 1500
            - 101 -> 200: 2000
            - >= 201: 2500
    '''
    giaTienDien = 0
    # Logic xác ra giá tiền điện và thực hiện gán lại vào biến giaTienDien
    if soChuDien >= 1 and soChuDien < 51:
        giaTienDien = 1000
    elif soChuDien >= 51 and soChuDien < 101:
        giaTienDien = 1500
    elif soChuDien >= 101 and soChuDien < 201:
        giaTienDien = 2000
    elif soChuDien >= 201:
        giaTienDien = 2500

    return soChuDien * giaTienDien


giaDienList = list(
    map(hamTinhGiaDien, userInputTemp))

# print('Danh sách giá điện theo tháng: {}'.format(giaDienList))

# BTVN2: Người dùng nhập vào dãy số -> tính ra xếp loại học lực theo biểu sau:
# Dưới 5 điểm: Kém
# 5 -> 7 điểm: Trung Bình
# 7 -> 8 điểm: Khá
# 8 -> 9 điểm: Giỏi
# 9 -> 10 điểm: Xuất Sắc
# Yêu cầu: không nhập chữ, ko nhập số > 10.
# Note: Dùng hàm float(số) để chuyển từ chữ -> dạng số thực

# -------------------------------------------------------------
# Bài 3: Giả sử biểu giá có thể thay đổi -> viết hàm
# nhận vào biểu giá + danh sách giá điện -> in ra giá điện
# của danh sách theo biểu giá nhập vào


def tinhGiaTienDienTheoBieuGia(bieuGia=[], danhSachTienDien=[]):

    def hamTinhGiaDien(soChuDien):
        gia01ChuDien = 0
        for thongTinKhoangGia in bieuGia:
            # -> trả về [0, 50], có 1 trường hợp là số
            # khoangGia = thongTinKhoangGia['khoang_gia']
            # giaDien = thongTinKhoangGia['gia_dien']  # -> trả về [0, 50]
            # Logic xác ra giá tiền điện dựa trên khoảng giá & giaDien và thực hiện gán lại vào biến gia01ChuDien
            # Cứ khi nào soChuDien rơi vào 1 khoảng giá nào đó thì trả về giá của khoảng đó
            # đồng thời thoát vòng for bằng break
            if len(thongTinKhoangGia['khoang_gia']) == 1:
                gia01ChuDien = thongTinKhoangGia['gia_dien']
                break
            else:
                # Kiểm tra soChuDien có rơi vào thông tin khoảng giá này ko
                # -> Nếu Có: thì gán giaDien = thongTinKhoangGia['gia_dien'] và thoát for bằng break
                # -> Nếu Ko: thì tiếp tục vòng lặp bằng continue
                pass
        return soChuDien * gia01ChuDien

    giaDienList = list(
        map(hamTinhGiaDien, danhSachTienDien))

    return giaDienList


bieuGia = [
    {'khoang_gia': [0, 50], 'gia_dien': 1000},
    {'khoang_gia': [51, 100], 'gia_dien': 1500},
    {'khoang_gia': [101, 200], 'gia_dien': 2000},
    {'khoang_gia': [201], 'gia_dien': 2500},
]


dsGiaDien = tinhGiaTienDienTheoBieuGia(bieuGia, userInputTemp)
print('Danh sách giá điện theo tháng: {}'.format(dsGiaDien))
