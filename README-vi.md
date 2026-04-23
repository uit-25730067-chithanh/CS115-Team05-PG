# [CS115] Policy Gradient cho Học tăng cường (RL) - Nhóm 05

[![GitHub Projects](https://img.shields.io/badge/Dự_án-Theo_dõi-blue?logo=github)](https://github.com/users/uit-25730067-chithanh/projects/1)
![Python](https://img.shields.io/badge/Python-3.9+-yellow?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red?logo=pytorch)
![Gymnasium](https://img.shields.io/badge/Gymnasium-RL-green)

Nghiên cứu cơ sở toán học và triển khai thực tế thuật toán **Policy Gradient** (thuật toán REINFORCE) trên các bài toán điều khiển cổ điển sử dụng thư viện `Gymnasium`.

> Môn học: _CS115 - Toán cho Khoa học máy tính_ | Trường Đại học Công nghệ Thông tin (UIT)

---

## 👥 Nhóm 05

| MSSV     | Họ và Tên          | Vai trò chính           | Hỗ trợ              | GitHub                                                             |
| :------- | :----------------- | :---------------------- | :------------------ | :----------------------------------------------------------------- |
| 25730067 | Đặng Chí Thanh     | Trưởng nhóm & Code Lead | Tất cả              | [@uit-25730067-chithanh](https://github.com/uit-25730067-chithanh) |
| 25730061 | Hoàng Cao Sơn      | Math Lead               | Code & Báo cáo      | [@uit-25730061-caoson](https://github.com/uit-25730061-caoson)     |
| 26210070 | Phạm Vũ Xuân Quỳnh | Report Lead             | Admin & Hỗ trợ Code | [@xuanquynhphamvu](https://github.com/xuanquynhphamvu)             |
| 25730094 | Nguyễn Đức Ý       | Supporter               | Tổng hợp            | [@ducy11](https://github.com/ducy11)                               |

---

## 🗺️ Lộ trình & Tiến độ

Dự án đang trong giai đoạn triển khai song song Toán học & Mã nguồn (Tuần 04).

| Giai đoạn   | Nội dung chính              | Trạng thái              |
| :---------- | :-------------------------- | :---------------------- |
| **Phase 1** | Chứng minh Toán & Thiết lập | Đang thực hiện          |
| **Phase 2** | Policy Net & REINFORCE      | Hoàn thành (Tinh chỉnh) |
| **Phase 3** | Huấn luyện & Tối ưu         | Sắp tới                 |

🚀 Xem lộ trình chi tiết và biểu đồ Gantt tại: **[docs/project-roadmap.md](./docs/project-roadmap.md)**

---

## 🦴 4 Cột trụ Cốt lõi

### 1. Toán học (Math Core)

- **Hàm mục tiêu** $J(\theta)$: Giá trị phần thưởng kỳ vọng.
- **Thủ thuật Đạo hàm Log (Log-derivative Trick)**: Biến đổi gradient sang dạng có thể tính toán được.
- **Gradient Ascent**: Tối đa hóa xác suất của các hành động mang lại phần thưởng cao.

### 2. Môi trường (Gymnasium)

- **Bài toán**: `CartPole-v1` (Cân bằng thanh gỗ trên xe đẩy).
- **Vòng lặp**: Trạng thái (State) → Hành động (Action) → Phần thưởng (Reward).

### 3. Mạng Chính sách (Policy Network - PyTorch)

- **Kiến trúc**: Mạng nơ-ron sâu đơn giản (Simple DNN).
- **Đầu vào**: Trạng thái môi trường → **Đầu ra**: Phân phối xác suất hành động.

### 4. Huấn luyện & Phân tích

- Thu thập quỹ đạo (trajectory) dựa trên từng tập (episode).
- Lan truyền ngược (Backprop) với hàm mất mát trọng số phần thưởng (reward-weighted loss).
- Trực quan hóa đường cong học tập (Learning curve).

---

## 🚀 Sử dụng

Để biết hướng dẫn chi tiết về cách thiết lập môi trường và huấn luyện thuật toán REINFORCE, vui lòng tham khảo:

👉 **[Hướng dẫn Cài đặt & Sử dụng](./docs/installation.md)**

---

## 📐 Định lý Policy Gradient

Tối ưu hóa phần thưởng kỳ vọng $J(\theta)$ bằng cách điều chỉnh các tham số $\theta$ của chính sách ngẫu nhiên (stochastic policy) $\pi_{\theta}(a|s)$.

$$
\nabla_{\theta} J(\theta) = \mathbb{E}_{\pi_{\theta}} \left[ \sum_{t=0}^{T} \nabla_{\theta} \log \pi_{\theta}(a_t|s_t) \hat{A}_t \right]
$$

- $\pi_{\theta}(a_t|s_t)$: Xác suất của hành động $a_t$ trong trạng thái $s_t$.
- $\hat{A}_t$: Ước lượng lợi thế (Advantage) hoặc lợi nhuận tích lũy $G_t$.
- **Thủ thuật Đạo hàm Log**: $\nabla_{\theta} \pi_{\theta}(a|s) = \pi_{\theta}(a|s) \nabla_{\theta} \log \pi_{\theta}(a|s)$.

---

## 🛠 Phân chia Công việc (WBS Summary)

| Module       | Phụ trách (Owner)  | Hỗ trợ        |
| :----------- | :----------------- | :------------ |
| **Toán học** | Hoàng Cao Sơn      | Chí Thanh     |
| **Mã nguồn** | Đặng Chí Thanh     | Hoàng Cao Sơn |
| **Báo cáo**  | Phạm Vũ Xuân Quỳnh | Chí Thanh     |

---

## 🤝 Điều lệ Nhóm (Team Charter v3.0 Summary)

- **Giao tiếp**: MS Teams (chính) | Zalo (chỉ việc khẩn cấp).
- **SLA**: Phản hồi trong 12-24h. Giờ nghỉ: 23h-07h & 18h30-21h.
- **Hạn chót tuần**: 23:00 Chủ Nhật hàng tuần.
- **Chính sách AI**: Chỉ dùng để tham khảo, không copy-paste. Tự diễn đạt lại bằng ngôn ngữ của mình.
- **Chất lượng**: "Giải thích Logic" — người thực hiện phải giải thích logic cho người kiểm duyệt.
- **Xung đột**: Đối thoại trực tiếp → Họp 15 phút → Trưởng nhóm quyết định.
- **Mục tiêu**: Điểm A+ (9.0-10.0). Học thật, không đi đường tắt.

---

## 📤 Nộp bài (Học kỳ)

### Đồ án cuối kỳ (Hạn chót: 01/07/2026)

- **Mở:** Thứ Bảy, 30/05/2026 (12:00 AM)
- **Hạn chót:** Thứ Tư, 01/07/2026 (11:59 PM)
- **Thành phần:** Slides, demo/kết quả, mã nguồn & dữ liệu, báo cáo (tùy chọn), video (nếu không thuyết trình trực tiếp).
- **Định dạng:** Một tệp `.zip` → `MSSV_Nhom.zip`. Nếu >100MB, nộp tệp `.txt` chứa link Google Drive công khai.

---

© 2026 CS115 - Trường Đại học Công nghệ Thông tin (UIT)
