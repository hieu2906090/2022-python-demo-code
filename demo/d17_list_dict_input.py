import d17.input_utils as input_utils
import d17.tinh_hoc_luc_utils as hoc_luc_utils

thongTinHSList = input_utils.nhapThongTinCuaNhieuHocSinh()

tempTTHSList = []
# for ttHs in thongTinHSList:
# newTTHS = hoc_luc_utils.xacDinhHocLucCua01Hs(ttHs)
# tempTTHSList.append(newTTHS)

tempTTHSList = list(map(hoc_luc_utils.xacDinhHocLucCua01Hs, thongTinHSList))

print('Thông tin bạn nhập vào là: ' + tempTTHSList.__str__())

dictTemp = [
    {'name': 'Hieu', 'lop': 'A1', 'diem_tb': 6.7, 'hoc_luc': 'Giỏi'},
    {'name': 'Tin', 'lop': 'A2', 'diem_tb': 7.5, 'hoc_luc': 'Giỏi'}
]
