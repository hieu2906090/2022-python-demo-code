# VARIABLE SCOPE
a = 'Tin'


def main():
    global a
    a = 'Hieu'
    print('a trong ham main la: ' + a)


main()
print('a ở ngoài là: ' + a)
