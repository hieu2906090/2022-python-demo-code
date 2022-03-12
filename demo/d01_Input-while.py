
# -------------------------------------------------------------
def xacDinhAmDuong(a):
    try:
        parseA = int(a)
        if parseA > 0:
            print('So duong')
            return
        if parseA < 0:
            print('So am')
            return
        if parseA == 0:
            print('Bang 0')
            return
    except ValueError:
        print('Lỗi Dữ Liệu')

# -------------------------------------------------------------


def hoiNguoiDungTiepTuc():
    print('Q1: Bạn có muốn tiếp tục chương trình? (C: Có, K: Không)')
    userInput = input()
    return userInput

# -------------------------------------------------------------


def chayChuongTrinh():
    # Mới chạy lần 1 thì mặc định userInput = 'C' để chạy
    # các lần khác sẽ thay đổi theo người dùng chọn
    userInput = 'C'
    while True:
        if (userInput == 'C'):
            print('Q2: --> Mời bạn nhập số: ')
            inputNumber = input()
            xacDinhAmDuong(inputNumber)
            userInput = hoiNguoiDungTiepTuc()
        else:
            break

# -------------------------------------------------------------


def main():
    chayChuongTrinh()


# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------
if __name__ == '__main__':
    main()
