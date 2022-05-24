import d19.input_utils as input_utils
import d19.gia_dien_utils as gia_dien_utils

# I. NHẬP INPUT CÁC THÔNG TIN ĐẦU VÀO
bieuGiaGlobal = input_utils.nhapNhieuThongTinVoiWhile('Nhập biểu giá theo format giá cận dưới, giá cận trên, giá điện', [
    'chan_duoi', 'chan_tren', 'gia_dien'])

danhSachDienTieuThu = input_utils.traThongTinTheoDS(
    'Nhập giá điện tiêu thụ theo format tháng1,tháng2,tháng3...')

print('Biểu giá điện bạn nhập vào là: {0}'.format(bieuGiaGlobal.__str__()))
print('Giá điện tiêu thụ bạn nhập vào là: {0}'.format(
    danhSachDienTieuThu.__str__()))

# II. TÍNH TOÁN VÀ TRẢ VỀ KẾT QUẢ
dsTienDienHangThang = gia_dien_utils.tinhGiaTienDienTheoBieuGia(
    bieuGiaGlobal, danhSachDienTieuThu)
print('Kết quả sau khi tính ra giá điện phải trả là: {}'.format(
    dsTienDienHangThang.__str__()))
