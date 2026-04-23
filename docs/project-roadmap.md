# Lộ trình Dự án (Project Roadmap)

Dưới đây là lịch trình làm việc và lộ trình phát triển chính cho CS115-Team05, bám sát theo kế hoạch song song hóa.

## 🗺️ Lộ trình tổng thể (Gantt Chart)

```mermaid
gantt
    title CS115 Lộ trình Dự án RL
    dateFormat  YYYY-MM-DD
    tickInterval 1w
    axisFormat  %m/%d

    section GĐ 1: Nền tảng
    Nghiên cứu & Toán (Sơn/Thanh)     :done, des1, 2026-04-06, 21d
    Cài đặt môi trường (Thanh)        :done, des2, 2026-04-06, 14d

    section 🗓️ Kỳ nghỉ lễ (Week 06)
    Nghỉ Giỗ Tổ & 30/4 - 1/5          :active, holiday, 2026-04-27, 7d

    section GĐ 2: Thuật toán
    Mạng Policy (Thanh/Sơn)           :des3, 2026-05-04, 14d
    Lập trình REINFORCE (Thanh/Sơn)   :des4, 2026-05-06, 15d

    section GĐ 3: Huấn luyện
    Huấn luyện & Tối ưu (Thanh/Sơn)   :des5, 2026-05-11, 21d
    Đánh giá & Biểu đồ (Thanh/Quỳnh)  :des6, 2026-05-11, 7d

    section GĐ 4: Báo cáo & Slide
    Soạn thảo Báo cáo (Quỳnh/Thanh)   :active, des7, 2026-04-13, 60d
    Slide thuyết trình (Quỳnh)        :des8, 2026-06-15, 10d

    section GĐ 5: Hoàn tất
    Hoàn thiện (Nhóm)                 :des9, 2026-06-25, 5d
    Nộp bài chính thức                :milestone, des10, 2026-07-01, 0d
```

---

## 📈 Theo dõi Tiến độ (Weekly Tracker)

### Tuần 03 (Khởi động) — 06/04/2026

- [x] Khởi tạo repo & Git setup.
- [x] Lập kế hoạch & WBS.
- [x] Hoàn tất Team Charter v3.0.
- [x] Tạo GitHub Project board.
- [x] Nghiên cứu: REINFORCE cho không gian hành động rời rạc.
- [x] Baseline: `CartPole-v1` với hành động ngẫu nhiên.

### Tuần 04 (Mở rộng nền tảng) — 13/04/2026

- [x] Bản nháp chứng minh PG theorem (LaTeX - Sơn đã soạn).
- [x] Push file LaTeX lên GitHub (`math/` folder) — _Đang chờ hoàn tất để merge_.
- [x] Giải thích Log-derivative trick.
- [x] Thiết kế Policy Network bằng PyTorch (Xong sớm).
- [x] Logic REINFORCE (Xong sớm).
- [x] Experience buffer cho trajectory (S, A, R).
- [🔄] Report: phần Introduction & Math Foundations — _Đang tổng hợp_.
- [x] Thống nhất quy trình: branch → PR → merge main.

### Tuần 05 (Hoàn thiện Core Logic & M1) — 20/04/2026

- **Trạng thái**: 🔄 Đang hoàn tất Milestone 1. Phần mã nguồn (Giai đoạn 2 & 3) đã hoàn thành sớm.
- [x] Triển khai thành công thuật toán REINFORCE (`sources/reinforce.py`).
- [x] Tích hợp Policy MLP (`sources/models/policy.py`).
- [x] Huấn luyện thành công trên `CartPole-v1` (Reward ~440+).
- [x] Xuất biểu đồ `training_curve.png` và tổ chức lại folder `outputs/`.
- [🔄] Hoàn thiện chứng minh Theorem & Objective Function (Sơn & Ý).
- [🔄] Soạn thảo mục lục chi tiết & Khảo sát tiêu chí đánh giá (Thanh).
- [🔄] Tổng hợp Chapter 1 & 2 vào báo cáo chính (Quỳnh).
- [x] Điều chỉnh Roadmap để né kỳ nghỉ lễ tuần 06.

---

## 🏗️ Phân chia Công việc chi tiết (WBS)

| Phân hệ     | Nội dung                                     | Người phụ trách | Hỗ trợ    |
| :---------- | :------------------------------------------- | :-------------- | :-------- |
| **Toán**    | Chứng minh PG, Log-derivative trick, LaTeX   | Hoàng Sơn       | Chí Thanh |
| **Code**    | Gymnasium env, PyTorch policy net, REINFORCE | Chí Thanh       | Hoàng Sơn |
| **Báo cáo** | Cập nhật tuần, biên bản họp, viết báo cáo    | Xuân Quỳnh      | Chí Thanh |

---

## 🚩 Các cột mốc chính (Milestones)

1. **M1: Nền tảng (W3-W5)** — Chứng minh PG theorem + setup môi trường.
2. **M2: Thuật toán (W6-W8)** — Mạng nơ-ron + implement REINFORCE.
3. **M3: Huấn luyện (W9-W11)** — Train, tối ưu tham số, vẽ biểu đồ (Cần song song với M2).
4. **M4: Báo cáo (W12-W13)** — Hoàn thiện report + slide thuyết trình.
5. **M5: Nộp bài (W14-W15)** — Chỉnh theo góp ý GV + nộp chính thức.
