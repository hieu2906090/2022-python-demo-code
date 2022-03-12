# LIST BÀI TẬP EXERCISE

## I. DATA STRUCTURE MODULE

## II. CONTROL FLOWS MODULE (IF, FOR, WHILE)

**BT1.** In kết quả trò chơi oẳn tù tì.
YC1 (BASIC): Người dùng nhập búa, kéo, bao theo định dạng số cho trước (3,2,1)
-> Chương trình tự random ra số ngẫu nhiên trong khoảng (1->3)
-> Nếu 2 số này = nhau -> In ra "HOÀ"
-> Nếu búa > kéo > bao > búa thì in ra "THẮNG"
-> Ngược lại là "THUA"
YC2 (ADV1): Đưa vào hỏi người dùng có muốn chơi tiếp không -> C: chơi tiếp -> K: không chơi nữa (out chương trình)
YC3 (ADV2): Lưu lại số lần chơi và số lần thắng của người dùng -> In ra tỷ lệ chiến thắng

**BT2.** Tương tự BT1 nhưng thay vì oẳn tù tì thì chơi trò "Guess the number"
YC1 (BASIC): Người dùng chọn trong khoảng 1 -> 10
-> Máy cũng chọn trong khoảng 1 -> 10
-> Nếu 2 số này bằng nhau thì in ra "CHÍNH XÁC"
-> Không thì "TIẾC QUÁ, THỬ LẠI SAU"
YC2 (ADV1): Đưa vào hỏi người dùng có muốn chơi tiếp không -> C: chơi tiếp -> K: không chơi nữa (out chương trình)
YC3 (ADV2): Tương tự YC2 nhưng lưu lại số lần chơi và số lần chính xác

**BT9.** Guess the number (ver2): Người dùng chọn sẵn 1 số bất kỳ từ 0 -> 100. Máy đoán 1 số. Có 3 trường hợp xảy ra (cao hơn, bằng, thấp hơn):
-> Nếu cao hơn hoặc thấp hơn thì cho máy đoán lại
-> Nếu bằng thì dừng chương trình và in ra số lần máy tính mất để đoán đúng số
Ví Dụ: Số phải đoán là 51
L1. AI đoán 100 -> Cao hơn
L2. AI đoán 1 -> Thấp hơn
... n lần
Ln. AI đoán 50 -> Đúng
-> Thoát chương trình + in ra số lần (n lần)

---

**BT3.** In các số nguyên tố (số chỉ chia hết cho 1 và chính nó) từ 1 -> số nhập vào

**BT4.** In các số trong dãy Fibonacci

**BT5.** Tính giai thừa của 1 số (vd số 5 thì 5! là 5*4*3*2*1 = 120)

**BT6.** Tính tổng các số là số lẻ trong 1 list (hoặc ngược lại, số chẵn)
Hint: Phép chia lấy phần dư (hay còn gọi là modulo - gọi tắt là mod). Nếu mod là 0 tức chia hết. Vd 4 % 2 = 0 || 3 % 2 = 1

**BT7.** Tính tổng các số ở vị trí chẵn/lẻ của 1 list
Hint: list[1::2] -> lấy dãy mới bắt đầu từ vị trí số 1 kèm theo bước nhảy là 2 -> idx 1,3,5,7

**BT8.** Trò chơi HangMan: Nguyên tắc là random chọn 1 dãy từ -> chọn ra 1 từ + ẩn đi và ký tự trong đó
-> Người dùng đoán từng từ + Nếu Đúng: Ok pass qua và ko trừ điểm (số điểm là số từ ẩn đi chẳng hạn) + Nếu Sai: Trừ điểm
-> Điều kiện kết thúc chương trình: + Điều kiện thắng: - Đoán được tất cả từ - Điểm không = 0 + Điều kiện thua: - Điểm = 0
