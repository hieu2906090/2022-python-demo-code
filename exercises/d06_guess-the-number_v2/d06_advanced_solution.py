import random

# -------------------------------------------------------------
# I. VER1: Guess theo kiểu cứ tăng lên 1 hoặc giảm 1
# -------------------------------------------------------------


def run_ct_v1(numberOfGuessing, guessingNumber, correctNumber):
    # -------------------------------------------------------------
    # II. PHẦN LOGIC CHÍNH CỦA CHƯƠNG TRÌNH
    # -------------------------------------------------------------
    numberOfGuessing += 1
    if (guessingNumber > correctNumber):
        # 1. Logic chạy khi giá trị là cao hơn
        # 1.1. Khi cao hơn thì random lại trong khoảng guessingNumber -> 100
        # print('Giá trị máy đoán {0} là cao hơn giá trị bạn chọn ({1})!'.format(
        #     guessingNumber, correctNumber))
        guessingNumber -= 1
    elif (guessingNumber < correctNumber):
        # 2. Logic chạy khi giá trị là thấp hơn
        # 2.1. Khi cao hơn thì random lại trong khoảng 0 -> guessingNumber
        # print('Giá trị máy đoán {0} là thấp hơn giá trị bạn chọn ({1})!'.format(
        #     guessingNumber, correctNumber))
        guessingNumber += 1

    return numberOfGuessing, guessingNumber

# -------------------------------------------------------------
# II. VER2: Guess theo kiểu random trong khoảng từ 0 -> guess hoặc guess -> 100
# -------------------------------------------------------------


def run_ct_v2(numberOfGuessing, guessingNumber, correctNumber):
    # -------------------------------------------------------------
    # II. PHẦN LOGIC CHÍNH CỦA CHƯƠNG TRÌNH
    # -------------------------------------------------------------
    numberOfGuessing += 1
    if (guessingNumber > correctNumber):
        # 1. Logic chạy khi giá trị là cao hơn
        # 1.1. Khi cao hơn thì random lại trong khoảng guessingNumber -> 100
        # print('Giá trị máy đoán {0} là cao hơn giá trị bạn chọn {1}!'.format(
        #     guessingNumber, correctNumber))
        guessingNumber = random.randint(0, guessingNumber)
    elif (guessingNumber < correctNumber):
        # 2. Logic chạy khi giá trị là thấp hơn
        # 2.1. Khi cao hơn thì random lại trong khoảng 0 -> guessingNumber
        # print('Giá trị máy đoán {0} là thấp hơn giá trị bạn chọn ({1})!'.format(
        #     guessingNumber, correctNumber))
        guessingNumber = random.randint(guessingNumber, 100)

    return numberOfGuessing, guessingNumber

# -------------------------------------------------------------
# III. VER3: Guess trong khoảng 1/2
# -------------------------------------------------------------


def run_ct_v3(numberOfGuessing, guessingNumber, correctNumber):
    # -------------------------------------------------------------
    # II. PHẦN LOGIC CHÍNH CỦA CHƯƠNG TRÌNH
    # -------------------------------------------------------------
    numberOfGuessing += 1
    if (guessingNumber > correctNumber):
        # 1. Logic chạy khi giá trị là cao hơn
        # 1.1. Khi cao hơn thì random lại trong khoảng thấp hơn tức 1/2 guessing -> guessing
        # print('Giá trị máy đoán {0} là cao hơn giá trị bạn chọn {1}!'.format(
        #     guessingNumber, correctNumber))
        guessingNumber = random.randint(
            round(guessingNumber/2), guessingNumber)
    elif (guessingNumber < correctNumber):
        # 2. Logic chạy khi giá trị là thấp hơn
        # 2.1. Khi thấp hơn thì random lại trong khoảng từ guessing -> (100 - guessing) /2
        # print('Giá trị máy đoán {0} là thấp hơn giá trị bạn chọn ({1})!'.format(
        #     guessingNumber, correctNumber))
        guessingNumber = random.randint(
            guessingNumber, guessingNumber + round((100 - guessingNumber)/2))

    return numberOfGuessing, guessingNumber

# -------------------------------------------------------------
# IV. VER4: Binary Search
# -------------------------------------------------------------


def run_ct_binary(numberOfGuessing, guessingNumber, correctNumber, **kwargs):
    min, max = kwargs['min'], kwargs['max']
    # print('CALLED MIN({0}) MAX({1}), GUESS ({2})'.format(
    #     min, max, guessingNumber))
    # -------------------------------------------------------------
    # II. PHẦN LOGIC CHÍNH CỦA CHƯƠNG TRÌNH
    # -------------------------------------------------------------
    numberOfGuessing += 1
    # 1. Khi số guess là lớn hơn thì cần random trong khoảng 1/2 của min -> guess (đồng thời set max là guess)
    if (guessingNumber > correctNumber):
        max = guessingNumber - 1
    # 2. Khi là bé hơn thì cần random trong khoảng 1/2 của guess -> max (đồng thời set min là guess)
    elif (guessingNumber < correctNumber):
        # 2. Logic chạy khi giá trị là thấp hơn
        min = guessingNumber + 1

    guessingNumber = round((max + min)/2)

    return numberOfGuessing, guessingNumber, min, max


# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------
dict_func = {1: run_ct_v1, 2: run_ct_v2, 3: run_ct_v3, 4: run_ct_binary}


def run_hoc_version(verInput, run_version_func, correctNumber):
    numberOfGuessing = 0
    guessingNumber = 1
    min = 0
    max = 100

    while guessingNumber != correctNumber:
        if (verInput != 4):
            numberOfGuessing, guessingNumber = run_version_func(
                numberOfGuessing, guessingNumber, correctNumber)
        else:
            numberOfGuessing, guessingNumber, min, max = run_version_func(
                numberOfGuessing, guessingNumber, correctNumber, min=min, max=max)
    # -------------------------------------------------------------
    # III. IN RA KẾT QUẢ
    # -------------------------------------------------------------

    print('Ver {2} Máy đoán trúng giá trị {0} sau {1} lần!'.format(
        guessingNumber, numberOfGuessing, verInput))

# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------


def test_algo_run_efficiency(correctNumber):
    for k, v in dict_func.items():
        verInput = int(k)
        run_hoc_version(verInput, dict_func[verInput], correctNumber)
    print('Bạn có muốn tiếp tục: (C) Có, (K) Không')
    userInput = input()
    return userInput


def main_run():
    userInput = 'C'
    while userInput != 'K':
        print('Hãy chọn 1 số là giá trị bạn mong muốn!')
        correctNumber = int(input())
        userInput = test_algo_run_efficiency(correctNumber)


main_run()
