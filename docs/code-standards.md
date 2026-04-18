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
