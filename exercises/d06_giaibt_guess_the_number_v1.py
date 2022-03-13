import random

# -------------------------------------------------------------
# I. CHUẨN BỊ CÁC BIẾN LIÊN QUAN CỦA CHƯƠNG TRÌNH
# -------------------------------------------------------------
tongLuotChoi = 0
soLanThang = 0
userInput = 'C'

# -------------------------------------------------------------
# II. VÒNG LẶP ĐỂ THỰC HIỆN CHƠI
# -------------------------------------------------------------
while userInput == 'C':
    tongLuotChoi += 1

    print("Mời bạn đoán số (trong khoảng 1->10): ")
    userinput = int(input())
    botinput = random.randint(1, 3)
    print('Người dùng chọn giá trị: {0}. Máy chọn giá trị: {1}'.format(
        userinput, botinput))

    # 1.2. LOGIC XỬ LÝ THẮNG THUA
    # -------------------------------------------------------------
    if (userinput == botinput):
        print('HOORAH! Bạn đã đoán đúng số {0}'.format(userinput))
    else:
        print('TIẾC QUÁ! Bạn đoán {0}, nhưng số đúng là: {1}'.format(
            userinput, botinput))

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
