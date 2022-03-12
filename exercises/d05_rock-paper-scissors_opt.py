import random
# -------------------------------------------------------------
# I. CHUẨN BỊ CÁC BIẾN LIÊN QUAN CỦA CHƯƠNG TRÌNH
# -------------------------------------------------------------
dict = {3: 'Búa', 2: 'Kéo', 1: 'Bao'}
tongLuotChoi = 0
soLanThang = 0

userInput = 'C'

# -------------------------------------------------------------
# II. VÒNG LẶP ĐỂ THỰC HIỆN CHƠI OẲN TÙ TÌ
# -------------------------------------------------------------
while userInput == 'C':
    tongLuotChoi += 1
    # -------------------------------------------------------------
    # 1. MỘT LƯỢT CHƠI
    # 1.1. PHẦN XỬ LÝ INPUT VÀO
    print("Mời bạn chọn: (3) Búa, (2) Kéo, (1) Bao")
    userinput = int(input())
    # print(type(userinput))
    botinput = random.randint(1, 3)
    print('Người dùng chọn giá trị: {0}. Máy chọn giá trị: {1}'.format(
        dict[userinput], dict[botinput]))

    # 1.2. LOGIC XỬ LÝ THẮNG THUA
    # -------------------------------------------------------------
    # 0. Trường hợp hoà
    if (userinput == botinput):
        print("Hoà")

    # -------------------------------------------------------------
    # 1. Hai trường hợp không nằm trong mẫu lớn hơn thì thắng (bé hơn thì thua)
    # Lưu ý 2 case này thì nhớ exit để thoát chương trình, không chạy if cuối cùng
    elif (userinput == 1 and botinput == 3):
        soLanThang += 1
        print('{0} Thắng {1}'.format(dict[userinput], dict[botinput]))

    elif (userinput == 3 and botinput == 1):
        print('{0} Thua {1}'.format(dict[userinput], dict[botinput]))

    # -------------------------------------------------------------
    # 2. Trong trường hợp bình thường thì lớn hơn thắng, bé hơn thua
    elif (userinput > botinput):
        soLanThang += 1
        print('{0} Thắng {1}'.format(dict[userinput], dict[botinput]))
    else:
        print('{0} Thua {1}'.format(dict[userinput], dict[botinput]))

    # -------------------------------------------------------------
    # 2. HỎI NGƯỜI DÙNG TIẾP TỤC
    print('Bạn có muốn tiếp tục: (C) Có, (K) Không')
    userInput = input()
    if (userInput == 'K'):
        break

# -------------------------------------------------------------
# III. IN KẾT QUẢ SAU KHI KẾT THÚC VÒNG LẶP
# -------------------------------------------------------------
print('Người chơi đã thực hiện tổng {0} lượt. Số lần thắng là {1}'.format(
    tongLuotChoi, soLanThang))
