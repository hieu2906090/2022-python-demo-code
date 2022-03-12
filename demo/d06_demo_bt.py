from d06_import_bt import xuLyLogicThangThua, taoUserVaBotInput


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
    # taoUserVaBotInput
    userinput, botinput = taoUserVaBotInput()
    print('Người dùng chọn giá trị: {0}. Máy chọn giá trị: {1}'.format(
        dict[userinput], dict[botinput]))

    # 1.2. LOGIC XỬ LÝ THẮNG THUA
    ketQua, soLanThang = xuLyLogicThangThua(
        userinput, botinput, dict, soLanThang)
    print('Kết quả in ra ở trong while là: ' + ketQua)

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

# Bài Tập 1: Người dùng chọn sẵn 1 số bất kỳ từ 0 -> 100. Máy đoán 1 số
# -> Có 3 trường hợp xảy ra (cao hơn, bằng, thấp hơn)
# -> Nếu cao hơn hoặc thấp hơn thì cho máy đoán lại
# -> Nếu bằng thì dừng chương trình và in ra số lần máy tính mất để đoán đúng số
# Ví Dụ: Số phải đoán là 51
# L1. AI đoán 100 -> Cao hơn
# L2. AI đoán 1 -> Thấp hơn
# ... n lần
# Ln. AI đoán 50 -> Đúng
# -> Thoát chương trình + in ra số lần (n lần)

# Hangman man _a_ -> ['beautiful', 'interest', 'python', 'vscode']
# -> i__e_es_ -> đoán đi!
# -> n -> đáon đúng -> in_e_es_ (bạn còn đủ 5 lần đoán)
# -> y -> sai -> in_e_es_ (bạn chỉ còn 4 lần)
