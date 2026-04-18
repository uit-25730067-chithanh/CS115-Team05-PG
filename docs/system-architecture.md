# Kiến trúc Hệ thống (System Architecture)

Giải thuật REINFORCE (Monte Carlo Policy Gradient) cho CartPole-v1. (Dự án CS115).

## 1. Môi trường mô phỏng (Environment)

- **Library**: `Gymnasium`.
- **Game**: `CartPole-v1`.
- **State Space**: Vector 4 chiều (Position, Velocity, Pole Angle, Pole Angular Velocity).
- **Action Space**: Rời rạc với 2 hành động (Đẩy xe sang trái `0` / Đẩy sang phải `1`).
- **Reward**: Mỗi khung hình con lắc trụ được sẽ được `+1`. Win là đạt 500.

## 2. Kiến trúc Mạng nơ-ron (PolicyNetwork)

Là một hàm Policy $\pi(a | s, \theta)$ parameterized bởi Neural Network truyền thẳng (MLP).

- **Input Dimension**: `4` (Kích thước State).
- **Hidden Layer**: `128` neurons, hàm kích hoạt `ReLU`.
- **Output Layer**: `2` neurons (Xác suất cho Action `0` và `1`).
- **Activation Output**: Hàm `Softmax` để đảm bảo tổng xác suất của 2 action = 1.0.

## 3. Khối điều khiển thuật toán (REINFORCE)

Thuật toán bao gồm 3 bước lặp chính:

1. **Rollout (Generate Episode)**:
   - Sử dụng `Categorical.sample()` để bốc xác suất tạo ra Action.
   - Sinh ra chuỗi trạng thái, log-xác suất và phần thưởng cho đến khi kết thúc (done / truncated).
2. **Compute Returns (Tính $G_t$)**:
   - $G\_t = R\_{t} + \gamma R\_{t+1} + \dots + \gamma^{T-t} R\_T$
   - Thuật toán lặp lùi từ phần thưởng cuối cùng về 0 để tối ưu tốc độ.
3. **Policy Update (Cập nhật Weights $\theta$)**:
   - Áp dụng trừ Baseline đơn giản: $G\_t = \frac{G\_t - \mu(G)}{\sigma(G) + \epsilon}$ để cắt bớt Variance.
   - Lan truyền ngược (Backpropagation). Loss: $- \ln \pi(A\_t |S\_t) \cdot G\_t$.
