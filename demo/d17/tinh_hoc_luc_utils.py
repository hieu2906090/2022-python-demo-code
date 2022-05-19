def xacDinhHocLucCua01Hs(ttHs):
    '''
        Hàm này nhận vào thông tin học sinh dưới dạng là:
        {'name': ..., 'diem_tb': ..., 'lop': ...}
        Và trả về thông tin học sinh có thêm 1 key là học lực
        {'name': ..., 'diem_tb': ..., 'lop': ..., 'hoc_luc': 'XS|Giỏi|Khá|TB|Kém'}
    '''
    # Logic xác định học lực dựa trên thông tin điểm trong dict ttHs
    # -> ttHs['diem_tb']
    if(ttHs['diem_tb'] < 5):
        ttHs['hoc_luc'] = 'Kém'
    if(ttHs['diem_tb'] >= 5 and ttHs['diem_tb'] < 7):
        ttHs['hoc_luc'] = 'Trung Bình'
    if(ttHs['diem_tb'] >= 7 and ttHs['diem_tb'] < 8):
        ttHs['hoc_luc'] = 'Khá'
    if(ttHs['diem_tb'] >= 8 and ttHs['diem_tb'] < 9):
        ttHs['hoc_luc'] = 'Giỏi'
    if(ttHs['diem_tb'] > 9):
        ttHs['hoc_luc'] = 'XS'

    return ttHs
