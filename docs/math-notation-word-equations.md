# CS115 Team 05 - Chuẩn hóa ký hiệu toán

File này tóm tắt các ký hiệu/công thức chuẩn dùng thống nhất trong báo cáo, slide, **và code**. Bảng dưới có cột đối chiếu trực tiếp với biến/hàm trong source để team kiểm tra đồng bộ.

## Bảng ký hiệu chuẩn

| STT | Khái niệm             | Ký hiệu thống nhất              | Ký hiệu trong Code                                       | Ghi chú                                                   |
| --- | --------------------- | ------------------------------- | -------------------------------------------------------- | --------------------------------------------------------- |
| 1   | State space           | $S$                             | `env.observation_space`                                  | Không gian trạng thái trong MDP.                          |
| 2   | State dimension       | $\mathbb{R}^4$                  | `state_dim = 4` (trong `PolicyNetwork`)                  | CartPole-v1 state là vector 4 chiều liên tục.             |
| 3   | State                 | $s_t$                           | `state`                                                  | Trạng thái tại thời điểm $t$.                             |
| 4   | Next state            | $s_{t+1}$                       | `next_state` (từ `env.step`)                             | Trạng thái tiếp theo sau transition.                      |
| 5   | CartPole pole angle   | $\phi$                          | `state[2]` (thành phần thứ 3 của state vector)           | Không dùng $\theta$ để tránh trùng với policy parameters. |
| 6   | Action space          | $A$                             | `env.action_space`                                       | Không gian hành động trong MDP.                           |
| 7   | Action                | $a_t$                           | `action`                                                 | Hành động tại thời điểm $t$.                              |
| 8   | Immediate reward      | $r_{t+1}$                       | `reward` (trả về từ `env.step`)                          | Reward nhận sau khi thực hiện $a_t$.                      |
| 9   | Reward function       | $R(s_t,a_t)$                    | `reward` (từ môi trường CartPole)                        | Hàm reward trong MDP.                                     |
| 10  | Environment dynamics  | $P(s_{t+1} \mid s_t, a_t)$      | `env.step(action)` (CartPole internals)                  | Transition dynamics, không phụ thuộc $\theta$.            |
| 11  | Discount factor       | $\gamma$                        | `gamma` (param truyền vào `compute_returns`)             | Hệ số chiết khấu future reward.                           |
| 12  | Policy parameters     | $\theta$                        | `policy_net.parameters()`, `theta` trong docstring       | Dành riêng cho tham số của policy network.                |
| 13  | Policy                | $\pi_\theta(a_t \mid s_t)$      | `probs`, `policy_net.forward(state)`                     | Xác suất chọn action $a_t$ tại state $s_t$.               |
| 14  | Log-policy            | $\log \pi_\theta(a_t \mid s_t)$ | `log_prob` (từ `Categorical.log_prob`)                   | Log-xác suất action được chọn.                            |
| 15  | Trajectory            | $\tau$                          | Một episode rollout (`while not done`)                   | Một episode hoặc chuỗi tương tác.                         |
| 16  | Time horizon          | $T$                             | `max_steps = 500` (CartPole limit)                       | Độ dài tối đa của một episode.                            |
| 17  | Trajectory return     | $R(\tau)$                       | `total_reward = sum(rewards)`                            | Tổng reward của cả trajectory.                            |
| 18  | Objective function    | $J(\theta)$                     | `episode_rewards`, `total_reward` (Monte-Carlo estimate) | Expected return cần maximize.                             |
| 19  | Reward-to-go          | $G_t$                           | `returns` (từ `compute_returns()`), `G_t` trong loop     | Tổng reward tương lai từ thời điểm $t$.                   |
| 20  | Learning rate         | $\alpha$                        | `lr` (truyền vào `optim.Adam`)                           | Tốc độ cập nhật gradient.                                 |
| 21  | Number of episodes    | $N$                             | `num_episodes`, `episodes` (CLI arg)                     | Số episode huấn luyện.                                    |
| 22  | Gradient update       | $\nabla_\theta J(\theta)$       | `policy_loss.backward()`, `optimizer.step()`             | Backprop + cập nhật weights.                              |
| 23  | PyTorch loss          | $L(\theta)$                     | `policy_loss` (trong `update_policy`)                    | Loss âm để optimizer minimize → maximize $J(\theta)$.     |
| 24  | Baseline              | $b(s_t)$                        | `(returns - returns.mean()) / (returns.std() + 1e-8)`    | Standardization giảm variance, không gây bias.            |
| 25  | Action-value function | $Q(s,a)$                        | Không hiện thực (PG không dùng Q)                        | Dùng khi so sánh với value-based methods.                 |

