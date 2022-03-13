import random


def run_ct_v1(userInput, numberOfGuessing, guessingNumber):
    # -------------------------------------------------------------
    # II. PHẦN LOGIC CHÍNH CỦA CHƯƠNG TRÌNH
    # -------------------------------------------------------------
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


def run_ct_v2(userInput, numberOfGuessing, guessingNumber):
    # -------------------------------------------------------------
    # II. PHẦN LOGIC CHÍNH CỦA CHƯƠNG TRÌNH
    # -------------------------------------------------------------
    while userInput != 'D':
        numberOfGuessing += 1
        if (userInput == 'C'):
            # 1. Logic chạy khi giá trị là cao hơn
            # 1.1. Khi cao hơn thì random lại trong khoảng guessingNumber -> 100
            guessingNumber = random.randint(0, guessingNumber)
            print('Giá trị máy đoán {0} là (C) cao hơn (T) thấp hơn hay đã (D) đúng với giá trị bạn chọn?'.format(
                guessingNumber))
            userInput = input()
        elif (userInput == 'T'):
            # 2. Logic chạy khi giá trị là thấp hơn
            # 2.1. Khi cao hơn thì random lại trong khoảng 0 -> guessingNumber
            guessingNumber = random.randint(guessingNumber, 100)
            print('Giá trị máy đoán {0} là (C) cao hơn (T) thấp hơn hay đã (D) đúng với giá trị bạn chọn?'.format(
                guessingNumber))
            userInput = input()

    # -------------------------------------------------------------
    # III. IN RA KẾT QUẢ
    # -------------------------------------------------------------
    print('Máy đoán trúng giá trị {0} sau {1} lần!'.format(
        guessingNumber, numberOfGuessing))


def run_ct_v3(userInput, numberOfGuessing, guessingNumber):
    # -------------------------------------------------------------
    # II. PHẦN LOGIC CHÍNH CỦA CHƯƠNG TRÌNH
    # -------------------------------------------------------------
    while userInput != 'D':
        numberOfGuessing += 1
        if (userInput == 'C'):
            # 1. Logic chạy khi giá trị là cao hơn
            # 1.1. Khi cao hơn thì random lại trong khoảng thấp hơn tức 1/2 guessing -> guessing
            guessingNumber = random.randint(
                round(guessingNumber/2), guessingNumber)
            print('Giá trị máy đoán {0} là (C) cao hơn (T) thấp hơn hay đã (D) đúng với giá trị bạn chọn?'.format(
                guessingNumber))
            userInput = input()
        elif (userInput == 'T'):
            # 2. Logic chạy khi giá trị là thấp hơn
            # 2.1. Khi thấp hơn thì random lại trong khoảng từ guessing -> (100 - guessing) /2
            guessingNumber = random.randint(
                guessingNumber, guessingNumber + round((100 - guessingNumber)/2))
            print('Giá trị máy đoán {0} là (C) cao hơn (T) thấp hơn hay đã (D) đúng với giá trị bạn chọn?'.format(
                guessingNumber))
            userInput = input()

    # -------------------------------------------------------------
    # III. IN RA KẾT QUẢ
    # -------------------------------------------------------------
    print('Máy đoán trúng giá trị {0} sau {1} lần!'.format(
        guessingNumber, numberOfGuessing))
