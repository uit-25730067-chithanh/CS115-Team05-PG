# Định nghĩa Reinforcement Learning qua lăng kính MDP

Reinforcement Learning (RL) không đơn thuần là việc "thử và sai". Về mặt toán học, RL là bài toán tối ưu hóa một hàm mục tiêu dựa trên các quyết định tuần tự trong một môi trường bất định.

## 1. Khung toán học: Markov Decision Process (MDP)

Mọi bài toán RL đều được mô hình hóa dưới dạng một bộ 5 thành phần $(S, A, P, R, \gamma)$:

![Agent Environment Loop Chalkboard](../assets/rl-loop-chalkboard.png)

1.  **State Space ($S$):** Tập hợp các trạng thái có thể có của môi trường.
    *   *Tính chất Markov:* Trạng thái hiện tại $S_t$ phải chứa đầy đủ thông tin để dự đoán tương lai mà không cần biết lịch sử quá khứ: $P(S_{t+1} | S_t, A_t, S_{t-1}, A_{t-1}, \dots) = P(S_{t+1} | S_t, A_t)$.
    *   *Ví dụ CartPole:* $s = [x, \dot{x}, \theta, \dot{\theta}]$ (vị trí xe, vận tốc xe, góc cực, vận tốc góc).
2.  **Action Space ($A$):** Tập hợp các hành động mà Agent có thể thực hiện.
    *   *Ví dụ CartPole:* $a \in \{0, 1\}$ (đẩy trái hoặc đẩy phải).
3.  **Transition Probability ($P(s' | s, a)$):** Xác suất môi trường chuyển sang trạng thái $s'$ khi Agent thực hiện hành động $a$ tại trạng thái $s$. Điều này thể hiện tính ngẫu nhiên của môi trường.
4.  **Reward Function ($R(s, a, s')$):** Giá trị vô hướng nhận được sau mỗi bước chuyển đổi.
5.  **Discount Factor ($\gamma$):** Hệ số chiết khấu ($0 \le \gamma \le 1$), thể hiện tầm quan trọng của các phần thưởng trong tương lai so với hiện tại.

## 2. Agent và Policy ($\pi$)

Agent tương tác với môi trường thông qua một **Policy** (Chính sách). Trong thuật toán REINFORCE, chúng ta sử dụng một chính sách ngẫu nhiên (stochastic policy) được tham số hóa bởi $\theta$:

$$\pi_{\theta}(a|s) = P(A_t = a | S_t = s; \theta)$$

Điều này có nghĩa là: Tại trạng thái $s$, Agent sẽ chọn hành động $a$ với xác suất được tính toán bởi mạng neural có trọng số $\theta$.

## 3. Mục tiêu của Reinforcement Learning

Mục tiêu tối thượng là tìm ra bộ tham số $\theta$ sao cho **Expected Return** (Kỳ vọng tổng phần thưởng) là lớn nhất:

$$
J(\theta) = \mathbb{E}_{\pi_{\theta}} \left[ \sum_{t=0}^{\infty} \gamma^t R_{t+1} \right]
$$

Trong đó, $J(\theta)$ được gọi là hàm mục tiêu (objective function). Công việc của chúng ta là thực hiện Gradient Ascent trên $J(\theta)$ để cập nhật mạng neural.

## 4. Tại sao bài toán này khó?

Khác với Supervised Learning (Học có giám sát), nơi chúng ta biết rõ "nhãn" đúng để tính đạo hàm trực tiếp, trong RL:
1.  Chúng ta không biết hành động nào là tối ưu ngay lập tức (Sparse rewards).
2.  Hành động hiện tại ảnh hưởng đến các trạng thái tương lai (Sequential dependencies).
3.  Hàm mục tiêu $J(\theta)$ là một kỳ vọng trên các quỹ đạo (trajectories), và chúng ta không thể tính đạo hàm trực tiếp qua các xác suất chuyển trạng thái $P(s'|s, a)$ của môi trường vì chúng thường là ẩn (unknown environment dynamics).
