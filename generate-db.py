# Thông tin của MySQL
HOST = 'localhost' # Host của MySQL
USER = 'root' # Người dùng
PASSWORD = 'camnguyen' # Mật khẩu

cntTruong = 100 # Số dòng cần thêm vào bảng TRUONG
cntHS = 1000000 # Số dòng cần thêm vào bảng HS

# Danh sách 120 họ người Việt
Ho = ['Biện', 'Bành', 'Bùi', 'Bạch', 'Cao', 'Chiêm', 'Chu', 'Chung', 'Châu', 'Chế', 'Cù', 'Danh', 'Diệp', 'Doãn', 'Dư', 'Dương', 'Giang', 'Hoàng', 'Huỳnh', 'Hà', 'Hàn', 'Hàng', 'Hán', 'Hồ', 'Hồng', 'Hứa', 'Khưu', 'Khổng', 'Kim', 'Kiều', 'La', 'Lai', 'Liêu', 'Lâm', 'Lã', 'Lê', 'Lý', 'Lư', 'Lưu', 'Lương', 'Lại', 'Lỗ', 'Lộc', 'Lục', 'Lữ', 'Ma', 'Mai', 'Mã', 'Mạc', 'Mạch', 'Nghiêm', 'Nguyễn', 'Ngô', 'Ngụy', 'Nhan', 'Nhâm', 'Ninh', 'Phan', 'Phí', 'Phù', 'Phùng', 'Phương', 'Phạm', 'Quan', 'Quách', 'Quảng', 'Quế', 'Sùng', 'Sơn', 'Sầm', 'Sử', 'Thi', 'Thiều', 'Thái', 'Thân', 'Thạch', 'Thập', 'Tiêu', 'Trang', 'Triệu', 'Trà', 'Trác', 'Trình', 'Trưng', 'Trương', 'Trầm', 'Trần', 'Trịnh', 'Tào', 'Tô', 'Tôn', 'Tăng', 'Tạ', 'Tấn', 'Tất', 'Tống', 'Từ', 'Uông', 'Vi', 'Viên', 'Vàng', 'Vòng', 'Võ', 'Văn', 'Vũ', 'Vưu', 'Vương', 'Âu', 'Ôn', 'Ông', 'Đinh', 'Đoàn', 'Đàm', 'Đào', 'Đường', 'Đậu', 'Đặng', 'Đồng', 'Đổng', 'Đỗ']

