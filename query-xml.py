# Cài đặt lxml
import subprocess
import sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'lxml'])

# Thêm thư viện cần thiết
import glob
from lxml import etree

# Đường dẫn đến file XML đầu tiên trong folder XML (do câu 4 xuất ra)
xmlFile = glob.glob(f"XML/*.xml")[0]

# Đọc file XML
print("Truy vấn trong file", xmlFile)
xmlTree = etree.parse(xmlFile)

# Nhập ngưỡng điểm [thấp, cao]
diemThap = input("Nhập ngưỡng điểm thấp: ")
diemCao = input("Nhập ngưỡng điểm cao: ")

# Dùng xpath để lấy những HocSinh có DiemTB trong ngưỡng điểm [thấp, cao]
danhSach = xmlTree.xpath(f"//HocSinh[number(DiemTB) >= {diemThap} and number(DiemTB) <= {diemCao}]")

print(f"Danh sách học sinh có điểm trung bình trong ngưỡng điểm [{diemThap}, {diemCao}] gồm {len(danhSach)} học sinh:")
for hocsinh in danhSach:
    # Vì trong file XML do câu 4 xuất ra:
    # MaHS là attribute của HocSinh nên để lấy MaHS ta dùng hocsinh.get('MaHS')
    # HoTen là subchild thứ 0 của HocSinh nên HoTen = hocsinh[0]. Ta cần nội dung của HoTen nên lấy hocsinh[0].text
    # DiemTB là subchild thứ 2 của HocSinh nên DiemTB = hocsinh[2]. Ta cần nội dung của HoTen nên lấy hocsinh[2].text
    print(f"Mã HS: {hocsinh.get('MaHS')}, Họ tên: {hocsinh[0].text}, Điểm TB: {hocsinh[2].text}")

