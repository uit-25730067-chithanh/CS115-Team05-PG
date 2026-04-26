# Giải tích, Gradient và Bài toán tối ưu Expectation

Tại sao chúng ta lại cần tính Gradient? Và tại sao Gradient trong RL lại khác biệt so với Deep Learning truyền thống?

## 1. Gradient Ascent: Leo núi tìm cực đại

Trong đa số các bài toán Machine Learning, chúng ta dùng Gradient Descent để giảm thiểu sai số (Loss). Tuy nhiên, trong RL, chúng ta muốn **tối đa hóa** phần thưởng, vì vậy chúng ta dùng **Gradient Ascent**:

$$
\theta_{new} = \theta_{old} + \alpha \nabla_{\theta} J(\theta)
$$

Trong đó $\nabla_{\theta} J(\theta)$ là vector chỉ hướng tăng nhanh nhất của hàm mục tiêu $J(\theta)$.

## 2. Nút thắt: Đạo hàm của một Kỳ vọng (Derivative of Expectation)

Hãy xem xét hàm mục tiêu của chúng ta:

$$
J(\theta) = \mathbb{E}_{\tau \sim \pi_{\theta}} [R(\tau)] = \int P(\tau | \theta) R(\tau) d\tau
$$

Chúng ta cần tính $\nabla_{\theta} J(\theta)$. Thông thường, nếu muốn tính đạo hàm của một tích phân, ta có thể đưa đạo hàm vào bên trong:

$$
\nabla_{\theta} \int P(\tau | \theta) R(\tau) d\tau = \int \nabla_{\theta} P(\tau | \theta) R(\tau) d\tau
$$

**Vấn đề:** Biểu thức $\int \nabla_{\theta} P(\tau | \theta) R(\tau) d\tau$ không còn là một kỳ vọng (Expectation) nữa, vì $\nabla_{\theta} P(\tau | \theta)$ không phải là một hàm mật độ xác suất (tổng của nó không bằng 1). Điều này khiến chúng ta không thể sử dụng phương pháp lấy mẫu (Sampling) để tính toán giá trị này một cách hiệu quả trên máy tính.

## 3. Giải pháp: Log-derivative Trick

Để biến biểu thức trên quay trở lại dạng kỳ vọng, chúng ta sử dụng một đồng nhất thức giải tích đơn giản:

$$
\frac{d}{dx} \log(f(x)) = \frac{f'(x)}{f(x)} \implies f'(x) = f(x) \frac{d}{dx} \log(f(x))
$$

Áp dụng vào xác suất quỹ đạo:

$$
\nabla_{\theta} P(\tau | \theta) = P(\tau | \theta) \nabla_{\theta} \log P(\tau | \theta)
$$

Thay ngược lại vào tích phân:

$$
\nabla_{\theta} J(\theta) = \int P(\tau | \theta) \nabla_{\theta} \log P(\tau | \theta) R(\tau) d\tau = \mathbb{E}_{\tau \sim \pi_{\theta}} [\nabla_{\theta} \log P(\tau | \theta) R(\tau)]
$$

**Kết luận quan trọng:** Nhờ Log-derivative trick, chúng ta đã biến đạo hàm của một kỳ vọng thành **kỳ vọng của một đạo hàm log**. Điều này cho phép chúng ta chỉ cần cho Agent "chơi thử" (lấy mẫu $\tau$), tính $\nabla_{\theta} \log P$ và nhân với phần thưởng nhận được để cập nhật mạng neural. Đây chính là nền tảng của thuật toán REINFORCE.

---

## Nguồn tham khảo

- **Sutton & Barto (2018).** *Reinforcement Learning: An Introduction*, 2nd Ed. — §13.2–13.3 Gradient Ascent and Policy Gradient (p.326-328). [Online](http://incompleteideas.net/book/the-book-2nd.html)
- **OpenAI Spinning Up.** Part 3 — "Deriving the Simplest Policy Gradient", Eq.1–5. [Link](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html)
