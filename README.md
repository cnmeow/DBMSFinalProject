# Đồ án cuối kì cho môn Cơ sở dữ liệu

Repo này chứa mã nguồn cho đồ án cuối kì môn Cơ sở dữ liệu. 

## Yêu cầu của đồ án

Mỗi trường học có một mã số duy nhất để nhận biết, có tên trường và địa chỉ. 

Mỗi học sinh có một mã số duy nhất để nhận biết, họ tên, số Căn cước công dân (CCCD) nếu đến tuổi cấp CCCD, được sinh vào một ngày và cư trú tại một địa chỉ. Số CCCD luôn duy nhất nếu có. 

Mỗi học sinh tham gia học tại 1 Trường vào một năm học, sẽ có một trị số Điểm trung bình chung (tính trên thang 10). Tùy thuộc vào Điểm trung bình chung mà học sinh sẽ được xếp loại học tập là “Xuất sắc”, “Giỏi”, “Khá”, “Trung bình” hoặc “Yếu”; và có một kết quả  là “Hoàn thành” hoặc “Chưa hoàn thành”. 

Các yêu cầu:

1.	Hãy viết script `CreateSchema1.sql` tạo cơ sở dữ liệu có tên là TRUONGHOC1, chứa 3 table như mô tả trên; có các khóa chính, khóa ngoại phù hợp. Với mỗi bảng hãy tạo clustered index theo khóa chính.
2.	Hãy viết chương trình `generate-db` bằng ngôn ngữ C++, Python hoặc Java; tự động phát sinh ra dữ liệu cho các bảng trên: Bảng TRUONG có ít nhất 100 dòng; Bảng HS có ít nhất 1 triệu dòng; Mỗi học sinh trong HS có tương ứng từ 1 đến 3 dòng trong bảng HOC.
3.	Hãy viết script `CreateSchema2.sql` tạo cơ sở dữ liệu có tên là TRUONGHOC2 giống như TRUONGHOC1, cả về cấu trúc lẫn dữ liệu; Ngoài ra, script còn tạo thêm trong TRUONGHOC2 các index riêng rẽ trên các thuộc tính Tên trường, Xếp loại, Năm học
4.	Hãy viết chương trình `query-db` nhận đầu vào là {tên database, tên trường; năm học; xếp loại học tập} và in ra màn hình danh sách gồm {họ tên học sinh, NTNS, Điểm TB, xếp loại, kết quả}. Đo lường và in ra thời gian truy vấn dữ liệu. (Hãy tự nhận xét thời gian thực hiện truy vấn khi làm việc trên 2 database khác nhau). Mỗi lần chạy chương trình, cũng xuất dữ liệu ra file XML. (tự động đặt tên file xml theo quy ước `têndatabase-têntrường-nămhọc-xếploại.xml`)
  
5.	Hãy viết chương trình `query-xml` đọc một file XML theo yêu cầu 4, nhận vào ngưỡng điểm [thấp, cao] và in ra màn hình danh sách học sinh có điểm trung bình nằm trong ngưỡng điểm. Lưu ý sử dụng Xpath."

## Triển khai

Đồ án được triển khai bằng:
* **Cơ sở dữ liệu:** MySQL
* **Ngôn ngữ lập trình:** Python

## Cấu trúc Repo

Repo chứa các tập tin sau:

* [CreateSchema1.sql](/CreateSchema1.sql) (yêu cầu 1): Script tạo cơ sở dữ liệu TRUONGHOC1 
* [generate-db.py](/generate-db.py) (yêu cầu 2): Chương trình bằng Python tạo dữ liệu cho các bảng của TRUONGHOC1 
* [CreateSchema2.sql](/CreateSchema2.sql) (yêu cầu 3): Script tạo cơ sở dữ liệu TRUONGHOC2 
* [query-db.py](/query-db.py) (yêu cầu 4): Chương trình bằng Python truy vấn cơ sở dữ liệu bằng {tên database, tên trường, năm học, xếp loại học tập} 
* [query-xml.py](/query-xml.py) (yêu cầu 5): Code Python đọc tệp XML theo yêu cầu 4, dùng Xpath in ra danh sách học sinh có điểm trung bình trong ngưỡng cần truy vấn
* Folder [XML](/XML): Chứa các file XML do yêu cầu 4 xuất ra

