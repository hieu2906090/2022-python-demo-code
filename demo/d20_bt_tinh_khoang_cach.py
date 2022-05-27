import d20.input_utils as input_utils
from d20.khoang_cach_utils import duyetQuaListToaDoDeTinhKhoangCach, timSoLonNhatNhoNhatTuDanhSach

if __name__ == '__main__':
    # I. NHẬP LIỆU DANH SÁCH KHOẢNG CÁCH VÀO
    cauThongBao = 'Mời bạn nhập toạ độ dạng x,y'
    listToaDo = input_utils.nhapNhieuThongTinVoiWhile(
        cauThongBao, 1, input_utils.traThongTinTheoDSInt)
    print('Danh sách toạ độ là: {0}'.format(listToaDo.__str__()))

    # II. TÍNH TOẠ ĐỘ DỰA TRÊN DANH SÁCH ĐÃ NHẬP VÀO
    listKhoangCach = duyetQuaListToaDoDeTinhKhoangCach(listToaDo)
    soMin, soMax = timSoLonNhatNhoNhatTuDanhSach(listKhoangCach)

    # III. IN KẾT QUẢ Ở BƯỚC II RA MÀN HÌNH
    print('Danh sách khoảng cách điểm là {0} \n Số lớn nhất là: {2} \n Số nhỏ nhất là: {1}'.format(
        listKhoangCach, soMin, soMax))
