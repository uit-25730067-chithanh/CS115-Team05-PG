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

### 5.1. Nhóm chỉ số dưới (Subscript Grouping) - BẮT BUỘC

- **Quy tắc:** Luôn sử dụng ngoặc nhọn `{}` cho tất cả các chỉ số dưới, ngay cả khi chỉ có một ký tự hoặc là ký tự Hy Lạp.
- **Sai:** `\pi_\theta`, `\nabla_\theta`, `G_t`, `r_t`.
- **Đúng:** `\pi_{\theta}`, `\nabla_{\theta}`, `G_{t}`, `r_{t}`.
- _Lưu ý:_ Việc thiếu `{}` là nguyên nhân hàng đầu khiến GitHub không render được các ký tự như $\theta$ trong chỉ số dưới.

### 5.2. Định dạng Khối công thức (Block Math)

- **Quy tắc:** Các khối công thức dùng cặp ký hiệu `$$` phải được đặt trên dòng riêng và **bắt buộc có dòng trống** bao quanh.
- **Ví dụ:**

  ```markdown
  Đây là văn bản mô tả.

  $$
  J(\theta) = \mathbb{E}_{\tau \sim \pi_{\theta}} [R(\tau)]
  $$

  Đây là văn bản tiếp theo.
  ```

### 5.3. Sử dụng ký hiệu chuẩn

- **Quy tắc:** Không dùng ký tự Unicode toán học (như `θ`, `∇`, `π`) trực tiếp trong file Markdown. Luôn sử dụng lệnh LaTeX tương ứng.
- **Lệnh phổ biến:**
  - `\theta`: Tham số chính sách.
  - `\nabla_{\theta}`: Gradient theo theta.
  - `\pi_{\theta}(a|s)`: Chính sách (Policy).
  - `\tau`: Quỹ đạo (Trajectory).
  - `\mathbb{E}`: Kỳ vọng (Expectation).

### 5.4. Đồng bộ Math-to-Code

- Khi đặt tên biến hoặc comment trong code, hãy cố gắng giữ sự tương quan với ký hiệu toán học:
  - `learning_rate` hoặc `lr` tương ứng với $\alpha$.
  - `gamma` tương ứng với $\gamma$.
  - `log_probs` tương ứng với $\ln \pi_{\theta}(a|s)$.

_Còn nhiều tiêu chuẩn khác sẽ bổ sung sau_
