print('Mời bạn nhập tiền điện 12 tháng, cách nhau bởi dấu ","')
tienDien = input()
tienDienList = tienDien.split(',')
tienDienConvertList = []

for item in tienDienList:
    tienDienConvertList.append(int(item))
print('Tiền điện bạn nhập vào là: {0}, {1}'.format(
    tienDienConvertList, len(tienDienConvertList)))


file = open('test-input.txt', 'w')

content = ' '.join(tienDienList)

file.write(content)

file.close()
