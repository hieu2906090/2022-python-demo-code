import random

dict = {3: 'Búa', 2: 'Kéo', 1: 'Bao'}

print("Mời bạn chọn: (3) Búa, (2) Kéo, (1) Bao")
userinput = int(input())
# print(type(userinput))
botinput = random.randint(1, 3)
print('Người dùng chọn giá trị: {0}. Máy chọn giá trị: {1}'.format(
    dict[userinput], dict[botinput]))

# -------------------------------------------------------------
# 0. Trường hợp hoà
if (userinput == botinput):
    print("Hoà")
    exit()

# -------------------------------------------------------------
# 1. Hai trường hợp không nằm trong mẫu lớn hơn thì thắng (bé hơn thì thua)
# Lưu ý 2 case này thì nhớ exit để thoát chương trình, không chạy if cuối cùng
if (userinput == 1 and botinput == 3):
    print('{0} Thắng {1}'.format(dict[userinput], dict[botinput]))
    exit()

if (userinput == 3 and botinput == 1):
    print('{0} Thua {1}'.format(dict[userinput], dict[botinput]))
    exit()

# -------------------------------------------------------------
# 2. Trong trường hợp bình thường thì lớn hơn thắng, bé hơn thua
if (userinput > botinput):
    print('{0} Thắng {1}'.format(dict[userinput], dict[botinput]))
else:
    print('{0} Thua {1}'.format(dict[userinput], dict[botinput]))

# -------------------------------------------------------------
# II. GIẢI BÀI TOÁN VỚI IF VÀ ELIF
# -------------------------------------------------------------
# -------------------------------------------------------------
# 0. Trường hợp hoà
# if (userinput == botinput):
#     print("Hoà")
#     exit()

# # -------------------------------------------------------------
# # 1. Hai trường hợp không nằm trong mẫu lớn hơn thì thắng (bé hơn thì thua)
# # Lưu ý 2 case này thì nhớ exit để thoát chương trình, không chạy if cuối cùng
# elif (userinput == 1 and botinput == 3):
#     print('{0} Thắng {1}'.format(dict[userinput], dict[botinput]))

# elif (userinput == 3 and botinput == 1):
#     print('{0} Thua {1}'.format(dict[userinput], dict[botinput]))

# # -------------------------------------------------------------
# # 2. Trong trường hợp bình thường thì lớn hơn thắng, bé hơn thua
# elif (userinput > botinput):
#     print('{0} Thắng {1}'.format(dict[userinput], dict[botinput]))
# else:
#     print('{0} Thua {1}'.format(dict[userinput], dict[botinput]))
