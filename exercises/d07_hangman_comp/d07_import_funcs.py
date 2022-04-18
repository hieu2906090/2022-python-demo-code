import random

'''
    Mục tiêu của phần này là phải ẩn được 70% hoặc 80% (số phần trăm do mình quy định)
    số ký tự của 1 từ cho trước (từ do mình nhập vào)
    
    BTVN: Viết hàm nhận vào 2 tham số: từ + % ký tự muốn ẩn đi -> in ra và trả về từ mới
    được ẩn đi. Ví dụ beautiful -> b__ut__l
'''


def initHiddenWordByPercent(word, percent):
    '''
        @params word: từ cần hide
        @params percent: % 1 từ cần hide đi
        return hiddenWord, hiddenWordArr, hiddenWordIdxArr
    '''
    # -------------------------------------------------------------
    # Bước 1: Chuyển chuỗi string thành dạng list (để có thể sử dụng hàm thao tác với list)
    numOfHideChars = round(percent * len(word))
    wordArr = [c for c in word]

    # -------------------------------------------------------------
    # Bước 2: Tạo ra list các index cần random (không trùng lắp). List này có số phần tử bằng với số ký tự cần ẩn đi
    tempIdxArr = []

    def checkRandomList():
        while True:
            randomNo = random.randint(0, len(word) - 1)
            if (randomNo in tempIdxArr):
                continue
            else:
                tempIdxArr.append(randomNo)
                return randomNo

    listRandom = [checkRandomList() for i in range(0, numOfHideChars)]

    # -------------------------------------------------------------
    # Bước 3: Duyệt qua list các vị trí ngẫu nhiên ở trên và thay thế
    # list ký tự bằng ký tự '_' đồng thời đưa vào dictionary cặp vị trí - ký tự
    # đã thay đổi
    hWordDict = {}

    for idx in listRandom:
        hWordDict[idx] = wordArr[idx]
        wordArr[idx] = "_"

    hiddenWord = ''.join(wordArr)

    # -------------------------------------------------------------
    # Bước 4: Trả về kết quả
    return hiddenWord, hWordDict

# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------
# TEST HÀM (SỬ DỤNG IF NAME = MAIN)


def rebuildHiddenWord(hWord, character, idxArr):
    '''
        @params hWord: từ mà người dùng đoán
        @params character: mảng chứa ký tự bị hide đi
        @params idxArr: mảng chứa vị trí idx của ký tự bị ẩn
        return rebuildWord
    '''
    # Bước 1. Kiểm trả mảng idxArr
    rebuildWord = ''
    fullHWordArr = [c for c in hWord]
    if (len(idxArr) > 0):
        for idx in idxArr:
            fullHWordArr[idx] = character
        rebuildWord = rebuildWord.join(fullHWordArr)

    return rebuildWord


def compareGuessingWithArr(guessingChar, hWordDict):
    '''
        @params guessingChar: ký tự mà người dùng đoán
        @params hWordDict: mảng chứa ký tự bị hide đi
        return guessingChar, idxInWordArr: trả về ký tự đoán + mảng chứa các vị trí của ký tự đó
    '''
    # Bước 1: kiểm tra xem từ cần đoán có nằm trong hWordDict hay không
    idxInWordArr = [k for k, v in hWordDict.items() if v == guessingChar]
    if (len(idxInWordArr) > 0):
        for idx in idxInWordArr:
            del hWordDict[idx]
        return guessingChar, idxInWordArr

    # Bước 2: Trả về mặc định mảng [] nếu không có
    return guessingChar, idxInWordArr


if (__name__ == '__main__'):
    hWord, hWordDict = initHiddenWordByPercent('beautiful', 0.6)
    # -------------------------------------------------------------
    # Phần logic lặp lại khi người dùng nhập vào 1 từ
    guessingChar, idxArr = compareGuessingWithArr('u', hWordDict)
    rebuildWord = rebuildHiddenWord(hWord, guessingChar, idxArr)

    print(idxArr, hWord, rebuildWord, hWordDict)
