# Hàm mục tiêu $J(\theta)$ và Performance Measure

Trong Reinforcement Learning, mục tiêu của chúng ta là tìm một chính sách tối ưu. Để làm được điều này, trước hết ta phải định nghĩa một "thước đo hiệu suất" (Performance Measure) để đánh giá xem một bộ tham số $\theta$ của mạng neural là tốt hay xấu.

## 1. Định nghĩa toán học của $J(\theta)$

Hàm mục tiêu $J(\theta)$ được định nghĩa là kỳ vọng của tổng phần thưởng tích lũy (Return) trên tất cả các quỹ đạo (trajectories) có thể xảy ra dưới chính sách $\pi_\theta$:

$$J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} [R(\tau)]$$

![J(theta) Chalkboard Explanation](../assets/j-theta-chalkboard.png)

Triển khai dưới dạng tích phân (hoặc tổng đối với không gian rời rạc):

$$J(\theta) = \int_{\mathbb{T}} P(\tau | \theta) R(\tau) d\tau$$

Trong đó:
*   $\mathbb{T}$: Không gian của tất cả các quỹ đạo có thể có.
*   $P(\tau | \theta)$: Xác suất xảy ra quỹ đạo $\tau$ khi Agent sử dụng tham số $\theta$.
*   $R(\tau)$: Tổng phần thưởng tích lũy của quỹ đạo $\tau$.

## 2. Phân tích xác suất quỹ đạo $P(\tau | \theta)$

Xác suất của một quỹ đạo $\tau = (s_0, a_0, s_1, a_1, \dots, s_T, a_T)$ được tính bằng quy tắc nhân xác suất (Chain Rule of Probability):

$$P(\tau | \theta) = \mu(s_0) \prod_{t=0}^{T} \pi_\theta(a_t | s_t) P(s_{t+1} | s_t, a_t)$$

Trong đó:
*   $\mu(s_0)$: Phân phối trạng thái khởi đầu.
*   $\pi_\theta(a_t | s_t)$: Mô hình chính sách (Policy Model) - đây là phần chúng ta kiểm soát.
*   $P(s_{t+1} | s_t, a_t)$: Mô hình chuyển trạng thái của môi trường (Environment Dynamics) - đây là phần chúng ta **không** kiểm soát và thường không biết trước.

## 3. Ý nghĩa của việc tối ưu hóa $J(\theta)$

Tại sao chúng ta lại tối ưu hóa kỳ vọng thay vì tối ưu hóa một ván chơi cụ thể?
1.  **Tính ngẫu nhiên (Stochasticity):** Cả chính sách $\pi_\theta$ và môi trường $P$ đều có thể mang tính ngẫu nhiên. Việc tối ưu hóa dựa trên một ván chơi duy nhất có thể dẫn đến hiện tượng "overfitting" vào một chuỗi may mắn.
2.  **Khả năng tổng quát hóa:** Bằng cách tối đa hóa $J(\theta)$, chúng ta đang yêu cầu Agent tìm ra các hành động có xác suất mang lại phần thưởng cao trên mức trung bình ở mọi tình huống.

## 4. Liên hệ với CartPole-v1

Trong môi trường CartPole:
*   Mỗi episode kết thúc khi thanh gỗ đổ hoặc xe đi quá giới hạn.
*   $R(\tau) = \text{Số bước sống sót}$ (vì mỗi bước được +1 reward).
*   Nếu $J(\theta) = 500$, điều đó có nghĩa là trung bình Agent của chúng ta có thể giữ thanh gỗ đứng vững trong toàn bộ thời gian cho phép của môi trường.

Mục tiêu của thuật toán REINFORCE là tính toán $\nabla_\theta J(\theta)$ để thực hiện cập nhật $\theta \leftarrow \theta + \alpha \nabla_\theta J(\theta)$.

## 5. Từ $R(\tau)$ đến Reward-to-go ($G_t$)

Trong lý thuyết cơ bản, ta dùng $R(\tau)$ là tổng phần thưởng của cả quỹ đạo. Tuy nhiên, trong thực tế và mã nguồn, ta thường sử dụng **Reward-to-go** ($G_t$) để tính gradient tại mỗi thời điểm $t$.

**Định nghĩa $G_t$:**
$$G_t = \sum_{k=t}^{T} \gamma^{k-t} r_{k+1}$$

**Tại sao lại dùng $G_t$ thay vì $R(\tau)$?**
- **Tính nhân quả (Causality):** Hành động tại thời điểm $t$ chỉ có thể ảnh hưởng đến các phần thưởng từ $t$ trở về sau. Việc bao gồm các phần thưởng trong quá khứ (từ $0$ đến $t-1$) vào công thức tính gradient tại $t$ chỉ làm tăng **phương sai (variance)** mà không giúp ích gì cho việc học (vì action $a_t$ không gây ra $r_{0 \dots t-1}$).
- **Mapping vào Code:** Trong file `sources/train.py`, bạn sẽ thấy bước tính `returns = compute_returns(...)` chính là phần hiện thực chuỗi $G_t$ này cho mỗi step trước khi thực hiện backpropagation.
