import random


def taoUserVaBotInput():
    print("Mời bạn chọn: (3) Búa, (2) Kéo, (1) Bao")
    userinput = int(input())
    # print(type(userinput))
    botinput = random.randint(1, 3)
    return userinput, botinput


def xuLyLogicThangThua(userinput, botinput, dict, soLanThang):
    # -------------------------------------------------------------
    # 0. Trường hợp hoà
    if (userinput == botinput):
        chuoiKetQua = "Hoà"

    # -------------------------------------------------------------
    # 1. Hai trường hợp không nằm trong mẫu lớn hơn thì thắng (bé hơn thì thua)
    # Lưu ý 2 case này thì nhớ exit để thoát chương trình, không chạy if cuối cùng
    elif (userinput == 1 and botinput == 3):
        soLanThang += 1
        chuoiKetQua = '{0} Thắng {1}'.format(dict[userinput], dict[botinput])

    elif (userinput == 3 and botinput == 1):
        chuoiKetQua = '{0} Thua {1}'.format(dict[userinput], dict[botinput])

    # -------------------------------------------------------------
    # 2. Trong trường hợp bình thường thì lớn hơn thắng, bé hơn thua
    elif (userinput > botinput):
        soLanThang += 1
        chuoiKetQua = '{0} Thắng {1}'.format(dict[userinput], dict[botinput])
    else:
        chuoiKetQua = '{0} Thua {1}'.format(dict[userinput], dict[botinput])

    return chuoiKetQua, soLanThang
