# Tóm tắt Mã nguồn (Codebase Summary)

Tài liệu này liệt kê cấu trúc thư mục và các tệp tin quan trọng nhất trong dự án CS115-Team05 (REINFORCE Parallelization).

## Cấu trúc Thư mục

```text
CS115-Team05-PG/
├── data/       # Lưu trữ dữ liệu log, checkpoints (được ignore)
├── docs/       # Tài liệu dự án (PDR, standards, architecture, knowledge)
├── math/       # Các file tĩnh LaTeX (chứng minh công thức toán học)
├── outputs/    # Kết quả training (model checkpoints, training curve) theo timestamp
├── notes/      # Ghi chú cá nhân & Nhật ký tiến độ/Journal (được ignore)
├── plans/      # Theo dõi lộ trình Agile/Kanban (được ignore)
├── reports/    # Báo cáo hàng tuần (Word/Markdown)
├── scripts/    # Các kịch bản bash/python dùng để review hoặc kiểm thử UI
├── sources/    # Mã nguồn chính của giải thuật RL
├── test/       # Môi trường chạy thử nghiệm nhanh
└── tmp/        # Rác sinh ra trong quá trình dev (được ignore)
```

## Code Logic cốt lõi (sources/)

Thư mục `sources/` chứa toàn bộ thành phần chính của giải thuật REINFORCE.

1. **`sources/train.py`**: Điểm neo thực thi. Khởi tạo `gymnasium`, cấu hình PyTorch, thiết lập Hyperparameters, quản lý vòng lặp Training và vẽ `training_curve.png`.
2. **`sources/reinforce.py`**: Chứa thuật toán Policy Gradient thuần tuý.
   - $G_{t} = R_{t} + \gamma R_{t+1} + \dots + \gamma^{T-t} R_{T}$
   - Thuật toán lặp lùi từ phần thưởng cuối cùng về 0 để tối ưu tốc độ.
3. **Policy Update (Cập nhật Weights $\theta$)**:
   - Áp dụng trừ Baseline đơn giản: $G_{t} = \frac{G_{t} - \mu(G)}{\sigma(G) + \epsilon}$ để cắt bớt Variance.
   - Lan truyền ngược (Backpropagation). Loss: $- \ln \pi(A_{t} | S_{t}) \cdot G_{t}$.
4. **`sources/models/policy.py`**: Chứa định nghĩa kiến trúc mạng nơ-ron `PolicyNetwork`. Trả về Softmax phân bố ngẫu nhiên để Sample hành động. Cung cấp hàm `select_action()`.
5. **`sources/test_env.py`**: Kiểm tra môi trường CartPole-v1 và chạy random baseline 100 episodes.
6. **`outputs/run_YYYYMMDD_HHMMSS/`**: Thư mục sinh ra sau khi chạy `train.py`, chứa `best_policy.pth`, `final_policy.pth` và `training_curve.png`.
7. **`outputs/baseline_YYYYMMDD_HHMMSS/`**: Thư mục sinh ra sau khi chạy baseline trong `test_env.py`, chứa `baseline_curve.png`, `baseline_stats.txt` và `baseline_log.txt`.
8. **`requirements.txt`**: Khai báo dependency chính gồm `gymnasium[classic-control]`, `torch`, `numpy`, `matplotlib`.
