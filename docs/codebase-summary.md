# Tóm tắt Mã nguồn (Codebase Summary)

Tài liệu này liệt kê cấu trúc thư mục và các tệp tin quan trọng nhất trong dự án.

## Cấu trúc Thư mục

```text
CS115-Team05-PG/
├── data/       # Lưu trữ dữ liệu log, checkpoints (được ignore)
├── docs/       # Tài liệu dự án (PDR, standards, architecture)
├── math/       # Các file tĩnh LaTeX (chứng minh công thức toán học)
├── notes/      # Ghi chú cá nhân, nháp cá nhân
├── plans/      # Theo dõi lộ trình Agile/Kanban
├── reports/    # Báo cáo hàng tuần (Word/Markdown)
├── scripts/    # Các kịch bản bash/python dùng để review hoặc kiểm thử UI
├── sources/    # Mã nguồn chính của giải thuật RL
├── test/       # Môi trường chạy thử nghiệm nhanh
└── tmp/        # Rác sinh ra trong quá trình dev (đã được ignore)
```

## Code Logic cốt lõi (sources/)

Thư mục `sources/` chứa toàn bộ thành phần chính của giải thuật REINFORCE.

1. **`sources/train.py`**: Điểm neo thực thi. Khởi tạo `gymnasium`, cấu hình PyTorch, thiết lập Hyperparameters, quản lý vòng lặp Training và vẽ `training_curve.png`.
2. **`sources/reinforce.py`**: Chứa thuật toán Policy Gradient thuần tuý.
   - Hàm `compute_returns()`: Tính toán $G_t$ cho từ phần thưởng.
   - Hàm `update_policy()`: Backpropagation cho Gradient Ascent với việc trừ trung bình để giảm variance (Baseline).
3. **`sources/models/policy.py`**: Chứa định nghĩa kiến trúc mạng nơ-ron `PolicyNetwork`. Trả về Softmax phân bố ngẫu nhiên để Sample hành động. Cung cấp hàm `select_action()`.
4. **`requirements.txt`**: Khai báo dependency chính gồm `gymnasium[classic-control]`, `torch`, `numpy`, `matplotlib`.
