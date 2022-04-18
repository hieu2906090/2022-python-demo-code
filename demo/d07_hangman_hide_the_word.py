import random

'''
    Mục tiêu của phần này là phải ẩn được 70% hoặc 80% (số phần trăm do mình quy định)
    số ký tự của 1 từ cho trước (từ do mình nhập vào)
    
    BTVN: Viết hàm nhận vào 2 tham số: từ + % ký tự muốn ẩn đi -> in ra và trả về từ mới
    được ẩn đi. Ví dụ beautiful -> b__ut__l
'''


def initRandomHiddenWord(word, percent):
    # -------------------------------------------------------------
    # Bước 1: Chuyển chuỗi string thành dạng list (để có thể sử dụng hàm thao tác với list)
    str1 = [c for c in word]

    tempArr = []

    # -------------------------------------------------------------
    # Bước 2: Tạo ra list các index cần random (không trùng lắp)
    # List này có số phần tử bằng với số ký tự cần ẩn đi

    def checkRandomList():
        while True:
            randomNo = random.randint(0, len(word) - 1)
            if (randomNo in tempArr):
                continue
            else:
                tempArr.append(randomNo)
                return randomNo

    soLuongTuBiAn = round(len(word) * percent)

    # KISS -> Keep It Simple & Short
    listRandom = [checkRandomList()
                  for i in range(0, soLuongTuBiAn)]

    # -------------------------------------------------------------
    # Bước 3: Duyệt qua list các vị trí ngẫu nhiên ở trên và thay thế
    # list ký tự bằng ký tự '_' đồng thời đưa vào dictionary cặp vị trí - ký tự
    # đã thay đổi
    hideDict = {}
    for idx in listRandom:
        hideDict[idx] = str1[idx]
        str1[idx] = "_"

    hideWord = ''.join(str1)

    return hideWord, hideDict


def nguoiChoiDoanKyTu(kyTuDoan, hideWord, hideDict):

    return hideWord, hideDict


hiWord, hiDict = initRandomHiddenWord('nationality', 0.6)
print(hiWord, hiDict)
print('Mời bạn đoán ký tự')
nguoiDungDoan = input()
hiWord, hiDict = nguoiChoiDoanKyTu(nguoiDungDoan, hiWord, hiDict)


# n___o__l_t_ -> đoán 'a'
# -> BINGO! có 2 chữ 'a'
# -> na___o_al_t_
# del dict[key]
# {5: 'n', 2: 't', 8: 'i', 10: 'y', 3: 'i'}
