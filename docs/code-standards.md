# Tiêu chuẩn Code (Code Standards)

Nhằm đảm bảo sự đồng bộ trong team, chúng ta thống nhất tuân thủ các quy tắc sau:

## 1. Git Workflow

- Nhánh `main`: Phải luôn sạch sẽ, chứa code có thể chạy được và báo cáo hoàn chỉnh. (Không push thẳng lên nhánh này).
- Thực hiện công việc: Tạo nhánh `feature/<tên-việc>`, ví dụ: `feature/setup-gymnasium`.
- Hợp nhất: Phải tạo Pull Request (PR) và cho các thành viên khác xem xét (Code Review) trước khi gộp vào `main`.

## 2. Tiêu chuẩn Mã nguồn (Python)

- Tuân thủ PEP 8 (khuyến nghị dùng `black`, `ruff format`, `autopep8` hoặc công cụ auto-format dành cho Python).
- Đặt tên biến, hàm **hoàn toàn bằng Tiếng Anh**, ví dụ: `compute_returns`, `policy_net` thay vì `tinh_phan_thuong`.
- Comment code: Giải thích **TẠI SAO (Why)** bạn làm như vậy, thay vì việc dòng code đó đang làm gì. (Ví dụ: `# Epsilon (1e-8) giúp tránh chia cho 0`).

## 3. Quản lý Tệp

- Mọi file sinh ra tạm thời, nháp cá nhân đặt ở thư mục `tmp/` (được gitignore).
- Các proof và derivation toán học phải lưu chuẩn LaTeX trong folder `math/`.

## 4. Chính sách AI và Quality Control

- **Charter v3.0**: Chúng ta chỉ dùng AI (Claude/ChatGPT) để nghiên cứu và lấy tài liệu tham khảo. **KHÔNG** copy-paste và uỷ thác 100% cho AI trong các assignment môn Toán.
- Owner của đoạn code / công thức Toán phải giải thích **đạt 100% logic** cho reviewer trước khi PR được duyệt.
