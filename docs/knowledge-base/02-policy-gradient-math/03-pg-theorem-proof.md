# Chứng minh Định lý Policy Gradient (toàn văn)

Định lý Policy Gradient (PG Theorem) là nền tảng cho mọi thuật toán RL dựa trên tối ưu hóa tham số chính sách (như REINFORCE, PPO, TRPO). Tài liệu này thực hiện chứng minh chi tiết định lý này cho trường hợp không gian hành động rời rạc.

## 1. Phát biểu Định lý

Cho một hàm mục tiêu $J(\theta) = \mathbb{E}_{\pi_{\theta}} [R(\tau)]$, đạo hàm của nó theo $\theta$ được tính bởi:

$$
\nabla_{\theta} J(\theta) = \mathbb{E}_{\pi_{\theta}} \left[ \sum_{t=0}^{T} \nabla_{\theta} \ln \pi_{\theta}(a_t | s_t) G_t \right]
$$

Trong đó $G_t = \sum_{k=t}^{T} \gamma^{k-t} r_{k+1}$ là Return tính từ thời điểm $t$.

## 2. Các bước chứng minh

### Bước 1: Chuyển đạo hàm vào trong kỳ vọng (sử dụng Log-derivative Trick)

Ta bắt đầu từ định nghĩa của kỳ vọng:

$$
J(\theta) = \sum_{\tau} P(\tau|\theta) R(\tau)
$$

Lấy đạo hàm hai vế:

$$
\begin{aligned}
\nabla_{\theta} J(\theta) &= \nabla_{\theta} \sum_{\tau} P(\tau|\theta) R(\tau) \\
&= \sum_{\tau} \nabla_{\theta} P(\tau|\theta) R(\tau)
\end{aligned}
$$

Áp dụng Log-derivative trick $\nabla_{\theta} P = P \nabla_{\theta} \ln P$:

$$
\begin{aligned}
\nabla_{\theta} J(\theta) &= \sum_{\tau} P(\tau|\theta) \frac{\nabla_{\theta} P(\tau|\theta)}{P(\tau|\theta)} R(\tau) \\
&= \sum_{\tau} P(\tau|\theta) \nabla_{\theta} \ln P(\tau|\theta) R(\tau) \\
&= \mathbb{E}_{\tau \sim \pi_{\theta}} [R(\tau) \nabla_{\theta} \ln P(\tau|\theta)]
\end{aligned}
$$

Tiếp theo, ta khai triển biểu thức $\nabla_{\theta} \ln P(\tau|\theta)$. Với $\tau = (s_0, a_0, \dots, s_T, a_T)$:

$$
\ln P(\tau|\theta) = \ln \left( \mu(s_0) \prod_{t=0}^T \pi_{\theta}(a_t|s_t) P(s_{t+1}|s_t, a_t) \right)
$$

$$
\ln P(\tau|\theta) = \ln \mu(s_0) + \sum_{t=0}^T \ln \pi_{\theta}(a_t|s_t) + \sum_{t=0}^T \ln P(s_{t+1}|s_t, a_t)
$$

Lấy đạo hàm theo $\theta$:

$$
\nabla_{\theta} \ln P(\tau|\theta) = \nabla_{\theta} \ln \mu(s_0) + \sum_{t=0}^T \nabla_{\theta} \ln \pi_{\theta}(a_t|s_t) + \nabla_{\theta} \sum_{t=0}^T \ln P(s_{t+1}|s_t, a_t)
$$

Vì $\mu(s_0)$ và dynamics $P(s_{t+1}|s_t, a_t)$ không phụ thuộc vào $\theta$, đạo hàm của chúng bằng 0:

$$
\nabla_{\theta} \ln P(\tau|\theta) = 0 + \sum_{t=0}^T \nabla_{\theta} \ln \pi_{\theta}(a_t|s_t) + 0
$$

Thay vào biểu thức trên:

$$
\nabla_{\theta} J(\theta) = \mathbb{E}_{\pi_{\theta}} \left[ R(\tau) \left( \sum_{t=0}^{T} \nabla_{\theta} \ln \pi_{\theta}(a_t | s_t) \right) \right]
$$

### Bước 2: Khai triển tổng phần thưởng $R(\tau)$

Ta có $R(\tau) = \sum_{t=0}^{T} \gamma^t r_{t+1}$.

Thay vào biểu thức gradient ở Bước 1:

$$
\nabla_{\theta} J(\theta) = \mathbb{E}_{\pi_{\theta}} \left[ \left( \sum_{t=0}^{T} \nabla_{\theta} \ln \pi_{\theta}(a_t | s_t) \right) \left( \sum_{t=0}^{T} \gamma^t r_{t+1} \right) \right]
$$

Áp dụng **Bổ đề Nhân quả** (Causality Lemma, xem Mục 4 bên dưới): hành động tại thời điểm $t$ chỉ ảnh hưởng đến phần thưởng từ $t$ trở đi, nên ta thay $R(\tau)$ bằng **Reward-to-go** $G_t = \sum_{k=t}^{T} \gamma^{k-t} r_{k+1}$:

$$
\boxed{\nabla_{\theta} J(\theta) = \mathbb{E}_{\pi_{\theta}} \left[ \sum_{t=0}^{T} \nabla_{\theta} \ln \pi_{\theta}(a_t | s_t) \cdot G_t \right]}
$$

Đây là dạng cuối cùng của **Policy Gradient Theorem** mà thuật toán REINFORCE sử dụng.

## 3. Ước lượng thực tế (Monte Carlo Estimator)

