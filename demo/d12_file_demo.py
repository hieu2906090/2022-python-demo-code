# file = open('./d12-file/input.txt', 'r')
# for line in file:
#     print(line)

# ###

# file = open('./d12-file/input.txt', 'r')
# lines = file.readlines()
# for line in lines:
#     print(line)

# ###

file = open('./d12-file/input.txt', 'w')
content = """
    Test thử write vào 1 file
    Nguyễn Quang Hiếu
"""

file.write(content)

file.close()
