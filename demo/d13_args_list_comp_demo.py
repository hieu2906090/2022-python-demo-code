import math
from random import randint

# def testFunction(*kwargs):  # arguments == parameters
#     print(kwargs)

# List comprehension


def testFunc(i):
    return i*i


def hamTinhTichPhanTrenI(i):
    return math.sin(i)


# annonymous function (ngôn ngữ #) == lambda function (python)
testArr = [(lambda i, ii: i*ii)(i, hamTinhTichPhanTrenI(i))
           for i in range(1, 100)]

# first class function
# testArr = [testFunc(i)
#            for i in range(1, 100)]


def testFunc(x): return math.cos(x)


print(testArr)


# print(testFunc(10, 1000))

# nameArr = 'anh hieu, anh toan, anh tien'.split(',')
# print(nameArr)
