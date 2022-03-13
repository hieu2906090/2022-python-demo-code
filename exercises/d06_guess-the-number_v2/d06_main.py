import random

# -------------------------------------------------------------
# I. KHAI BÁO BIẾN CẦN DÙNG
# -------------------------------------------------------------
userInput = 'C'
numberOfGuessing = 0
guessingNumber = 1

# -------------------------------------------------------------
# II. PHẦN LOGIC CHÍNH CỦA CHƯƠNG TRÌNH
# -------------------------------------------------------------
while userInput != 'D':
    numberOfGuessing += 1
    if (userInput == 'C'):
        # 1. Logic chạy khi giá trị là cao hơn
        # 1.1. Khi cao hơn thì random lại trong khoảng guessingNumber -> 100
        guessingNumber -= 1
        print('Giá trị máy đoán {0} là (C) cao hơn (T) thấp hơn hay đã (D) đúng với giá trị bạn chọn?'.format(
            guessingNumber))
        userInput = input()
    elif (userInput == 'T'):
        # 2. Logic chạy khi giá trị là thấp hơn
        # 2.1. Khi cao hơn thì random lại trong khoảng 0 -> guessingNumber
        guessingNumber += 1
        print('Giá trị máy đoán {0} là (C) cao hơn (T) thấp hơn hay đã (D) đúng với giá trị bạn chọn?'.format(
            guessingNumber))
        userInput = input()

# -------------------------------------------------------------
# III. IN RA KẾT QUẢ
# -------------------------------------------------------------
print('Máy đoán trúng giá trị {0} sau {1} lần!'.format(
    guessingNumber, numberOfGuessing))
