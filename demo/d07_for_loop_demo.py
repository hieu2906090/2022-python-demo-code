import random

# -------------------------------------------------------------
# I. FOR LOOOP
# 1. In xuôi, in ngược
print(' I.1 --------------------------------------------------------------')
print(' --> In xuôi')
for i in range(1, 10, 2):
    print(i)

print(' --> In ngược')
for i in range(10, 1, -2):
    print(i)

# 2. For in ra phần tử trong dictionary
print(' I.2 --------------------------------------------------------------')
loopDict = {'k1': 1, 'k2': 2, 'k3': 3}
for key, value in loopDict.items():
    print('Key {k} có value là: {v}'.format(k=key, v=value))

# 3. For in ra phần tử trong list
print(' I.3 --------------------------------------------------------------')
loopList = [1, 2, 3, 'STR']
for item in loopList:
    print(item)

for idx, item in enumerate(loopList):
    print('Phần tử tại index {i} có giá trị {val}'.format(i=idx, val=item))

for idx in range(0, len(loopList)):
    print('Phần tử tại index {i} có giá trị {val}'.format(
        i=idx, val=loopList[idx]))
# -------------------------------------------------------------
# II. LIST
# 1. Khai báo 1 list
print('II.1 --------------------------------------------------------------')
arr1 = [1, 2, 3, 'STR', {'dict1': 'Chuoi'}]

# 2. Gán hoặc tham chiếu tới giá trị của list
arr1[0] = 1000

# 3. Một số hàm thông dụng với list
arr2 = arr1.__reversed__()
arr3 = arr1.copy()
arr1.append(arr3)
arr1.pop(4)

print('--> Chuỗi arr1: ' + str(arr1))
print('--> Chuỗi arr2: ' + str(arr2))
print('--> Chuỗi arr3: ' + str(arr3))

# 4. Kiểm tra phần tử có trong list
if (1000 in arr1):
    print('Có giá trị 1 trong list')
else:
    print('Không có giá trị 1 trong list')

# -------------------------------------------------------------
# III. LIST COMPREHENSION
# 1. Trả về list gồm 100 số bất kỳ trong khoảng 1 -> 10
print('III.1 --------------------------------------------------------------')
listNum = [random.randint(1, 10) for i in range(0, 100)]
print('--> 100 số bất kỳ: ' + str(listNum))

# 2. Trả về 100 ký tự bất kỳ ngẫu nhiên theo các ký tự xuất hiện trong từ beautiful
print('III.2 --------------------------------------------------------------')
str0 = 'beautiful'


def returnRandomChar(string):
    randomNumber = random.randint(0, 8)
    return string[randomNumber]


str1 = [returnRandomChar(str0) for i in range(0, 100)]
print('--> 100 ký tực bất kỳ của \'beautiful\': ' + str(str1))

# # count = 0
# # countHidden = 3

# # for idx, val in enumerate(str):
# #     print(idx, val)
# # for i in range(0, len(str)):
# #     print("Phần tử tại vị trí số ", i, "= ", str[i])


# 1. FOR
# 1.1. Chạy for với range: for item in range(start, stop, step):
# 1.2. Chạy for với dictionary: for key, value in {k:v}.items():
# 1.3. Chạy for với string: for character in 'string':
# 1.4. Chạy for với list: for item in list:
# 1.4.1. Chạy for với list kèm index:
# (a) for index, value in enumerate(list):

# 2. LIST
# 2.1. List là mảng gồm nhiều phần tử kiểu dữ liệu có thể khác nhau
# 2.2. Tham chiếu 1 phần tử list: list[idx]
# 2.3. List bắt đầu bằng phần từ số 0
# 2.4. Một số hàm thông dụng với list:
# (a) list.copy()
# (b) list.append(item)
# (c) list.pop()
# (d) list.pop(idx)
# (d) len(list)
# (a) ''.join(list)

# 3. LIST COMPREHENSION
# (b) ''.join([str(item) for item in list])
# (b) for index in range(0, len(list)): --> để tham chiếu giá trị thì dùng list[idx]
