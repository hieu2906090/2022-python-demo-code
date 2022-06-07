# I. TỔ CHỨC LƯU TRỮ DỮ LIỆU
tenBien = 'asdfasdfasdf'
duLieuStr = 'asdfasdfasdfasdf'
duLieuInt = 10234234234
duLieuFloat = 10.131123123
duLieuBoolean = True


def duLieuObject(x): return x**2


duLieuList = [1, 's', lambda x: x**2, (1, 2), duLieuObject, [123, 321]]
duLieuDict = {'key': duLieuList}

testItem = 's'
if (testItem in duLieuList):
    print('Co s trong danh sach')
# print(duLieuDict['key'])

# II. CÚ PHÁP LIÊN QUAN HỖ TRỢ CHO GIẢI THUẬT
# 1. IF
if 10 > 2:
    print('Dieu kien nay luon dung')

if 10 > 2 and 3 > 2:
    print('Dieu kien nay luon dung')

# 1.1. OPERATOR

# 1.1.2. Comparison Operators

# 1.1.3. Logical Operators

# 2. FOR
for item in duLieuList:
    # print(item)
    pass

# for item, idx in enumerate(duLieuList):
#     print(idx, item)

# for i in range(1, 10, 2):
#     print(i)

# for i in range(10, 1, -2):
#     print(i)

testDict = {'k1': 123, 'k2': 123123, 'k3': 'asdfasdf'}

for (k, v) in testDict.items():
    print(k, v)

# 3. WHILE
i = 1
while i < 10:
    print('con chay tiep', i)
    i += 1

while True:
    print('con chay tiep')
    i += 1
    if (i == 20):
        break

# 4. FUNCTION DECLARATION


def tenHam(tham_so1, tham_so2):
    return tham_so1 + tham_so2


testHam = tenHam(1, 10)

print(testHam)

# 5. INPUT
userInput = input().split(',')
print(userInput)
