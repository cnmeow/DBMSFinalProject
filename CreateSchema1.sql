-- Xoá cơ sở dữ liệu TRUONGHOC1 nếu tồn tại trước đó
DROP DATABASE IF EXISTS TRUONGHOC1;

-- Tạo cơ sở dữ liệu
CREATE DATABASE TRUONGHOC1;
USE TRUONGHOC1;

-- Tạo bảng TRUONG để lưu thông tin các trường
CREATE TABLE TRUONG (
    MATR INT PRIMARY KEY, -- Mã trường là khoá chính
    TENTR NVARCHAR(100) NOT NULL, -- Tên trường
    DCHITR NVARCHAR(100) NOT NULL -- Địa chỉ trường
);

-- Tạo bảng HS để lưu thông tin các học sinh
CREATE TABLE HS (
    MAHS INT PRIMARY KEY, -- Mã học sinh là khoá chính
    HO NVARCHAR(50) NOT NULL, -- Họ của học sinh
    TEN NVARCHAR(50) NOT NULL, -- Tên của học sinh
    CCCD NVARCHAR(12) UNIQUE, -- CCCD của học sinh, nếu có thì phải là duy nhất
    NTNS DATE NOT NULL, -- Ngày tháng năm sinh của học sinh
    DCHI_HS NVARCHAR(100) NOT NULL -- Địa chỉ của học sinh
);

-- Tạo bảng HOC để lưu kết quả học tập của các học sinh
CREATE TABLE HOC (
    MATR INT, -- Mã trường
    MAHS INT, -- Mã học sinh
    NAMHOC INT NOT NULL, -- Năm học
    DIEMTB FLOAT(4, 2) NOT NULL, -- Điểm trung bình
    XEPLOAI NVARCHAR(20) NOT NULL, -- Xếp loại (Hoàn thành/Không hoàn thành)
    KQUA NVARCHAR(20) NOT NULL, -- Kết quả (Xuất sắc/Giỏi/Khá/Trung bình/Yếu)
    PRIMARY KEY (MATR, MAHS, NAMHOC), -- Khoá chính là (Mã trường, Mã học sinh, Năm học)
    FOREIGN KEY (MATR) REFERENCES TRUONG(MATR), -- Mã trường là khoá ngoại
    FOREIGN KEY (MAHS) REFERENCES HS(MAHS) -- Mã học sinh là khoá ngoại
);


-- Tạo index cho các bảng
CREATE INDEX IDX_TRUONG ON TRUONG (MATR);
CREATE INDEX IDX_HS ON HS (MAHS);
CREATE INDEX IDX_HOC ON HOC (MATR, MAHS, NAMHOC);
