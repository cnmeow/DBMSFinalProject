# Thông tin của MySQL
HOST = 'localhost' # Host của MySQL
USER = 'root' # Người dùng
PASSWORD = 'camnguyen' # Mật khẩu

# Cài đặt pymysql
import subprocess
import sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pymysql'])

# Thêm các thư viện cần thiết
import pymysql
import xml.etree.ElementTree as XML
import time

def query(databaseName, schoolName, academicYear, academicRank):
    # Kết nối đến database
    connectDatabase = pymysql.connect(host=HOST, user=USER, password=PASSWORD, database=databaseName)

    # Tạo một đối tượng cursor
    cursor = connectDatabase.cursor()

    # Thực hiện truy vấn dữ liệu
    query = f"""
        SELECT HS.MAHS, HS.HO, HS.TEN, HS.NTNS, HOC.DIEMTB, HOC.XEPLOAI, HOC.KQUA
        FROM HS
        JOIN HOC ON HS.MAHS = HOC.MAHS
        JOIN TRUONG ON HOC.MATR = TRUONG.MATR
        WHERE TRUONG.TENTR = '{schoolName}' AND HOC.NAMHOC = {academicYear} AND HOC.XEPLOAI = '{academicRank}'
    """
    startTime = time.time()  # Thời gian bắt đầu truy vấn
    cursor.execute(query) # Thực hiện truy vấn
    endTime = time.time()  # Thời gian hoàn thành truy vấn
    students = cursor.fetchall()

    # In ra danh sách học sinh với truy vấn trên
    print("Danh sách gồm {họ tên học sinh, NTNS, Điểm TB, xếp loại, kết quả}:")
    for student in students:
        print(student[1], student[2], ',', student[3], ',', student[4], ',', student[5], ',', student[6])

    # In ra thời gian truy vấn
    print("------")
    print("Thời gian truy vấn của", databaseName ,", năm học,", academicYear, ", xếp loại", academicRank, "là:", endTime - startTime, "giây")

    # Tạo file XML
    dsHocSinh = XML.Element("DanhSachHocSinh")
    for student in students:
        hocsinh = XML.SubElement(dsHocSinh, "HocSinh")
        hocsinh.set("MaHS", str(student[0])) # Thêm thuộc tính MaHS (Mã học sinh) để phân biệt các học sinh trùng thông tin

        hoTen = XML.SubElement(hocsinh, "HoTen")
        hoTen.text = student[1] + " " + student[2] # Tên học sinh
        hoTen.set("datatype", "string") # Gán kiểu dữ liệu của tên học sinh là string

        NTNS = XML.SubElement(hocsinh, "NTNS")
        NTNS.text = str(student[3])  # Ngày tháng năm sinh
        NTNS.set("datatype", "date") # Gán kiểu dữ liệu của ngày tháng năm sinh là date

        diemTB = XML.SubElement(hocsinh, "DiemTB")
        diemTB.text = str(student[4]) # Điểm trung bình
        diemTB.set("datatype", "float")  # Gán kiểu dữ liệu của điểm trung bình là float

        xepLoai = XML.SubElement(hocsinh, "XepLoai")
        xepLoai.text = student[5] # Xếp loại
        xepLoai.set("datatype", "string")  # Gán kiểu dữ liệu của xếp loại là string

        ketQua = XML.SubElement(hocsinh, "KetQua")
        ketQua.text = student[6] # Kết quả
        ketQua.set("datatype", "string")  # Gán kiểu dữ liệu của kết quả là string

    xmlTree = XML.ElementTree(dsHocSinh)
    XML.indent(xmlTree, space="\t", level=0)
    xmlPath = f"XML/{databaseName}-{schoolName}-{academicYear}-{academicRank}.xml"
    xmlTree.write(xmlPath, encoding='UTF-8', xml_declaration=True)

    # Đóng kết nối
    cursor.close()
    connectDatabase.close()

# Nhận đầu vào
DATABASE = input("Nhập tên database: ")
TRUONG = input("Nhập tên trường: ")
NAMHOC = input("Nhập năm học: ")
XEPLOAI = input("Nhập xếp loại học tập: ")

# Thực hiện truy vấn dữ liệu với đầu vào đã nhập
query(DATABASE, TRUONG, NAMHOC, XEPLOAI)


