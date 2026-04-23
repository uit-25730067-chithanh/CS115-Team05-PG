# Cơ chế Autograd và Hàm Loss trong REINFORCE

Trong toán học, chúng ta thực hiện **Gradient Ascent** để tối đa hóa hàm mục tiêu $J(\theta)$. Tuy nhiên, các thư viện Deep Learning như PyTorch được thiết kế tối ưu cho **Gradient Descent** (giảm thiểu Loss). Tài liệu này giải thích cách chúng ta "lừa" PyTorch để thực hiện tối ưu hóa RL.

## 1. Tại sao lại có dấu âm (-) trong hàm Loss?

Trong bài toán phân loại (Supervised Learning), chúng ta cực tiểu hóa Negative Log Likelihood (NLL):
$$\text{Loss} = -\ln P(\text{label} | \text{input})$$

Trong RL (REINFORCE), chúng ta muốn cực đại hóa:
$$\nabla_\theta J(\theta) \approx \nabla_\theta \ln \pi_\theta(a|s) G_t$$

Để sử dụng trình tối ưu hóa (Optimizer) của PyTorch, chúng ta định nghĩa một hàm Loss giả lập sao cho đạo hàm của nó ngược hướng với hướng chúng ta muốn đi:
$$\text{Loss}_{RL} = - \ln \pi_\theta(a|s) G_t$$

Khi PyTorch tính `loss.backward()`, nó sẽ tính $\nabla_\theta \text{Loss}_{RL} = - \nabla_\theta \ln \pi_\theta(a|s) G_t$. Sau đó, Optimizer thực hiện bước cập nhật:
$$\theta \leftarrow \theta - \alpha \nabla_\theta \text{Loss}_{RL} \implies \theta \leftarrow \theta + \alpha (\nabla_\theta \ln \pi_\theta(a|s) G_t)$$

**Kết quả:** Việc cực tiểu hóa $-\ln \pi \cdot G$ tương đương với việc cực đại hóa $\ln \pi \cdot G$.

## 2. Phân tích dòng code then chốt

Trong file `sources/reinforce.py`, hàm `update_policy` chứa logic:

```python
# Trong sources/reinforce.py
def update_policy(optimizer, log_probs, returns, device="cpu"):
    returns = torch.tensor(returns, dtype=torch.float32).to(device)
    
    # Bước quan trọng: Chuẩn hóa returns để giảm phương sai
    if len(returns) > 1:
        returns = (returns - returns.mean()) / (returns.std() + 1e-8)
        
    policy_loss = []
    for log_prob, G_t in zip(log_probs, returns):
        policy_loss.append(-log_prob * G_t)
        
    # Tính tổng loss và thực hiện backprop
    policy_loss = torch.stack(policy_loss).sum()
    optimizer.zero_grad()
    policy_loss.backward()
    optimizer.step()
```

- `log_prob`: Chính là $\ln \pi_\theta(a_t|s_t)$ thu được từ `m.log_prob(action)`.
- `G_t`: Chính là $G_t$ đã được tính toán và chuẩn hóa.
- `-log_prob * G_t`: Chính là thành phần của hàm Loss cho mỗi bước thời gian.

## 3. Tại sao không dùng Mean Squared Error (MSE)?

Nhiều người mới học RL thường thắc mắc tại sao không dùng `MSE(action, true_action)`.

- **Trả lời:** Trong RL, chúng ta không biết "true action" (hành động đúng). Chúng ta chỉ biết hành động đó mang lại bao nhiêu phần thưởng. Do đó, chúng ta phải sử dụng Policy Gradient để "đẩy" xác suất của các hành động dựa trên kết quả của chúng, thay vì ép nó theo một nhãn cố định.

## 4. Vai trò của `backward()`

Khi gọi `policy_loss.backward()`, PyTorch thực hiện:

1.  Áp dụng quy tắc Chain Rule trên toàn bộ đồ thị tính toán của mạng neural.
2.  Tính toán vector Gradient của $\theta$ đối với từng tham số trong các lớp Linear.
3.  Lưu trữ Gradient vào thuộc tính `.grad` của các Tensor trọng số.

Optimizer sau đó chỉ việc lấy các giá trị `.grad` này để cập nhật trọng số.
