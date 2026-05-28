# Lộ trình Dự án

Dưới đây là lịch trình làm việc và lộ trình phát triển chính cho CS115-Team05, bám sát theo kế hoạch song song hóa. Tính đến ngày 27/05/2026, code, báo cáo cuối và slide thuyết trình đã hoàn thành; phần còn lại là đóng gói nộp bài và dọn repository public.

## 🗺️ Lộ trình tổng thể (Biểu đồ Gantt)

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
    Nghỉ Giỗ Tổ & 30/4 - 1/5          :done, holiday, 2026-04-27, 7d

    section GĐ 2: Thuật toán
    Mạng Policy (Thanh/Sơn)           :done, des3, 2026-05-04, 14d
    Lập trình REINFORCE (Thanh/Sơn)   :done, des4, 2026-05-06, 15d

    section GĐ 3: Huấn luyện
    Huấn luyện & Tối ưu (Thanh/Sơn)   :done, des5, 2026-05-04, 7d
    Đánh giá & Biểu đồ (Thanh/Quỳnh)  :done, des6, 2026-05-04, 7d

    section GĐ 4: Báo cáo & Slide
    Soạn thảo Báo cáo (Quỳnh/Thanh)   :done, des7, 2026-04-13, 45d
    Slide thuyết trình (Quỳnh)        :done, des8, 2026-05-21, 7d

    section GĐ 5: Hoàn tất
    Đóng gói repo public (Nhóm)       :active, des9, 2026-05-28, 5d
    Nộp bài chính thức                :milestone, des10, 2026-07-01, 0d
```

---

## 📈 Theo dõi Tiến độ

> **Nguồn chính thống:** `reports/weekly_updates/week-0{3,4,5}.md` — chi tiết theo từng người tại `reports/detailed_reports/`. Quy tắc cập nhật thư mục báo cáo xem tại [`reports/README.md`](../reports/README.md).
>
> | Tuần | Giai đoạn   | Trạng thái                                                                |
> | :--- | :---------- | :------------------------------------------------------------------------ |
> | W03  | 06/04–12/04 | ✅ Hoàn thành — Khởi động, Charter, WBS                                   |
> | W04  | 13/04–19/04 | ✅ Hoàn thành — Bản nháp chứng minh PG, Mạng Policy, Logic REINFORCE      |
> | W05  | 20/04–26/04 | ✅ Hoàn thành — Đóng Milestone 1, code cốt lõi chạy được trên CartPole-v1 |
> | W06  | 27/04–03/05 | ✅ Hoàn thành — Nghỉ lễ theo kế hoạch, không giao thêm task nặng          |
> | W07  | 04/05–10/05 | ✅ Code đi trước tiến độ — CODE-05..08 hoàn thành, tiếp tục toán/báo cáo  |

## ✅ Mốc đã hoàn thành tính đến ngày 27/05/2026

| Nhóm việc             | Mốc                                                                 | Trạng thái             | Bằng chứng chính                                                                          |
| :-------------------- | :------------------------------------------------------------------ | :--------------------- | :---------------------------------------------------------------------------------------- |
| Nền tảng              | Setup Python, PyTorch, Gymnasium; random baseline                   | ✅ Hoàn thành          | `requirements.txt`, `sources/test_env.py`, `outputs/final/random-baseline/`               |
| Thuật toán            | Policy MLP và REINFORCE core                                        | ✅ Hoàn thành          | `sources/models/policy.py`, `sources/reinforce.py`, `sources/train.py`                    |
| Reproducibility       | Entrypoint train/evaluate, seed, hidden_dim, output logs            | ✅ Hoàn thành          | `scripts/train.py`, `scripts/evaluate.py`, `rewards.txt`, `run_config.txt`, `metrics.txt` |
| Hyperparameter tuning | Grid nhỏ, ranking theo mean last-50/std/best reward                 | ✅ Hoàn thành          | `scripts/run_experiments.py`, cấu hình chọn lọc trong `outputs/final/reinforce-cartpole-v1/` |
| Visualization         | Figure report-ready, baseline vs trained, HP comparison             | ✅ Hoàn thành          | `scripts/visualize.py`, figure chọn lọc trong `outputs/final/`                            |
| Logic explanation     | Tài liệu giải trình code, PR #40 coi như đã merge vào `origin/main` | ✅ Hoàn thành kỹ thuật | `docs/`, PR #40, issue #11                                                                |
| Báo cáo & slide       | Report cuối và slide thuyết trình                                  | ✅ Hoàn thành          | File cuối giữ riêng cho submission, không public link trong repo                          |

## 🔄 Trọng tâm còn lại

1. **Repository public-readiness**: cập nhật README/docs, dọn output policy, test smoke.
2. **Submission prep**: đóng gói file cuối và nộp theo deadline 01/07/2026.
3. **Post-submission archive**: giữ report/slide protected, không public link trong repo.

---

## 🏗️ Phân chia Công việc chi tiết (WBS - Phân rã Công việc)

| Phân hệ     | Nội dung                                             | Người phụ trách    | Hỗ trợ         |
| :---------- | :--------------------------------------------------- | :----------------- | :------------- |
| **Toán**    | Chứng minh PG, Thủ thuật log-đạo hàm, LaTeX          | Hoàng Cao Sơn      | Đặng Chí Thanh |
| **Code**    | Môi trường Gymnasium, Mạng policy PyTorch, REINFORCE | Đặng Chí Thanh     | Hoàng Cao Sơn  |
| **Báo cáo** | Cập nhật tuần, biên bản họp, viết báo cáo            | Phạm Vũ Xuân Quỳnh | Đặng Chí Thanh |

---

## 🚩 Các cột mốc chính

1. **M1: Nền tảng (W3-W5)** — Chứng minh định lý PG + thiết lập môi trường. ✅ Hoàn thành.
2. **M2: Thuật toán (W6-W8)** — Mạng nơ-ron + triển khai REINFORCE. ✅ Hoàn thành sớm.
3. **M3: Huấn luyện (W9-W11)** — Huấn luyện, tối ưu tham số, vẽ biểu đồ. ✅ Hoàn thành sớm phần code.
4. **M4: Báo cáo (W12-W13)** — Hoàn thiện báo cáo + slide thuyết trình. ✅ Hoàn thành.
5. **M5: Nộp bài (W14-W15)** — Đóng gói repo/file cuối + nộp chính thức. 🔄 Đang chuẩn bị.