# Danh sách 271 tên người Việt
Ten = ['An' ,'Anh' ,'Ban' ,'Bi' ,'Bách' ,'Bình' ,'Bích' ,'Bính' ,'Băng' ,'Bảo' ,'Bắc' ,'Bằng' ,'Can' ,'Chanh' ,'Chi' ,'Chánh' ,'Châu' ,'Chí' ,'Cát' ,'Công' ,'Cúc' ,'Cơ' ,'Cương' ,'Cường' ,'Cảnh' ,'Cầm' ,'Cửu' ,'Cựu' ,'Danh' ,'Dao' ,'Di' ,'Diễm' ,'Diệp' ,'Diệu' ,'Doanh' ,'Dung' ,'Duy' ,'Duyên' ,'Duyệt' ,'Dũng' ,'Dương' ,'Dần' ,'Dự' ,'Gia' ,'Giang' ,'Giao' ,'Giác' ,'Hiếu' ,'Hiền' ,'Hiển' ,'Hiệp' ,'Hiệu' ,'Hoa' ,'Hoàng' ,'Huy' ,'Huyên' ,'Huyền' ,'Huấn' ,'Huế' ,'Huệ' ,'Hy' ,'Hà' ,'Hào' ,'Hân' ,'Hòa' ,'Hùng' ,'Hưng' ,'Hương' ,'Hạc' ,'Hạnh' ,'Hải' ,'Hảo' ,'Hậu' ,'Hằng' ,'Hồng' ,'Hội' ,'Hợp' ,'Kha' ,'Khang' ,'Khanh' ,'Khiêm' ,'Khiết' ,'Khoa' ,'Khoá' ,'Khoáng' ,'Khuê' ,'Kháng' ,'Khánh' ,'Khôi' ,'Khải' ,'Kim' ,'Kiên' ,'Kiều' ,'Kiệm' ,'Kiệt' ,'Kỳ' ,'Kỷ' ,'Lam' ,'Lan' ,'Linh' ,'Liêm' ,'Liên' ,'Liễu' ,'Liệu' ,'Loan' ,'Long' ,'Luyện' ,'Luân' ,'Ly' ,'Lài' ,'Lâm' ,'Lạc' ,'Lệ' ,'Lịch' ,'Lộc' ,'Lợi' ,'Lụa' ,'Mai' ,'Mi' ,'Minh' ,'My' ,'Mão' ,'Mại' ,'Mạnh' ,'Mạo' ,'Mẫn' ,'Mỹ' ,'Nam' ,'Nga' ,'Nghi' ,'Nghĩa' ,'Nghệ' ,'Ngung' ,'Nguyên' ,'Nguyệt' ,'Ngân' ,'Ngạn' ,'Ngọc' ,'Ngự' ,'Nhi' ,'Nhiên' ,'Nhung' ,'Nhàn' ,'Nhâm' ,'Nhân' ,'Nhã' ,'Như' ,'Nhật' ,'Nhựt' ,'Nương' ,'Oanh' ,'Phi' ,'Phong' ,'Phát' ,'Phú' ,'Phúc' ,'Phương' ,'Phước' ,'Phượng' ,'Phụng' ,'Quang' ,'Quyên' ,'Quân' ,'Quý' ,'Quế' ,'Quốc' ,'Quỳnh' ,'Sang' ,'Soạn' ,'Sính' ,'Sĩ' ,'Sơn' ,'Sương' ,'Thanh' ,'Thi' ,'Thiên' ,'Thiện' ,'Thoa' ,'Thuyên' ,'Thuận' ,'Thy' ,'Thành' ,'Thái' ,'Thông' ,'Thùy' ,'Thúy' ,'Thơ' ,'Thư' ,'Thương' ,'Thượng' ,'Thảo' ,'Thắm' ,'Thắng' ,'Thịnh' ,'Thủy' ,'Tiên' ,'Tiến' ,'Tiềm' ,'Toàn' ,'Toại' ,'Trang' ,'Trinh' ,'Triết' ,'Trung' ,'Trà' ,'Trâm' ,'Trân' ,'Trí' ,'Trúc' ,'Trường' ,'Trọng' ,'Tuyết' ,'Tuyền' ,'Tuyển' ,'Tuấn' ,'Tuệ' ,'Tài' ,'Tâm' ,'Tân' ,'Tích' ,'Tín' ,'Tùng' ,'Tú' ,'Tăng' ,'Tước' ,'Tường' ,'Tạo' ,'Tấn' ,'Tế' ,'Tựu' ,'Uyên' ,'Vi' ,'Vinh' ,'Việt' ,'Vy' ,'Vân' ,'Văn' ,'Vĩ' ,'Vũ' ,'Vương' ,'Vọng' ,'Vỹ' ,'Xuyên' ,'Xuyến' ,'Xuân' ,'Xương' ,'Yên' ,'Yến' ,'Yểm' ,'Ái' ,'Ánh' ,'Ân' ,'Ý' ,'Đan' ,'Điều' ,'Đoàn' ,'Đào' ,'Đình' ,'Đính' ,'Đông' ,'Đăng' ,'Được' ,'Đại' ,'Đạt' ,'Đảm' ,'Đản' ,'Đậu' ,'Đối' ,'Độ' ,'Đức' ,'Ấn']

# Danh sách các quận, huyện và thành phố thuộc Thành phố Hồ Chí Minh
QuanHuyenHCM = ['Quận 1', 'Quận 3', 'Quận 4', 'Quận 5', 'Quận 6', 'Quận 7', 'Quận 8', 'Quận 10', 'Quận 11', 'Quận 12', 'Quận Bình Tân', 'Quận Bình Thạnh', 'Quận Gò Vấp', 'Quận Phú Nhuận', 'Quận Tân Bình', 'Quận Tân Phú', 'Thành phố Thủ Đức', 'Huyện Nhà Bè', 'Huyện Hóc Môn', 'Huyện Bình Chánh', 'Huyện Củ Chi', 'Huyện Cần Giờ']

