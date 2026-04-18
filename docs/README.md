# /docs README

Chào mừng các bạn Team 05 và các AI Agents! Dự án này sử dụng hệ thống tài liệu phân tầng để mọi người và AI đều dễ dàng nắm bắt.

## 📌 Mục lục Tài liệu

| Tệp tin                                                  | Đối tượng       | Nội dung chính                                                                       |
| :------------------------------------------------------- | :-------------- | :----------------------------------------------------------------------------------- |
| **[installation.md](./installation.md)**                 | Cả hai          | Cách setup môi trường, sửa lỗi `ModuleNotFoundError` và chạy code.                   |
| **[codebase-summary.md](./codebase-summary.md)**         | AI Agents       | Bản đồ các file sources, giúp Agent biết nên sửa code ở đâu mà không làm hỏng logic. |
| **[code-standards.md](./code-standards.md)**             | Cả hai          | Quy tắc đặt tên (Tiếng Anh), Git Flow, và giới hạn Copy-paste từ AI (Charter v3.0).  |
| **[system-architecture.md](./system-architecture.md)**   | Cả hai          | Chip Mac (MPS) vs CPU, kiến trúc mạng Neural (128 units), REINFORCE logic.           |
| **[project-roadmap.md](./project-roadmap.md)**           | Team members    | Lịch trình "Song song hóa" và WBS chi tiết.                                          |
| **[project-overview-pdr.md](./project-overview-pdr.md)** | Giảng viên/Team | Tổng quan yêu cầu dự án (PDR) và mục tiêu môn học.                                   |

---

## 🤖 Ghi chú cho AI Agents

- **Luôn đọc `CLAUDE.md`** để biết các lệnh chạy chính.
- **Hãy đọc [`installation.md`](./installation.md) và [`codebase-summary.md`](./codebase-summary.md)** để biết cách chạy dự án và xác định đúng khu vực cần sửa.
- **Tuân thủ `Installation Guide`** trước khi báo lỗi thiếu thư viện.
- **Không bao giờ sửa logic Toán** trong `sources/reinforce.py` nếu không khớp với các công thức trong `math/`.
