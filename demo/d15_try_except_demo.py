# userInput = []
# try:
#     userInput = [int(i) for i in input().split()]
# except:
#     userInput = []

# print('Người dùng nhập vào: {}'.format(userInput))

# -------------------------------------------------------------
# userInput = input()
# for i in userInput:
#     print(i)
# -------------------------------------------------------------

userInput = input().split()
userInputTemp = []

for i in userInput:
    # tempI = int(i)
    # userInputTemp.append(tempI)
    try:
        tempI = int(i)
        userInputTemp.append(tempI)
    except:
        continue

print('Người dùng nhập vào: {}'.format(userInputTemp))
