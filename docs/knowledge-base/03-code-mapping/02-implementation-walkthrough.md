# Ánh xạ 1:1 giữa Toán học và Mã nguồn

Để giúp team dễ dàng đối chiếu, bảng dưới đây ánh xạ các thành phần trong công thức toán học của thuật toán REINFORCE vào các biến số và hàm số thực tế trong mã nguồn dự án.

## 1. Bảng đối chiếu Ký hiệu (Symbol Mapping)

| Ký hiệu Toán học | Ý nghĩa | Tên biến trong Code | Vị trí (File) |
| :--- | :--- | :--- | :--- |
| $s$ | Trạng thái (State) | `state` | `train.py`, `reinforce.py` |
| $a$ | Hành động (Action) | `action` | `train.py`, `reinforce.py` |
| $\pi_\theta(a\|s)$ | Chính sách (Policy) | `probs` hoặc `action_probs` | `reinforce.py` (Hàm `forward`) |
| $\ln \pi_\theta(a\|s)$ | Log-policy | `log_prob` | `reinforce.py` (Hàm `select_action`) |
| $r_t$ | Phần thưởng tức thời | `reward` | `train.py` (Vòng lặp episode) |
| $G_t$ | Tổng phần thưởng tích lũy | `returns` hoặc `G` | `reinforce.py` (Hàm `update_policy`) |
| $\gamma$ | Hệ số chiết khấu | `gamma` | `PolicyGradient` class constructor |
| $\alpha$ | Learning rate | `lr` | `PolicyGradient` class constructor |
| $\nabla_\theta J(\theta)$ | Gradient hàm mục tiêu | `policy_loss.backward()` | `reinforce.py` (Hàm `update_policy`) |

## 2. Sơ đồ Luồng Công việc (REINFORCE Workflow)

Dưới đây là chu trình từ khi Agent quan sát môi trường cho đến khi cập nhật tham số:

![REINFORCE Workflow Chalkboard](../assets/reinforce-workflow.png)

## 3. Luồng dữ liệu (Data Flow)

### Bước 1: Thu thập Trajectory (Sampling)
Trong `train.py`, vòng lặp `while not done` thực hiện việc lấy mẫu:
```python
action, log_prob = agent.select_action(state)
state, reward, done, _, _ = env.step(action)
agent.rewards.append(reward)
agent.log_probs.append(log_prob)
```
*   Tương ứng với việc lấy mẫu $\tau \sim \pi_\theta$.

### Bước 2: Tính toán Return ($G_t$)
Trong `reinforce.py`, hàm `update_policy` tính ngược từ cuối episode:
```python
for r in self.rewards[::-1]:
    G = r + self.gamma * G
    returns.insert(0, G)
```
*   Tương ứng với công thức $G_t = \sum_{k=t}^T \gamma^{k-t} r_{k+1}$.

### Bước 3: Chuẩn hóa Baseline (Variance Reduction)
```python
returns = torch.tensor(returns)
returns = (returns - returns.mean()) / (returns.std() + 1e-9)
```
*   Tương ứng với việc áp dụng Baseline $b = \text{mean}(G)$ và chuẩn hóa phương sai.

### Bước 4: Tính Loss và Backward
```python
for log_prob, disc_return in zip(self.log_probs, returns):
    policy_loss.append(-log_prob * disc_return)
```
*   Tương ứng với việc lập biểu thức $\nabla \ln \pi \cdot G$.

## 3. Tại sao cấu trúc code lại như vậy?

1.  **Lưu trữ `log_probs`:** Chúng ta phải lưu lại `log_prob` tại mỗi bước vì đó là một phần của đồ thị tính toán (computational graph). Nếu không lưu, PyTorch sẽ không biết cách tính đạo hàm ngược lại các trọng số mạng neural đã sinh ra xác suất đó.
2.  **Tính `returns` ngược:** Tính ngược từ dưới lên (từ $T$ về $0$) hiệu quả hơn về mặt tính toán ($O(T)$ thay vì $O(T^2)$).
3.  **Xóa bộ nhớ:** Sau mỗi lần `update_policy`, chúng ta phải xóa `self.rewards` và `self.log_probs` để chuẩn bị cho episode tiếp theo. Điều này tương ứng với việc chúng ta đang thực hiện On-policy learning (học dựa trên dữ liệu mới nhất).