# Danh sách các trường THPT và địa chỉ trường tại Thành phố Hồ Chí Minh
TruongHCM = [(1, "THPT Bình Chánh", "Huyện Bình Chánh, Thành phố Hồ Chí Minh"),(2, "THPT Đa Phước", "Huyện Bình Chánh, Thành phố Hồ Chí Minh"),(3, "THPT Lê Minh Xuân", "Huyện Bình Chánh, Thành phố Hồ Chí Minh"),(4, "THPT Năng Khiếu TDTT Huyện Bình Chánh", "Huyện Bình Chánh, Thành phố Hồ Chí Minh"),(5, "THPT Tân Túc", "Huyện Bình Chánh, Thành phố Hồ Chí Minh"),(6, "THPT Vĩnh Lộc B", "Huyện Bình Chánh, Thành phố Hồ Chí Minh"),(7, "THCS-THPT Thạnh An", "Huyện Cần Giờ, Thành phố Hồ Chí Minh"),(8, "THPT An Nghĩa", "Huyện Cần Giờ, Thành phố Hồ Chí Minh"),(9, "THPT Bình Khánh", "Huyện Cần Giờ, Thành phố Hồ Chí Minh"),(10, "THPT Cần Thạnh", "Huyện Cần Giờ, Thành phố Hồ Chí Minh"),(11, "THPT An Nhơn Tây", "Huyện Củ Chi, Thành phố Hồ Chí Minh"),(12, "THPT Củ Chi", "Huyện Củ Chi, Thành phố Hồ Chí Minh"),(13, "THPT Phú Hòa", "Huyện Củ Chi, Thành phố Hồ Chí Minh"),(14, "THPT Quang Trung", "Huyện Củ Chi, Thành phố Hồ Chí Minh"),(15, "THPT Tân Thông Hội", "Huyện Củ Chi, Thành phố Hồ Chí Minh"),(16, "THPT Trung Lập", "Huyện Củ Chi, Thành phố Hồ Chí Minh"),(17, "THPT Trung Phú", "Huyện Củ Chi, Thành phố Hồ Chí Minh"),(18, "THPT Bà Điểm", "Huyện Hóc Môn, Thành phố Hồ Chí Minh"),(19, "THPT Hồ Thị Bi", "Huyện Hóc Môn, Thành phố Hồ Chí Minh"),(20, "THPT Lý Thường Kiệt", "Huyện Hóc Môn, Thành phố Hồ Chí Minh"),(21, "THPT Bùi Thị Xuân", "Quận 1, Thành phố Hồ Chí Minh"),(22, "THPT Chuyên Trần Đại Nghĩa", "Quận 1, Thành phố Hồ Chí Minh"),(23, "THPT Lương Thế Vinh", "Quận 1, Thành phố Hồ Chí Minh"),(24, "THPT Năng Khiếu TDTT", "Quận 1, Thành phố Hồ Chí Minh"),(25, "THPT Ten Lơ Man", "Quận 1, Thành phố Hồ Chí Minh"),(26, "THPT Trưng Vương", "Quận 1, Thành phố Hồ Chí Minh"),(27, "THPT Diên Hồng", "Quận 10, Thành phố Hồ Chí Minh"),(28, "THPT Nguyễn An Ninh", "Quận 10, Thành phố Hồ Chí Minh"),(29, "THPT Nguyễn Du", "Quận 10, Thành phố Hồ Chí Minh"),(30, "THPT Nguyễn Khuyến", "Quận 10, Thành phố Hồ Chí Minh"),(31, "THPT Sương Nguyệt Anh", "Quận 10, Thành phố Hồ Chí Minh"),(32, "THPT Nam Kỳ Khởi Nghĩa", "Quận 11, Thành phố Hồ Chí Minh"),(33, "THPT Nguyễn Hiền", "Quận 11, Thành phố Hồ Chí Minh"),(34, "THPT Trần Quang Khải", "Quận 11, Thành phố Hồ Chí Minh"),(35, "THPT Thạnh Lộc", "Quận 12, Thành phố Hồ Chí Minh"),(36, "THPT Chinh", "Quận 12, Thành phố Hồ Chí Minh"),(37, "THPT Võ Toản", "Quận 12, Thành phố Hồ Chí Minh"),(38, "THPT Lê Quí Đôn", "Quận 3, Thành phố Hồ Chí Minh"),(39, "THPT Lê Thị Hồng Gấm", "Quận 3, Thành phố Hồ Chí Minh"),(40, "THPT Marie Curie", "Quận 3, Thành phố Hồ Chí Minh"),(41, "THPT Nguyễn Thị Diệu", "Quận 3, Thành phố Hồ Chí Minh"),(42, "THPT Nguyễn Thị Minh Khai", "Quận 3, Thành phố Hồ Chí Minh"),(43, "THPT Nguyễn Hữu Thọ", "Quận 4, Thành phố Hồ Chí Minh"),(44, "THPT Nguyễn Trãi", "Quận 4, Thành phố Hồ Chí Minh"),(45, "Phổ Thông Năng Khiếu, ĐHQG-HCM", "Quận 5, Thành phố Hồ Chí Minh"),(46, "PT Năng Khiếu Đại Học Quốc Gia", "Quận 5, Thành phố Hồ Chí Minh"),(47, "TH Thực Hành ĐHSP", "Quận 5, Thành phố Hồ Chí Minh"),(48, "THPT Chuyên Lê Hồng Phong", "Quận 5, Thành phố Hồ Chí Minh"),(49, "THPT Hùng Vương", "Quận 5, Thành phố Hồ Chí Minh"),(50, "THPT Trần Hữu Trang", "Quận 5, Thành phố Hồ Chí Minh"),(51, "THPT Trần Khai Nguyên", "Quận 5, Thành phố Hồ Chí Minh"),(52, "Trung Học Thực Hành Đại Học Sư Phạm TP.HCM", "Quận 5, Thành phố Hồ Chí Minh"),(53, "Trung Học Thực Hành Sài Gòn", "Quận 5, Thành phố Hồ Chí Minh"),(54, "THPT Bình Phú", "Quận 6, Thành phố Hồ Chí Minh"),(55, "THPT Mạc Đĩnh Chi", "Quận 6, Thành phố Hồ Chí Minh"),(56, "THPT Nguyễn Tất Thành", "Quận 6, Thành phố Hồ Chí Minh"),(57, "THPT Phạm Phú Thứ", "Quận 6, Thành phố Hồ Chí Minh"),(58, "THPT Lê Thánh Tôn", "Quận 7, Thành phố Hồ Chí Minh"),(59, "THPT Nam Sài Gòn", "Quận 7, Thành phố Hồ Chí Minh"),(60, "THPT Ngô Quyền", "Quận 7, Thành phố Hồ Chí Minh"),(61, "THPT Tân Phong", "Quận 7, Thành phố Hồ Chí Minh"),(62, "THPT Lương Văn Can", "Quận 8, Thành phố Hồ Chí Minh"),(63, "THPT Năng Khiếu TDTT Nguyễn Thị Định", "Quận 8, Thành phố Hồ Chí Minh"),(64, "THPT Ngô Gia Tự", "Quận 8, Thành phố Hồ Chí Minh"),(65, "THPT Nguyễn Văn Linh", "Quận 8, Thành phố Hồ Chí Minh"),(66, "THPT Tạ Quang Bửu", "Quận 8, Thành phố Hồ Chí Minh"),(67, "THPT Võ Văn Kiệt", "Quận 8, Thành phố Hồ Chí Minh"),(68, "THPT Gia Định", "Quận Bình Thạnh, Thành phố Hồ Chí Minh"),(69, "THPT Hoàng Hoa Thám", "Quận Bình Thạnh, Thành phố Hồ Chí Minh"),(70, "THPT Phan Đăng Lưu", "Quận Bình Thạnh, Thành phố Hồ Chí Minh"),(71, "THPT Thanh Đa", "Quận Bình Thạnh, Thành phố Hồ Chí Minh"),(72, "THPT Trần Văn Giàu", "Quận Bình Thạnh, Thành phố Hồ Chí Minh"),(73, "THPT Võ Thị Sáu", "Quận Bình Thạnh, Thành phố Hồ Chí Minh"),(74, "THPT Gò Vấp", "Quận Gò Vấp, Thành phố Hồ Chí Minh"),(75, "THPT Nguyễn Công Trứ", "Quận Gò Vấp, Thành phố Hồ Chí Minh"),(76, "THPT Nguyễn Trung Trực", "Quận Gò Vấp, Thành phố Hồ Chí Minh"),(77, "THPT Trần Hưng Đạo", "Quận Gò Vấp, Thành phố Hồ Chí Minh"),(78, "THPT Hàn Thuyên", "Quận Phú Nhuận, Thành phố Hồ Chí Minh"),(79, "THPT Phú Nhuận", "Quận Phú Nhuận, Thành phố Hồ Chí Minh"),(80, "THPT Quốc Tế Việt Úc", "Quận Phú Nhuận, Thành phố Hồ Chí Minh"),(81, "THPT Lý Tự Trọng", "Quận Tân Bình, Thành phố Hồ Chí Minh"),(82, "THPT Nguyễn Chí Thanh", "Quận Tân Bình, Thành phố Hồ Chí Minh"),(83, "THPT Nguyễn Thái Bình", "Quận Tân Bình, Thành phố Hồ Chí Minh"),(84, "THPT Nguyễn Thượng Hiền", "Quận Tân Bình, Thành phố Hồ Chí Minh"),(85, "THPT Thủ Khoa Huân", "Quận Tân Bình, Thành phố Hồ Chí Minh"),(86, "THPT Giồng Ông Tố", "Thành phố Thủ Đức, Thành phố Hồ Chí Minh"),(87, "THPT Thủ Thiêm", "Thành phố Thủ Đức, Thành phố Hồ Chí Minh"),(88, "THPT Long", "Thành phố Thủ Đức, Thành phố Hồ Chí Minh"),(89, "THPT Nguyễn Huệ", "Thành phố Thủ Đức, Thành phố Hồ Chí Minh"),(90, "THPT Nguyễn Văn Tăng", "Thành phố Thủ Đức, Thành phố Hồ Chí Minh"),(91, "THPT Phước Long", "Thành phố Thủ Đức, Thành phố Hồ Chí Minh"),(92, "Phổ Thông Năng Khiếu Thể Thao Olympic", "Thành phố Thủ Đức, Thành phố Hồ Chí Minh"),(93, "THPT Bình Chiểu", "Thành phố Thủ Đức, Thành phố Hồ Chí Minh"),(94, "THPT Đào Sơn Tây", "Thành phố Thủ Đức, Thành phố Hồ Chí Minh"),(95, "THPT Dương Văn Thì", "Thành phố Thủ Đức, Thành phố Hồ Chí Minh"),(96, "THPT Hiệp Bình", "Thành phố Thủ Đức, Thành phố Hồ Chí Minh"),(97, "THPT Linh Trung", "Thành phố Thủ Đức, Thành phố Hồ Chí Minh"),(98, "THPT Nguyễn Hữu Huân", "Thành phố Thủ Đức, Thành phố Hồ Chí Minh"),(99, "THPT Tam Phú", "Thành phố Thủ Đức, Thành phố Hồ Chí Minh"),(100, "THPT Thủ Đức", "Thành phố Thủ Đức, Thành phố Hồ Chí Minh")]
# Dictionary soNguoiTrung6SoDauCCCD có key là 6 chữ số đầu của CCCD, trả về số người có cùng 6 chữ số đầu đó
soNguoiTrung6SoDauCCCD = {}

