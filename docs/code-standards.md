# Tiêu chuẩn Code (Code Standards)

Nhằm đảm bảo sự đồng bộ trong team, chúng ta thống nhất tuân thủ các quy tắc sau:

## 1. Git Workflow

- Nhánh `main`: Cần luôn sạch sẽ, chứa code có thể chạy được và báo cáo hoàn chỉnh. (Không push thẳng lên nhánh này).
- Thực hiện công việc: Tạo nhánh `feature/<tên-việc>`, ví dụ: `feature/setup-gymnasium`.
- Hợp nhất: Cần tạo Pull Request (PR) và cho **Code Lead (Chí Thanh)** hoặc các thành viên khác review trước khi gộp vào `main`.

## 2. Tiêu chuẩn Mã nguồn & Ngôn ngữ (Python)

- **Đặt tên (Naming):** Biến, hàm, lớp **bắt buộc 100% bằng Tiếng Anh** (ví dụ: `compute_loss`, `policy_net`).
- **Chú thích (Comments):**
  - **Tiếng Anh (Ưu tiên):** Dùng cho các chú thích ngắn gọn (What/How), ví dụ: `# Initialize weights`.
  - **Tiếng Việt (Linh hoạt):** Được phép dùng để giải thích các **logic toán học phức tạp hoặc lý do (Why)** đằng sau các công thức (đối chiếu từ folder `math/`) để đảm bảo các thành viên trong team đều hiểu đúng bản chất toán học.
- **Định dạng:** Tuân thủ PEP 8 (khuyến nghị dùng `black`, `ruff format` hoặc các công cụ auto-format).

## 3. Quản lý Tệp

- Mọi file sinh ra tạm thời, nháp cá nhân đặt ở thư mục `tmp/` (được gitignore).
- Các proof và derivation toán học cần được lưu chuẩn LaTeX trong folder `math/`.
- Các báo cáo hàng tuần cần được lưu trong folder `reports/`.

## 4. Chính sách AI và Quality Control

- **Charter v3.0**: Chúng ta chỉ dùng AI (Claude/ChatGPT) để nghiên cứu và lấy tài liệu tham khảo. **KHÔNG** copy-paste và uỷ thác 100% cho AI trong các assignment môn Toán.
- Owner của đoạn code / công thức Toán cần giải thích **đạt 100% logic** cho reviewer trước khi PR được duyệt.

## 5. Tiêu chuẩn Ký hiệu Toán học (LaTeX Standards)

Để đảm bảo các công thức toán học được hiển thị chính xác và đồng nhất trên GitHub (tránh lỗi font hoặc không render được), toàn team cần tuân thủ:

### 5.1. Ký hiệu thống nhất cho Policy Gradient

- **Quy tắc:** Ký hiệu toán trong code comments, README, docs và slide phải khớp `docs/math-notation-word-equations.md`.
- **Sai:** `\pi_\theta(a|s)`, `\ln \pi(A_t|S_t)`, `R_t`, `R_k`.
- **Đúng:** `\pi_\theta(a_t \mid s_t)`, `\log \pi_\theta(a_t \mid s_t)`, `r_{t+1}`, `G_t`.
- _Lưu ý:_ Giữ $\theta$ cho policy parameters; góc nghiêng CartPole dùng $\phi$ (`state[2]`).

### 5.2. Định dạng Khối công thức (Block Math)

- **Quy tắc:** Các khối công thức dùng cặp ký hiệu `$$` phải được đặt trên dòng riêng và **bắt buộc có dòng trống** bao quanh.
- **Ví dụ:**

  ```markdown
  Đây là văn bản mô tả.

  $$
  J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta}[R(\tau)]
  $$

  Đây là văn bản tiếp theo.
  ```

### 5.3. Sử dụng ký hiệu chuẩn

- **Quy tắc:** Không dùng ký tự Unicode toán học (như `θ`, `∇`, `π`) trực tiếp trong file Markdown. Luôn sử dụng lệnh LaTeX tương ứng.
- **Lệnh phổ biến:**
  - `\theta`: Tham số chính sách.
  - `\phi`: Góc nghiêng của cột CartPole.
  - `\nabla_\theta`: Gradient theo theta.
  - `\pi_\theta(a_t \mid s_t)`: Chính sách (Policy). Trong Markdown Table phải dùng `\mid` thay vì `|` để tránh vỡ bảng.
  - `G_t`: Reward-to-go.
  - `r_{t+1}`: Immediate reward nhận sau transition từ time step `t`.
  - `\tau`: Quỹ đạo (Trajectory).
  - `\mathbb{E}`: Kỳ vọng (Expectation).

### 5.4. Đồng bộ Math-to-Code

- Khi đặt tên biến hoặc comment trong code, hãy cố gắng giữ sự tương quan với ký hiệu toán học:
  - `learning_rate` hoặc `lr` tương ứng với $\alpha$.
  - `gamma` tương ứng với $\gamma$.
  - `state` tương ứng với $s_t$; `next_state` tương ứng với $s_{t+1}$.
  - `reward` tương ứng với $r_{t+1}$.
  - `log_probs` tương ứng với $\log \pi_\theta(a_t \mid s_t)$.
  - `returns` tương ứng với $G_t$.

### 5.5. Các lỗi render thường gặp trên GitHub Markdown

Những quy tắc sau giúp tránh các lỗi render công thức toán học trên GitHub (và hầu hết các parser Markdown hiện đại):

- **Inline math:** Luôn dùng `$...$`. **KHÔNG** dùng `\( ... \)` — GitHub không render cú pháp này.
  - Sai: `\( J(\theta) \)`
  - Đúng: `$J(\theta)$`

- **Không escaped underscores:** Trong LaTeX, dấu `_` không cần escape. Việc thêm `\` trước `_` sẽ khiến GitHub hiển thị sai.
  - Sai: `\pi\_\theta`, `G\_t`
  - Đúng: `\pi_\theta`, `G_t`

- **Không dùng `*` thay cho `_` trong chỉ số dưới:** LaTeX chỉ nhận `_` cho subscript.
  - Sai: `\nabla*{\theta}`, `\pi*{\theta}`
  - Đúng: `\nabla_\theta`, `\pi_\theta`

- **Block math `$$...$$` phải đứng một mình trên dòng riêng:** Không để chung dòng với text khác.
  - Sai: `Đây là công thức $$J(\theta)$$ trong văn bản.`
  - Đúng:

    ```markdown
    Đây là công thức.

    $$
    J(\theta) = \dots
    $$

    Văn bản tiếp theo.
    ```

_Còn nhiều tiêu chuẩn khác sẽ bổ sung sau_
