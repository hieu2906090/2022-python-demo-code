from d06_print_function_solutions import run_ct_v1, run_ct_v2, run_ct_v3

dict_func = {1: run_ct_v1, 2: run_ct_v2, 3: run_ct_v3}


def run_one_version(func_to_run):
    userDec = 'T'
    numberOfGuessing = 0
    guessingNumber = 0
    func_to_run(
        userDec, numberOfGuessing, guessingNumber)


def main():
    userInput = 'C'
    while userInput != 'K':
        print('Mời bạn chọn các cách giải (1), (2), (3)?')
        verInput = int(input())
        run_one_version(dict_func[verInput])
        print('Bạn có muốn tiếp tục (C) Có, (K) Không?')
        userInput = input()


main()
