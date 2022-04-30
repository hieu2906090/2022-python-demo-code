# P1: Phần đọc input người dùng
print('Mời bạn nhập tiền điện 12 tháng, cách nhau bởi dấu ","')
tienDien = input()
tienDienList = tienDien.split(',')
tienDienConvertList = []

# P2: Phần convert input từ dạng chuỗi sang số
for item in tienDienList:
    tienDienConvertList.append(int(item))

print('Tiền điện bạn nhập vào là: {0}, {1}'.format(
    tienDienConvertList, len(tienDienConvertList)))

# P3: Phần logic chính để xác định yêu cầu bài toán

# P4: Phần đọc ghi file để in kết quả tiền điện
file = open('test-input.txt', 'w')

content = ' '.join(tienDienList)

file.write(content)

file.close()