## 1. CartPole state vector

**Chưa đồng nhất:** Dùng $\theta$ cho góc CartPole trong state vector, trong khi $\theta$ cũng là policy parameters.

**Nên sửa thành:**

$$
s_t = [x, \dot{x}, \phi, \dot{\phi}]
$$

**Ghi chú:** Giữ $\theta$ chỉ cho tham số của policy network để tránh một ký hiệu mang hai nghĩa.

**Áp dụng cho Code:** Trong `sources/models/policy.py` và `sources/train.py`, `state` là numpy array 4 chiều; thành phần `state[2]` đại diện cho góc nghiêng. Không dùng `theta` làm tên biến cho góc.

**Bổ sung:** CartPole-v1 state vector thuộc không gian $\mathbb{R}^4$, tức $s_t \in \mathbb{R}^4$. Trong code, `state_dim = 4` được truyền vào `PolicyNetwork`.

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

**Áp dụng cho Code:** Trong `sources/models/policy.py`, docstring ghi `pi(a | s, theta)` → sửa thành `pi_theta(a_t | s_t)`. Trong `sources/reinforce.py` comment, dùng `log_prob(a|s, theta)` → sửa thành `log pi_theta(a_t | s_t)`.

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

**Áp dụng cho Code:** Trong `sources/train.py`, `episode_rewards` lưu tổng reward từng episode (`total_reward = sum(rewards)`). Đây chính là quan sát mẫu của $R(\tau)$.

## 4. Trajectory probability

**Chưa đồng nhất:** Trajectory probability dễ bị viết gọn thành $P(\tau)$ hoặc chỉ còn tích các policy, thiếu dynamics môi trường.

**Nên sửa thành:**

$$
P(\tau \mid \theta)
= \rho_0(s_0)\prod_{t=0}^{T}\pi_\theta(a_t \mid s_t)P(s_{t+1}\mid s_t,a_t)
$$

**Ghi chú:** Khi lấy đạo hàm theo $\theta$, chỉ policy phụ thuộc $\theta$; dynamics của CartPole không phụ thuộc policy parameters.

**Áp dụng cho Code:** `env.step(action)` trong `sources/train.py` sinh ra transition $(s_t, a_t, r_{t+1}, s_{t+1})$. Đạo hàm `policy_loss.backward()` chỉ backprop qua policy network, không qua môi trường.

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

**Áp dụng cho Code:** Trong `sources/reinforce.py`, comment dùng `ln` → đổi thành `log`. Code dùng `m.log_prob(action)` từ PyTorch `Categorical`, đây là $\log$ tự nhiên.

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

**Áp dụng cho Code:** `sources/reinforce.py` tính `returns` bằng `compute_returns(rewards, gamma)` — đây là $G_t$. `update_policy` dùng `log_prob * G_t` tương ứng với $\log \pi_\theta(a_t \mid s_t) \cdot G_t$.

## 7. Reward-to-go

**Chưa đồng nhất:** Công thức bị dẹt kiểu `Gt = ΣTk=t γk-t rk+1`, mất chỉ số trên/dưới.

**Nên sửa thành:**

$$
G_t = \sum_{k=t}^{T}\gamma^{k-t}r_{k+1}
$$

