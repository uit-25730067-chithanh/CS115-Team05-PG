# Hướng dẫn Cài đặt & Sử dụng (Installation Guide)

Tài liệu này hướng dẫn cách thiết lập môi trường để chạy mã nguồn REINFORCE cho bài toán CartPole-v1. Việc tuân thủ hướng dẫn này giúp tránh gặp lỗi thiếu thư viện (`ModuleNotFoundError`).

## 1. Yêu cầu hệ thống

- **Python**: Phiên bản 3.9 trở lên.
- **Hệ điều hành**: MacOS, Linux hoặc Windows.

## 2. Thiết lập môi trường

Khuyên dùng môi trường ảo (virtual environment) để tránh xung đột với các dự án khác:

```bash
# Tạo môi trường ảo có tên 'venv'
python3 -m venv venv

# Kích hoạt môi trường (MacOS/Linux)
source venv/bin/activate

# Kích hoạt môi trường (Windows)
.\venv\Scripts\activate
```

## 3. Cài đặt thư viện

Cài đặt các dependency cần thiết từ file `requirements.txt`:

```bash
pip3 install -r requirements.txt
```

_(Lưu ý: File requirements đã bao gồm `gymnasium[classic-control]` và `torch`. Nếu cài thiếu gói classic-control, Gymnasium sẽ không tải được môi trường CartPole)._

## 4. Chạy huấn luyện (Training)

Từ thư mục gốc của dự án (`cs/`), chạy lệnh:

```bash
python3 sources/train.py
```

Code sẽ:

1. Huấn luyện mô hình trong 1000 tập (episodes).
2. Tự động lưu biểu đồ huấn luyện vào file `training_curve.png`.

## 5. Xử lý sự cố (Troubleshooting)

Nếu gặp màn hình treo hoặc crash trên **MacOS dùng chip Apple Silicon (M1/M2/M3)**, hãy tham khảo `docs/troubleshooting.md`. Cụ thể, bạn cần chỉnh sửa `device` trong file `train.py` thành `cpu` thay vì `mps`.
