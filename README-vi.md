# [CS115] Policy Gradient for Reinforcement Learning (RL) - Nhóm 05

[![GitHub Projects](https://img.shields.io/badge/Project-Tracking-blue?logo=github)](https://github.com/users/uit-25730067-chithanh/projects/1)
![Python](https://img.shields.io/badge/Python-3.9+-yellow?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red?logo=pytorch)
![Gymnasium](https://img.shields.io/badge/Gymnasium-RL-green)

Khám phá nền tảng toán học và triển khai thực tế **Policy Gradient** (thuật toán REINFORCE) trên các bài toán điều khiển kinh điển từ `Gymnasium`.

> Môn: _CS115 - Toán cho Khoa học máy tính_ | Trường ĐH Công nghệ Thông tin (UIT)

---

## 👥 Nhóm 05

| MSSV     | Họ Tên             | Vai Trò                 | Hỗ Trợ              | GitHub                                                             |
| :------- | :----------------- | :---------------------- | :------------------ | :----------------------------------------------------------------- |
| 25730067 | Đặng Chí Thanh     | Team Leader & Code Lead | Tất cả              | [@uit-25730067-chithanh](https://github.com/uit-25730067-chithanh) |
| 25730061 | Hoàng Cao Sơn      | Math Lead               | Code & Báo cáo      | [@uit-25730061-caoson](https://github.com/uit-25730061-caoson)     |
| 26210070 | Phạm Vũ Xuân Quỳnh | Report Lead             | Admin & Hỗ trợ Code | [@xuanquynhphamvu](https://github.com/xuanquynhphamvu)             |
| 25730094 | Nguyễn Đức Ý       | Supporter               | General (Chung)     | [@ducy11](https://github.com/ducy11)                               |

---

## 🗺️ Lộ trình & Tiến độ

Dự án đang triển khai song song Math & Code.

| Giai đoạn | Nội dung chính                       | Trạng thái     |
| :-------- | :----------------------------------- | :------------- |
| **GĐ 1**  | Chứng minh toán & Cài đặt môi trường | Đang thực hiện |
| **GĐ 2**  | Mạng Policy & REINFORCE              | Xong sớm       |
| **GĐ 3**  | Huấn luyện & Tối ưu                  | Sắp tới        |

🚀 Xem lộ trình chi tiết và biểu đồ Gantt tại: **[docs/project-roadmap.md](./docs/project-roadmap.md)**

---

## 🦴 4 Trụ cột Kỹ thuật

### 1. Toán học

- **Hàm mục tiêu** $J(\theta)$: Phần thưởng kỳ vọng.
- **Log-derivative Trick**: Biến đổi để tính được đạo hàm.
- **Gradient Ascent**: Cực đại hóa xác suất hành động có phần thưởng cao.

### 2. Môi trường (Gymnasium)

- **Bài toán**: `CartPole-v1` (giữ thăng bằng gậy).
- **Vòng lặp**: State → Action → Reward.

### 3. Policy Network (PyTorch)

- **Kiến trúc**: DNN đơn giản.
- **Đầu vào**: Trạng thái → **Đầu ra**: Phân phối xác suất hành động.

### 4. Huấn luyện & Phân tích

- Thu thập trajectory theo episode.
- Lan truyền ngược với loss có trọng số phần thưởng.
- Trực quan hóa đường cong học tập.

---

## 📐 Định lý Policy Gradient

Tối ưu phần thưởng kỳ vọng $J(\theta)$ bằng cách điều chỉnh $\theta$ của policy $\pi_{\theta}(a|s)$.

$$ \nabla_{\theta} J(\theta) = \mathbb{E}_{\pi_{\theta}} \left[ \sum_{t=0}^{T} \nabla_{\theta} \log \pi_{\theta}(a_t|s_t) \hat{A}_t \right] $$

- $\pi_{\theta}(a_t|s_t)$: Xác suất hành động $a_t$ ở trạng thái $s_t$.
- $\hat{A}_t$: Ước lượng Advantage hoặc Return $G_t$.
- **Log-derivative Trick**: $\nabla_{\theta} \pi_{\theta}(a|s) = \pi_{\theta}(a|s) \nabla_{\theta} \log \pi_{\theta}(a|s)$.

---

## 🛠 Phân chia Công việc (WBS Summary)

| Phân hệ      | Người phụ trách | Hỗ trợ    |
| :----------- | :-------------- | :-------- |
| **Toán học** | Hoàng Sơn       | Chí Thanh |
| **Mã nguồn** | Chí Thanh       | Hoàng Sơn |
| **Báo cáo**  | Xuân Quỳnh      | Chí Thanh |

---

---

## 🤝 Cam kết Nhóm (Charter v3.0)

- **Kênh liên lạc**: MS Teams (chính) | Zalo (khẩn cấp).
- **SLA**: 12-24h phản hồi. Quiet hours: 23h-07h & 18h30-21h.
- **Deadline Sprint**: 23:00 Chủ nhật hàng tuần.
- **AI**: Chỉ tham khảo, không copy-paste. Viết lại theo ý hiểu.
- **Chất lượng**: Cơ chế "Giải trình Logic" — owner phải giải thích cho reviewer.
- **Xung đột**: Nói thẳng → họp 15 phút → Leader quyết.
- **Mục tiêu**: A+ (9.0-10.0). Học thật, không đi tắt.

---

## 📤 Quy định Nộp bài

### Đồ án cuối kì (Deadline: 1/7/2026)

- **Mở nộp**: T7, 30/05/2026 (00:00)
- **Hết hạn**: T4, 01/07/2026 (23:59)
- **Thành phần**: Slides, demo/kết quả, source code & data, report (tùy chọn), video (nếu chưa báo cáo trực tiếp).
- **Format**: 1 file `.zip` → `ID_group.zip`. Nếu >100MB, nộp `.txt` chứa link GDrive (public).

---

© 2026 CS115 - Trường Đại học Công nghệ Thông tin (UIT)
