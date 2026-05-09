# Tối ưu hóa trong Học Tăng cường: Gradient Ascent & Policy Gradient

## 1. Cơ chế cập nhật trọng số: $\theta \leftarrow \theta + \alpha \nabla J(\theta)$

Công thức cập nhật này thuộc về **Gradient Ascent** (lên dốc), khác với Gradient Descent (xuống dốc) thường thấy trong học sâu. Mục tiêu là **tối đa hóa** hàm mục tiêu $J(\theta)$.

### Mô hình hóa Gradient Ascent

**Liên kết minh họa:** [https://www.geogebra.org/calculator/bmd2rdyd](https://www.geogebra.org/calculator/bmd2rdyd)

Trong mô phỏng này:
- Trục $x$ biểu diễn tham số $\theta$ (chính sách).
- Trục $y$ biểu diễn giá trị hàm $J(\theta)$ (ví dụ: tổng phần thưởng kỳ vọng).
- Đường cong thể hiện một hàm lồi (hoặc có đỉnh) mà ta muốn đạt đỉnh cao nhất.

**Cơ chế hoạt động:**

1. Xuất phát từ điểm $\theta$ hiện tại, tính **đạo hàm (độ dốc)** $\nabla J(\theta)$. Đạo hàm dương → hàm đang đi lên, đạo hàm âm → hàm đi xuống.

2. Trong **Gradient Ascent**, ta muốn tăng $J(\theta)$, nên đi **theo hướng của gradient**:

   $$\theta_{\text{new}} = \theta_{\text{old}} + \alpha \cdot \nabla J(\theta_{\text{old}})$$

3. $\alpha$ là **tốc độ học** (learning rate) – điều khiển bước nhảy dọc theo độ dốc.

4. Quá trình lặp lại cho đến khi hội tụ tại đỉnh (cực đại địa phương).

> Thao tác trên GeoGebra: Kéo tham số hoặc xem đồ thị minh họa đường đi lên đỉnh của một hàm đa biến.

### Mô hình hóa Policy Gradient

**Liên kết minh họa:** [https://www.geogebra.org/calculator/vmqne9w4](https://www.geogebra.org/calculator/vmqne9w4)

Trong Học Tăng cường:
- $\theta$ là tham số của **chính sách** (policy) $\pi_{\theta}(a|s)$ – xác suất chọn hành động $a$ ở trạng thái $s$.
- $J(\theta)$ là **phần thưởng kỳ vọng** khi tuân theo chính sách $\theta$.
- **Policy Gradient** tính $\nabla J(\theta)$ bằng cách lấy mẫu các quỹ đạo tương tác với môi trường.

**Cơ chế:**

- Với mỗi bước cập nhật, thu thập dữ liệu trải nghiệm $(s, a, r)$.
- Ước lượng gradient.
- Cập nhật $\theta \leftarrow \theta + \alpha \nabla J(\theta)$ để tăng xác suất sinh ra các hành động có phần thưởng cao.

> GeoGebra trong link này có thể minh họa không gian tham số và hướng tăng dần của phần thưởng.

---

## 2. Log-derivative trick: Tại sao cần $\nabla \log \pi = \frac{\nabla \pi}{\pi}$?

**Log-derivative trick** là phép biến đổi toán học quan trọng trong Policy Gradient.

### Công thức

$$\nabla_{\theta} \log \pi_{\theta}(a|s) = \frac{\nabla_{\theta} \pi_{\theta}(a|s)}{\pi_{\theta}(a|s)}$$

### Tại sao phải dùng?

1. **Tránh tính gradient trực tiếp của xác suất:** Gradient gốc của $J(\theta)$ có dạng:

   $$\nabla_{\theta} J(\theta) = \mathbb{E} \left[ \sum_{t} R_t \cdot \nabla_{\theta} \log \pi_{\theta}(a_t|s_t) \right]$$

   Xuất hiện $\frac{\nabla \pi}{\pi}$ nhờ kỹ thuật **log-derivative**.

2. **Cho phép lấy mẫu (likelihood ratio trick):** Nếu không dùng log, ta có $\nabla \pi$ nhưng không thể ước lượng qua mẫu vì không thể lấy mẫu trực tiếp gradient. Log giúp viết kỳ vọng dưới dạng:

   $$\mathbb{E}[R \cdot \nabla \log \pi]$$

   → Rất dễ ước lượng bằng trung bình mẫu từ các quỹ đạo thực tế.

3. **Ổn định số học:** Khi $\pi$ rất nhỏ, $\frac{\nabla \pi}{\pi}$ ít bị tràn hơn so với tính trực tiếp $\nabla \pi$.

### Ví dụ cụ thể

Giả sử $\pi(a|s) = 0.01$, $\nabla \pi = 0.0005$.

Khi đó:
- $\frac{\nabla \pi}{\pi} = 0.05$ – gọn gàng, ổn định.
- $\nabla \pi = 0.0005$ – rất nhỏ, dễ gây vanishing gradient khi nhân với hệ số.

---

## 3. Mục tiêu tối ưu hóa $J(\theta)$

Trong Học Tăng cường, $J(\theta)$ là **hàm phần thưởng kỳ vọng** (expected return) khi tác tử theo chính sách $\pi_{\theta}$.

### Các dạng phổ biến

| Loại môi trường | Công thức $J(\theta)$ |
|----------------|------------------------|
| Tập từng bước (episodic) | $$J(\theta) = \mathbb{E}{\tau \sim \pi{\theta}} \left[ \sum_{t=0}^{T} \gamma^t r_t \right]$$|
| Liên tục (continuing) | $$J(\theta) = \lim_{T \to \infty} \frac{1}{T} \mathbb{E} \left[ \sum_{t=0}^{T} r_t \right]$$ |

Trong đó:
- $\tau$: quỹ đạo $(s_0, a_0, r_1, s_1, \dots)$
- $\gamma$: hệ số chiết khấu ($0 \leq \gamma < 1$) – ưu tiên phần thưởng trước mắt hơn tương lai xa.
- $r_t$: phần thưởng tại bước $t$.

### Mục tiêu

$$\max_{\theta} J(\theta)$$

Tức tìm bộ tham số $\theta$ giúp tác tử thu được **tổng phần thưởng kỳ vọng lớn nhất**.

### Ứng dụng

- **Tối ưu hóa chính sách** (Policy Optimization) như REINFORCE, PPO, TRPO đều giải bài toán này.
- Khác với học có giám sát (tối thiểu lỗi), ở đây **không có nhãn đúng/sai** – chỉ có phần thưởng phản hồi từ môi trường.

---

## Tổng kết

| Khái niệm | Ý nghĩa |
|-----------|---------|
| $\theta \leftarrow \theta + \alpha \nabla J(\theta)$ | Gradient Ascent – cập nhật tham số để tăng hàm mục tiêu |
| $\nabla \log \pi = \frac{\nabla \pi}{\pi}$ | Log-derivative trick – biến đổi giúp ước lượng gradient dễ dàng qua mẫu |
| $J(\theta)$ | Phần thưởng kỳ vọng – đại lượng cần tối đa hóa |

Hai mô phỏng GeoGebra là công cụ trực quan tốt để cảm nhận cách một điểm di chuyển lên đỉnh hàm (Gradient Ascent) và sự phụ thuộc của gradient vào tham số chính sách (Policy Gradient).
