# 🛠️ Hướng dẫn Cài đặt và Chạy (Installation & Usage)

Tài liệu này hướng dẫn cách thiết lập môi trường và thực thi thuật toán REINFORCE trên môi trường CartPole-v1.

## 1. Yêu cầu hệ thống (Prerequisites)

- Python 3.9 trở lên.
- [venv](https://docs.python.org/3/library/venv.html) (Khuyến nghị - có sẵn trong Python).
- [Conda](https://docs.conda.io/en/latest/) (Tùy chọn - mạnh mẽ cho quản lý thư viện AI).

> **💡 Lựa chọn môi trường nào?**
>
> - **venv**: Là công cụ chuẩn đi kèm Python, cực kỳ nhẹ và đơn giản. Phù hợp nếu bạn chỉ muốn cài đặt nhanh để chạy code.
> - **Conda**: Phù hợp nếu bạn đang học nhiều môn AI khác nhau và muốn quản lý các thư viện hệ thống phức tạp (như CUDA cho GPU) một cách an toàn.

## 2. Cài đặt (Installation)

### Bước 1: Tạo môi trường ảo (Virtual Environment)

```bash
# Dùng venv (Mặc định)
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# HOẶC dùng Conda (Nếu bạn đã cài sẵn Miniconda/Anaconda)
conda create -n cs115-rl python=3.10
conda activate cs115-rl
```

### Bước 2: Cài đặt các thư viện cần thiết

```bash
pip install -r requirements.txt
```

_Lưu ý: Nếu bạn dùng Mac chip M1/M2/M3, PyTorch sẽ tự động hỗ trợ tăng tốc qua MPS._

## 3. Huấn luyện REINFORCE (Training)

### Bước 3: Chạy training

Để bắt đầu quá trình huấn luyện thuật toán REINFORCE trên CartPole-v1:

```bash
# Đảm bảo bạn đang đứng ở thư mục gốc của dự án
python3 scripts/train.py --episodes 500 --seed 42 --hidden-dim 64
```

Lệnh trên là demo nhanh. Để chạy lại cấu hình final đang được track trong repo public:

```bash
python3 scripts/train.py --episodes 1000 --seed 123 --hidden-dim 128
```

### Các tham số CLI quan trọng

- `--lr`: Learning Rate (mặc định `0.001`).
- `--gamma`: Hệ số chiết khấu $\gamma$ (mặc định `0.99`).
- `--episodes`: Số tập huấn luyện (mặc định `1000`).
- `--hidden-dim`: Kích thước hidden layer. Khi evaluate checkpoint, giá trị này phải khớp `run_config.txt`.
- `--seed`: Seed để dễ tái lập kết quả.

## 4. Kết quả sau khi chạy (Outputs)

Sau khi quá trình huấn luyện hoàn tất, các tệp tin sẽ được lưu vào một thư mục riêng biệt theo thời gian trong thư mục `outputs/` (ví dụ: `outputs/run_20260423_163506/`). Các run timestamp này là generated artifacts và được ignore; repo public chỉ giữ bộ kết quả chọn lọc trong `outputs/final/`.

Các tệp tin bao gồm:

1. **`training_curve.png`**: Biểu đồ biểu diễn Reward trung bình qua các Episodes.
2. **`best_policy.pth`**: File lưu trọng số mạng Neural tốt nhất đạt được trong quá trình huấn luyện.
3. **`final_policy.pth`**: File lưu trọng số mạng Neural tại Episode cuối cùng.
4. **`run_config.txt`**: Cấu hình dùng để train checkpoint, đặc biệt là `hidden_dim`.
5. **`metrics.txt`** và **`rewards.txt`**: Metrics tóm tắt và raw reward log.

Bộ kết quả chọn lọc của repo public nằm tại `outputs/final/`. Có thể đánh giá checkpoint đã chọn bằng:

```bash
python3 scripts/evaluate.py \
  --checkpoint outputs/final/reinforce-cartpole-v1/best_policy.pth \
  --episodes 10 \
  --hidden-dim 128
```

## 5. Xử lý sự cố (Troubleshooting)

- **Lỗi treo hoặc crash trên MacOS dùng chip Apple Silicon (M1/M2/M3)**: Hãy tham khảo [docs/troubleshooting.md](./troubleshooting.md). Cụ thể, bạn cần chỉnh sửa `device` trong file `train.py` thành `cpu` thay vì `mps`.
- **Lỗi `ModuleNotFoundError: No module named 'models'`**: Ưu tiên chạy qua `scripts/train.py` hoặc `scripts/evaluate.py` từ thư mục gốc dự án. Các entrypoint này tự thiết lập import path.
- **Lỗi render Gymnasium**: Nếu muốn xem Agent chơi (render), bạn cần cài thêm `swig` và `box2d-py`, nhưng trong script `train.py` hiện tại chúng ta chạy ở chế độ `non-render` để tối ưu tốc độ trên Server/Terminal.
