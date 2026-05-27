# CS115 Team 05 - Chuẩn hóa ký hiệu toán

File này tóm tắt các ký hiệu/công thức chưa đồng nhất giữa báo cáo và slide, kèm dạng nên sửa để dùng thống nhất trong phần Policy Gradient.

## Bảng ký hiệu chuẩn

| Khái niệm | Ký hiệu thống nhất | Ghi chú |
|---|---|---|
| Policy parameters | $\theta$ | Dành riêng cho tham số của policy network. |
| Policy | $\pi_\theta(a_t \mid s_t)$ | Xác suất chọn action $a_t$ tại state $s_t$. |
| State | $s_t$ | Trạng thái tại thời điểm $t$. |
| Action | $a_t$ | Hành động tại thời điểm $t$. |
| Immediate reward | $r_{t+1}$ | Reward nhận sau khi thực hiện $a_t$. |
| Reward function | $R(s_t,a_t)$ | Hàm reward trong MDP. |
| Trajectory | $\tau$ | Một episode hoặc chuỗi tương tác. |
| Trajectory return | $R(\tau)$ | Tổng reward của cả trajectory. |
| Reward-to-go | $G_t$ | Tổng reward tương lai từ thời điểm $t$. |
| CartPole pole angle | $\phi$ | Không dùng $\theta$ để tránh trùng với policy parameters. |

## 1. CartPole state vector

**Chưa đồng nhất:** Dùng $\theta$ cho góc CartPole trong state vector, trong khi $\theta$ cũng là policy parameters.

**Nên sửa thành:**

$$
s_t = [x, \dot{x}, \phi, \dot{\phi}]
$$

**Ghi chú:** Giữ $\theta$ chỉ cho tham số của policy network để tránh một ký hiệu mang hai nghĩa.

## 2. Policy notation

**Chưa đồng nhất:** Lẫn cách viết `πθ`, `pi_theta`, `π_θ`, hoặc thiếu biến thời gian $a_t, s_t$.

**Nên sửa thành:**

$$
\pi_\theta(a_t \mid s_t)
$$

Nếu cần viết rõ là xác suất có điều kiện:

$$
\pi_\theta(a_t \mid s_t) = P(a_t \mid s_t; \theta)
$$

**Ghi chú:** Trong script thuyết trình có thể đọc là "pi theta", nhưng trong báo cáo/slide công thức nên dùng subscript.

## 3. Objective function

**Chưa đồng nhất:** Objective đôi khi viết thiếu phân phối lấy kỳ vọng, ví dụ chỉ viết $J(\theta)=E[R]$.

**Nên sửa thành:**

$$
J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta}[R(\tau)]
$$

Dạng khai triển rời rạc:

$$
J(\theta) = \sum_{\tau}P(\tau \mid \theta)R(\tau)
$$

**Ghi chú:** Phần này nói expected return trên các trajectory sinh bởi policy hiện tại, nên phải có $\tau \sim \pi_\theta$.

## 4. Trajectory probability

**Chưa đồng nhất:** Trajectory probability dễ bị viết gọn thành $P(\tau)$ hoặc chỉ còn tích các policy, thiếu dynamics môi trường.

**Nên sửa thành:**

$$
P(\tau \mid \theta)
= \rho_0(s_0)\prod_{t=0}^{T}\pi_\theta(a_t \mid s_t)P(s_{t+1}\mid s_t,a_t)
$$

**Ghi chú:** Khi lấy đạo hàm theo $\theta$, chỉ policy phụ thuộc $\theta$; dynamics của CartPole không phụ thuộc policy parameters.

## 5. Log-derivative trick

**Chưa đồng nhất:** Lẫn `ln` và `log` trong cùng phần proof.

**Nên sửa thành:**

$$
\nabla_\theta f(\theta) = f(\theta)\nabla_\theta \log f(\theta)
$$

Áp dụng cho trajectory probability:

$$
\nabla_\theta P(\tau \mid \theta)
= P(\tau \mid \theta)\nabla_\theta \log P(\tau \mid \theta)
$$

**Ghi chú:** Trong ML/RL, $\log$ thường hiểu là natural logarithm; dùng một ký hiệu giúp proof sạch hơn.

## 6. Policy Gradient Theorem

**Chưa đồng nhất:** Dùng lẫn $R(\tau)$ và $G_t$ nhưng chưa nói rõ khác nhau.

**Nên sửa thành:**

Dạng theorem theo trajectory return:

