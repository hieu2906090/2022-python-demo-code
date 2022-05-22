import d18.input_utils as input_utils

cauTB = 'Mời bạn nhập giá điện theo định dạng Khoảng,Giá'
dsKey = ['khoang', 'gia']

khoangGiaDict = input_utils.nhapNhieuThongTinVoiWhile(
    cauThongBao=cauTB, danhSachKey=dsKey)

print('Khoảng giá điện nhập vào là: {0}'.format(khoangGiaDict.__str__()))
