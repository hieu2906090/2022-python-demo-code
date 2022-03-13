import random

# -------------------------------------------------------------
# -1. CHUẨN BỊ CÁC BIẾN LIÊN QUAN CỦA CHƯƠNG TRÌNH
# -------------------------------------------------------------
dict = {3: 'Búa', 2: 'Kéo', 1: 'Bao'}

# -------------------------------------------------------------
# I. MỘT LƯỢT CHƠI
# -------------------------------------------------------------
# 1. PHẦN XỬ LÝ INPUT VÀO
print("Mời bạn chọn: (3) Búa, (2) Kéo, (1) Bao")
userinput = int(input())
# print(type(userinput))
botinput = random.randint(1, 3)
print('Người dùng chọn giá trị: {0}. Máy chọn giá trị: {1}'.format(
    dict[userinput], dict[botinput]))

# 2. LOGIC XỬ LÝ THẮNG THUA
# -------------------------------------------------------------
# 2.C0: Hoà
if (userinput == botinput):
    print("Hoà")
    exit()

# -------------------------------------------------------------
# 2.C1: Trường hợp người dùng chọn Búa
if (userinput == 3):
    if (botinput == 2):
        print('{0} thắng {1}'.format(dict[userinput], dict[botinput]))
    if (botinput == 1):
        print('{0} thua {1}'.format(dict[userinput], dict[botinput]))

# -------------------------------------------------------------
# 2.C2: Trường hợp người dùng chọn Kéo
elif (userinput == 2):
    if (botinput == 1):
        print('{0} thắng {1}'.format(dict[userinput], dict[botinput]))
    if (botinput == 3):
        print('{0} thua {1}'.format(dict[userinput], dict[botinput]))

# -------------------------------------------------------------
# 2.C3: Trường hợp người dùng chọn Bao
elif (userinput == 1):
    if (botinput == 3):
        print('{0} thắng {1}'.format(dict[userinput], dict[botinput]))
    if (botinput == 2):
        print('{0} thua {1}'.format(dict[userinput], dict[botinput]))

# 3. TRẢ KẾT QUẢ THẮNG THUA