$$
\nabla_\theta J(\theta)
= \mathbb{E}_{\tau \sim \pi_\theta}
\left[
R(\tau)\sum_{t=0}^{T}\nabla_\theta \log \pi_\theta(a_t \mid s_t)
\right]
$$

Dạng REINFORCE dùng reward-to-go:

$$
\nabla_\theta J(\theta)
= \mathbb{E}_{\tau \sim \pi_\theta}
\left[
\sum_{t=0}^{T}\nabla_\theta \log \pi_\theta(a_t \mid s_t)G_t
\right]
$$

**Ghi chú:** $R(\tau)$ là return toàn trajectory; $G_t$ là reward-to-go từ thời điểm $t$.

## 7. Reward-to-go

**Chưa đồng nhất:** Công thức bị dẹt kiểu `Gt = ΣTk=t γk-t rk+1`, mất chỉ số trên/dưới.

**Nên sửa thành:**

$$
G_t = \sum_{k=t}^{T}\gamma^{k-t}r_{k+1}
$$

**Ghi chú:** Nên dùng $r_{k+1}$ nhất quán với quy ước reward nhận sau transition từ time $k$.

## 8. Gradient ascent update

**Chưa đồng nhất:** Update rule dễ bị nhầm với gradient descent nếu không ghi rõ dấu cộng/ascent.

**Nên sửa thành:**

$$
\theta \leftarrow \theta + \alpha \nabla_\theta J(\theta)
$$

Dạng sample update của REINFORCE:

$$
\theta \leftarrow \theta
+ \alpha \sum_{t=0}^{T}G_t\nabla_\theta \log \pi_\theta(a_t \mid s_t)
$$

**Ghi chú:** Policy Gradient đang tối đa hóa expected return, còn trong PyTorch thì dùng loss âm để optimizer minimize.

## 9. PyTorch loss

**Chưa đồng nhất:** Loss âm trong code có thể bị hiểu là đang minimize sai mục tiêu nếu không giải thích.

**Nên sửa thành:**

$$
L(\theta)
= -\sum_{t=0}^{T}\log \pi_\theta(a_t \mid s_t)G_t
$$

Giải thích ngắn:

$$
\min L(\theta) \equiv \max J(\theta)
$$

**Ghi chú:** Đây là cầu nối giữa công thức gradient ascent và cơ chế gradient descent của optimizer.

## 10. Baseline subtraction

**Chưa đồng nhất:** Baseline proof dễ thiếu phân phối trên action hoặc dùng $b(s)$ lẫn với $b(s_t)$.

**Nên sửa thành:**

Gradient có baseline:

$$
\nabla_\theta J(\theta)
= \mathbb{E}_{\tau \sim \pi_\theta}
\left[
\sum_{t=0}^{T}
\nabla_\theta \log \pi_\theta(a_t \mid s_t)(G_t - b(s_t))
\right]
$$

Baseline không gây bias:

$$
\mathbb{E}_{a_t \sim \pi_\theta(\cdot \mid s_t)}
[
\nabla_\theta \log \pi_\theta(a_t \mid s_t)b(s_t)
] = 0
$$

Khai triển chứng minh:

$$
\sum_{a_t}
\pi_\theta(a_t \mid s_t)
\frac{
\nabla_\theta \pi_\theta(a_t \mid s_t)
}{
\pi_\theta(a_t \mid s_t)
}
b(s_t)
$$

Rút gọn:

$$
b(s_t)\sum_{a_t}\nabla_\theta \pi_\theta(a_t \mid s_t)
= b(s_t)\nabla_\theta \sum_{a_t}\pi_\theta(a_t \mid s_t)
= b(s_t)\nabla_\theta 1
= 0
$$

**Ghi chú:** Baseline chỉ giảm variance; nó không làm lệch gradient vì kỳ vọng của score function bằng 0.

## Thứ tự sửa khuyến nghị

1. Đổi CartPole pole angle từ $\theta$ sang $\phi$.
2. Chuẩn hóa mọi policy thành $\pi_\theta(a_t \mid s_t)$.
3. Sửa reward-to-go thành $G_t = \sum_{k=t}^{T}\gamma^{k-t}r_{k+1}$.
4. Tách rõ $R(s_t,a_t)$, $r_{t+1}$, $R(\tau)$, và $G_t$.
5. Trong proof, dùng $\log$ nhất quán, không lẫn `ln`.
6. Sửa baseline proof theo đúng dạng expectation trên action.
