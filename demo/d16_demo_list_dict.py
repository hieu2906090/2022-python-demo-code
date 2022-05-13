dsHocSinh = [
    {'ho': 'Nguyen', 'ten': 'Hieu', 'tuoi': 18, 'lop': '12A1'},
    {'ho': 'Nguyen', 'ten': 'Tin', 'tuoi': 18, 'lop': '12A2'},
    {'ho': 'Nguyen', 'ten': 'Trong', 'tuoi': 18, 'lop': '12A3'},
    {'ho': 'Nguyen', 'ten': 'Truong', 'tuoi': 18, 'lop': '12A4'},
]

for thongTinHocSinh in dsHocSinh:
    print('Thông tin học sinh: Tên: {0}, Tuổi: {1}, Lớp: {2}'.format(
        thongTinHocSinh['ten'], thongTinHocSinh['tuoi'], thongTinHocSinh['lop']))
