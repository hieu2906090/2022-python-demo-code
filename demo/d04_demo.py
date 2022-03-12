'''
    1: Búa
    2: Kéo
    3: Bao
    Logic1: Búa > Kéo, Kéo > Bao, Bao > Búa && ==
    Logic2: -> hiện cho user nhập input
            -> so sánh userinput với botinput theo logic1 
            -> in ra kết quả trả về của logic1

    --> def hàm cho logic1
    --> def hàm chạy cho logic1 trong đó nhận vào userinput và botinput
    
    def logic1(userinput, botinput)
        return về kết quả hoặc print ra kết quả
'''
import random

dict = {1: 'Búa', 2: 'Kéo', 3: 'Bao'}


print("Mời bạn chọn: (3) Búa, (2) Kéo, (1) Bao")
userinput = input()
botinput = random.randint(1, 3)
# print('Người dùng chọn giá trị: {0}. Máy chọn giá trị: {1}'.format(
#     dict[int(userinput)], dict[botinput]))

# -------------------------------------------------------------
# Case HOÀ
if (int(userinput) == botinput):
    print('Hoà')
    exit()

# -------------------------------------------------------------
# Case BAO: Mặc định nếu bé hơn thì thua nhưng chỉ có trường hợp là BAO bé hơn là thắng
if (int(userinput) == 3 and botinput == 1):
    print('Bao thắng Búa')

if (int(userinput) == 1 and botinput == 3):
    print('Búa thua Bao')

# -------------------------------------------------------------
# Case Bình thường: Trong mọi trường hợp thì bé hơn là thắng, lớn hơn là thua
if (int(userinput) < botinput):
    print('Người thắng. Người chọn: {0}. Máy chọn: {1}'.format(
        dict[int(userinput)], dict[botinput]))
else:
    print('Máy thắng. Người chọn: {0}. Máy chọn: {1}'.format(
        dict[int(userinput)], dict[botinput]))