# Cài đặt pymysql
import subprocess
import sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pymysql'])

# Thêm các thư viện cần thiết
import pymysql
import random

# Kết nối đến database TRUONGHOC1
connectTruongHoc1 = pymysql.connect(host = HOST, user = USER, password = PASSWORD, database = 'TRUONGHOC1')

# Tạo một đối tượng cursor
cursor = connectTruongHoc1.cursor()

# Cấu hình random
generator = random.Random()
generator.seed()

# --- Phát sinh 100 dòng dữ liệu cho bảng TRUONG ---
queryTruong = 'INSERT INTO TRUONG (MATR, TENTR, DCHITR) VALUE (%s, %s, %s)'
cursor.executemany(queryTruong, TruongHCM)
connectTruongHoc1.commit() # Cập nhật dữ liệu trường vào database

# Danh sách dữ liệu HS
batchHS = []
# Danh sách dữ liệu HOC
batchHOC = []

# --- Phát sinh 1 triệu dòng dữ liệu cho bảng HS ---
for maHS in range(1, cntHS + 1):
    rdHo = Ho[generator.randint(0, len(Ho) - 1)]  # rdHo là 1 họ ngẫu nhiên từ danh sách Ho
    rdTen = Ten[generator.randint(0, len(Ten) - 1)]  # rdTen là 1 tên ngẫu nhiên từ danh sách Ten

    # Random ngày tháng năm sinh
    rdNamSinh = generator.randint(1995, 2005)  # rdNamSinh là 1 năm sinh ngẫu nhiên từ 1980 đến 2004
    rdThangSinh = generator.randint(1, 12)  # rdThangSinh là 1 tháng sinh ngẫu nhiên từ 1 đến 12
    if rdThangSinh == 2:
        rdNgaySinh = generator.randint(1, 28)  # Nếu sinh vào tháng 2 thì ngày sinh ngẫu nhiên từ 1 đến 28
    else:
        rdNgaySinh = generator.randint(1, 30)  # Nếu sinh vào tháng khác tháng 2 thì ngày sinh ngẫu nhiên từ 1 đến 30

    # Random số CCCD
    rdGioiTinh = generator.randint(0, 1)  # rdGioiTinh là mã giới tính ngẫu nhiên, với 0 là nam và 1 là nữ
    rdMaTinh = generator.randint(1, 96)  # rdMaTinh là 1 số ngẫu nhiên từ 1 đến 96, đại diện cho Mã Tỉnh trong CCCD

    # 3 chữ số đầu là mã tỉnh
    cccd = str(rdMaTinh)
    if len(cccd) < 3:
        cccd = '0' * (3 - len(cccd)) + cccd  # Nếu chưa đủ 3 số thì bổ sung thêm các số 0 ở trước

    # 1 chữ số tiếp theo là mã giới tính và mã thế kỉ
    if rdNamSinh >= 2000:
        rdGioiTinh += 2  # Nếu năm sinh thuộc thế kỉ 21 thì mã giới tính cộng thêm 2
    cccd += str(rdGioiTinh)

    # 2 chữ số tiếp theo là mã năm sinh
    strNamSinh = str(rdNamSinh)
    cccd += strNamSinh[2:]

    # 6 chữ số cuối là số ngẫu nhiên
    rd6SoCuoi = soNguoiTrung6SoDauCCCD.get(cccd, 0)  # Ta lấy 6 chữ số cuối bằng số người có cùng 6 chữ số đầu với người hiện tại
    cccd6SoCuoi = str(rd6SoCuoi)
    if len(cccd6SoCuoi) < 6:
        cccd6SoCuoi = '0' * (6 - len(cccd6SoCuoi)) + cccd6SoCuoi  # Nếu chưa đủ 6 chữ số thì ta thêm các số 0 vào trước
    rd6SoCuoi += 1  # Tăng số người có cùng 6 chữ số đầu lên 1
    soNguoiTrung6SoDauCCCD[cccd] = rd6SoCuoi
    cccd += cccd6SoCuoi

    # Random địa chỉ
    rdDChi = QuanHuyenHCM[generator.randint(0, len(QuanHuyenHCM) - 1)] + ', Thành phố Hồ Chí Minh'

    # Thêm dữ liệu học sinh này vào danh sách dữ liệu
    batchHS.append((maHS, rdHo, rdTen, cccd, str(rdNamSinh)+'-'+str(rdThangSinh)+'-'+str(rdNgaySinh), rdDChi))

    # --- Với mỗi học sinh, phát sinh 1-3 dòng dữ liệu cho bảng HOC ---
    rdTruong = generator.randint(0, len(TruongHCM) - 1)
    for i in range(0, 3):
        if rdNamSinh + 16 + i <= 2023:  # Nếu tuổi phù hợp để học THPT
            rdDiem = round(generator.uniform(0.0, 10.0), 2)
            xepLoai = ''
            kQua = 'Hoàn thành'
            if rdDiem >= 9.0:
                xepLoai = 'Xuất sắc'
            elif rdDiem >= 8.0:
                xepLoai = 'Giỏi'
            elif rdDiem >= 7.0:
                xepLoai = 'Khá'
            elif rdDiem >= 5.0:
                xepLoai = 'Trung bình'
            else:
                xepLoai = 'Kém'
                kQua = 'Chưa hoàn thành'
            batchHOC.append((rdTruong+1, maHS, rdNamSinh + 16 + i, rdDiem, xepLoai, kQua))

# Thêm tất cả dữ liệu học sinh vào bảng HS
queryHS = 'INSERT INTO HS (MAHS, HO, TEN, CCCD, NTNS, DCHI_HS) VALUE (%s, %s, %s, %s, %s, %s)'
cursor.executemany(queryHS, batchHS)
connectTruongHoc1.commit() # Cập nhật dữ liệu các học sinh vào database

# Thêm tất cả dữ liệu kết quả học tập vào bảng HOC
queryHOC = 'INSERT INTO HOC (MATR, MAHS, NAMHOC, DIEMTB, XEPLOAI, KQUA) VALUE (%s, %s, %s, %s, %s, %s)'
cursor.executemany(queryHOC, batchHOC);
connectTruongHoc1.commit() # Cập nhật dữ liệu kết quả học tập vào database

# Đóng kết nối
connectTruongHoc1.close()