## Cách sử dụng Repo

Tải Repo về, ví dụ địa chỉ của Repo sau khi tải là `/Users/cnmeow/DBMSFinalProject`

1. Mở terminal và nhập lệnh sau để tạo database TRUONGHOC1
```
mysql -uroot -p </User/cnmeow/DBMSFinalProject/CreateSchema1.sql
```

Kiểm tra cấu trúc của TRUONGHOC1 bằng cách đăng nhập mysql và dùng các lệnh:
* Dùng database TRUONGHOC1:
```
use TRUONGHOC1;
```
* Xem danh sách các bảng của TRUONGHOC1:
```
show tables;
```
* Xem các cột trong bảng (ví dụ với bảng HOC):
```
show columns from HOC;
```
* Xem các ràng buộc trong bảng (ví dụ với bảng HOC):
```
show constraints from HOC;
```
* Xem các chỉ mục trong bảng (ví dụ với bảng HOC):
```
show index from HOC;
```

2. Chạy file `generate-db.py`. Sau đó kiểm tra dữ liệu trong các bảng của TRUONGHOC1 bằng lệnh (ví dụ với bảng HOC):
```
select * from HOC;
```

3. Thoát mysql bằng lệnh
```
exit
```
sau đó chạy script `CreateSchema2.sql` tương tự như bước 1. 

4. Mở file `query-db.py`, chỉnh sửa thông tin mysql ở các dòng 2-4. Lưu lại và chạy chương trình. Sau đó nhập các thông tin cần truy vấn, ví dụ:
- Tên database: "TRUONGHOC1"
- Tên trường: "THPT Đa Phước"
- Năm học: 2022
- Xếp loại học tập: "Giỏi"

Để so sánh thời gian truy vấn giữa database TRUONGHOC1 và TRUONGHOC2, truy vấn nhiều lần với {tên trường, năm học, xếp loại} của các lần khác nhau. Ghi nhận thời gian và so sánh, đưa ra kết luận.

5. Mặc định chương trình `query-xml.py` sẽ truy vấn file đầu tiên trong folder XML. Để truy vấn trong file XML cụ thể, mở file `query-xml.py` và chỉnh sửa đường dẫn đến file đó ở dòng 11. Lưu lại và chạy chương trình. Sau đó nhập ngưỡng điểm cần truy vấn, ví dụ:
- Ngưỡng điểm thấp: 2.1
- Ngưỡng điểm cao: 6.4

## Kết quả

Kết quả sau khi thực hiện các yêu cầu của đồ án:

1. `CreateSchema1.sql` tạo cơ sở dữ liệu TRUONGHOC1 phù hợp theo mô tả, có clustered index theo khóa chính.
   
2. Chương trình `generate-db.py` phát sinh đủ dữ liệu cho TRUONGHOC1.
  
3. `CreateSchema2.sql` tạo cơ sở dữ liệu TRUONGHOC2 giống TRUONGHOC1 về cấu trúc lẫn dữ liệu, có các index riêng rẽ trên thuộc tính Tên trường, Xếp loại, Năm học.
 
4. Chương trình `query-db.py` trả về chính xác danh sách học sinh khi truy vấn bằng {tên database, tên trường, năm học, xếp loại học tập}, có tạo file XML trong folder XML với tên theo yêu cầu. Kết quả chạy cho thấy thời gian thực thi truy vấn trên TRUONGHOC2 có thêm các chỉ mục, nhanh hơn TRUONGHOC1 đáng kể.

5. Chương trình `query-xml.py` có dùng Xpath để in ra chính xác danh sách học sinh có điểm trung bình trong ngưỡng cần truy vấn.