**Ghi chú:** Nên dùng $r_{k+1}$ nhất quán với quy ước reward nhận sau transition từ time $k$.

**Áp dụng cho Code:** Trong `sources/reinforce.py:12`, comment ghi `R_k` → sửa thành `r_{k+1}`. Hàm `compute_returns()` duyệt ngược: `G_t = r + gamma * G_t`, đúng với công thức $G_t = \sum_{k=t}^{T}\gamma^{k-t}r_{k+1}$.

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

**Áp dụng cho Code:** Trong `sources/reinforce.py`, `optimizer.step()` sau `policy_loss.backward()` thực hiện gradient descent trên loss âm, tương đương gradient ascent trên $J(	heta)$.

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

**Áp dụng cho Code:** `sources/reinforce.py:50` `policy_loss.append(-log_prob * G_t)` là hiện thực của $-\log \pi_	heta(a_t \mid s_t)G_t$.

## 10. Return normalization symbols

**Chưa đồng nhất:** Trong report/slide, công thức normalization dùng $\mu(G)$, $\sigma(G)$, $\varepsilon$ nhưng chưa định nghĩa rõ trong bảng chuẩn.

**Nên sửa thành:**

$$
G_t \leftarrow \frac{G_t - \mu(G)}{\sigma(G) + \varepsilon}
$$

Trong đó:

- $\mu(G)$ — mean (trung bình) của returns trong episode
- $\sigma(G)$ — standard deviation (độ lệch chuẩn) của returns
- $\varepsilon$ — epsilon nhỏ (thường $10^{-8}$) để tránh chia cho 0

**Ghi chú:** Normalization giảm variance của gradient estimator, là dạng baseline đơn giản nhất trong code.

**Áp dụng cho Code:** `(returns - returns.mean()) / (returns.std() + 1e-8)` trong `sources/reinforce.py:42`.

## 11. Baseline subtraction

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

**Áp dụng cho Code:** `sources/reinforce.py:42` `(returns - returns.mean()) / (returns.std() + 1e-8)` là standardization — dạng baseline đơn giản nhất trong code. Đảm bảo docstring nói rõ "baseline đơn giản" thay vì chỉ "chuẩn hóa".

## Thứ tự sửa khuyến nghị

| STT | Nội dung                                                                          | Phạm vi                        |
| --- | --------------------------------------------------------------------------------- | ------------------------------ |
| 1   | Đổi CartPole pole angle từ $\theta$ sang $\phi$.                                  | Report, Slide, Code comments   |
| 2   | Chuẩn hóa mọi policy thành $\pi_\theta(a_t \mid s_t)$.                            | Report, Slide, Code docstrings |
| 3   | Sửa reward-to-go thành $G_t = \sum_{k=t}^{T}\gamma^{k-t}r_{k+1}$.                 | Report, Slide, Code comments   |
| 4   | Tách rõ $R(s_t,a_t)$, $r_{t+1}$, $R(\tau)$, và $G_t$.                             | Report, Slide, Code docstrings |
| 5   | Trong proof, dùng $\log$ nhất quán, không lẫn `ln`.                               | Report, Slide, Code comments   |
| 6   | Sửa baseline proof theo đúng dạng expectation trên action.                        | Report, Slide                  |
| 7   | Định nghĩa rõ $J(\theta)$ với phân phối $\tau \sim \pi_\theta$ khi xuất hiện.     | Report, Slide                  |
| 8   | Đồng bộ $s_{t+1}$ (next state) thay vì viết gọn hoặc dùng tên biến không rõ.      | Report, Slide, Code comments   |
| 9   | Mô tả CartPole state space bằng $\mathbb{R}^4$ thay vì chỉ nói "4 chiều".         | Report, Slide                  |
| 10  | Định nghĩa rõ $\mu(G)$, $\sigma(G)$, $\varepsilon$ trong công thức normalization. | Report, Slide                  |