> **Lưu ý:** Phần này KHÔNG thuộc chứng minh định lý mà là bước chuyển từ lý thuyết sang thực hành.

Vì ta không thể tính kỳ vọng $\mathbb{E}_{\pi_\theta}[\cdot]$ một cách chính xác (trajectory space quá lớn), ta xấp xỉ bằng trung bình $N$ trajectory đã lấy mẫu:

$$
\nabla_{\theta} J(\theta) \approx \frac{1}{N} \sum_{i=1}^N \left( \sum_{t=0}^T \nabla_{\theta} \ln \pi_{\theta}(a_t^i | s_t^i) \cdot G_t^i \right)
$$

### Trực giác "Push-Pull"

![Policy Gradient Update](../assets/probability-pushing.png)

- Nếu $G_t$ dương (phần thưởng cao): Gradient sẽ đẩy xác suất của hành động $a_t$ lên cao.
- Nếu $G_t$ âm hoặc thấp: Xác suất của hành động đó sẽ bị kéo xuống (tương đối so với các hành động khác).

## 4. Chứng minh Bổ đề Nhân quả (Causality)

Trong REINFORCE, chúng ta thay thế tổng phần thưởng cả trajectory $R(\tau)$ bằng phần thưởng tương lai (reward-to-go) $G_t = \sum_{k=t}^T \gamma^{k-t} r_{k+1}$. Tại sao ta có thể bỏ qua các phần thưởng trong quá khứ ($r_{k < t}$)?

**Chứng minh:**

Ta cần chứng minh rằng phần thưởng quá khứ không đóng góp vào gradient kỳ vọng:

$$
\mathbb{E}_{\tau \sim \pi} \left[ \nabla_{\theta} \ln \pi(a_t|s_t) \cdot r_{k+1} \right] = 0 \text{ với } k < t
$$

Sử dụng luật kỳ vọng lặp (Law of Iterated Expectations):

$$
\mathbb{E}_{s_t, a_t} \left[ \nabla_{\theta} \ln \pi_{\theta}(a_t|s_t) \cdot r_{k+1} \right] = \mathbb{E}_{s_t} \left[ r_{k+1} \cdot \mathbb{E}_{a_t \sim \pi_{\theta}} [\nabla_{\theta} \ln \pi_{\theta}(a_t|s_t) | s_t] \right]
$$

Xét số hạng bên trong:

$$
\mathbb{E}_{a_t \sim \pi_{\theta}} [\nabla_{\theta} \ln \pi_{\theta}(a_t|s_t) | s_t] = \sum_{a} \pi_{\theta}(a|s_t) \frac{\nabla_{\theta} \pi_{\theta}(a|s_t)}{\pi_{\theta}(a|s_t)} = \nabla_{\theta} \sum_{a} \pi_{\theta}(a|s_t) = \nabla_{\theta} (1) = 0
$$

Vì số hạng này luôn bằng 0, các phần thưởng quá khứ $r_{k+1}$ ($k < t$) không làm thay đổi kỳ vọng của gradient, nhưng việc loại bỏ chúng giúp giảm phương sai (variance) đáng kể.

Do đó, ta có thể rút gọn tổng bên trong:

$$
\nabla_{\theta} J(\theta) = \mathbb{E}_{\pi_{\theta}} \left[ \sum_{t=0}^{T} \nabla_{\theta} \ln \pi_{\theta}(a_t | s_t) \left( \sum_{k=t}^{T} \gamma^{k-t} r_{k+1} \right) \right]
$$

Biểu thức $\sum_{k=t}^{T} \gamma^{k-t} r_{k+1}$ chính là $G_t$ như đã định nghĩa ở Mục 1.

## 5. Thuật toán REINFORCE

Dựa trên định lý này, thuật toán REINFORCE thực hiện các bước:

1.  Cho Agent chạy thử để thu thập một trajectory $\tau$.
2.  Với mỗi bước $t$ trong trajectory, tính $G_t$.
3.  Cập nhật $\theta \leftarrow \theta + \alpha \sum_{t} \nabla_{\theta} \ln \pi_{\theta}(a_t|s_t) G_t$.

## 6. Ý nghĩa vật lý

- Nếu $G_t > 0$ (kết quả tốt): Chúng ta đẩy tham số $\theta$ theo hướng $\nabla_{\theta} \ln \pi_{\theta}$, tức là **tăng** xác suất chọn hành động $a_t$ tại trạng thái $s_t$.
- Nếu $G_t < 0$ (kết quả xấu): Chúng ta đẩy $\theta$ theo hướng ngược lại, tức là **giảm** xác suất chọn hành động đó.

Đây chính là cơ chế "Học tăng cường" (Reinforcement) được cụ thể hóa bằng toán học.

---

## Nguồn tham khảo

- **Sutton & Barto (2018).** *Reinforcement Learning: An Introduction*, 2nd Ed. — Theorem 13.1: Policy Gradient Theorem (p.327), §13.3 REINFORCE algorithm (p.328). [Online](http://incompleteideas.net/book/the-book-2nd.html)
- **Williams, R.J. (1992).** "Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning." *Machine Learning*, 8, 229-256. — Bài báo gốc đề xuất thuật toán REINFORCE.
- **OpenAI Spinning Up.** Part 3 — Full derivation + "Expected Grad-Log-Prob Lemma" (cơ sở cho Bổ đề Nhân quả) + "Don't Let the Past Distract You" (Reward-to-go). [Link](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html)
- **Sutton, R.S. et al. (2000).** "Policy Gradient Methods for Reinforcement Learning with Function Approximation." NIPS. — Chứng minh chính thức PG Theorem cho function approximation.
