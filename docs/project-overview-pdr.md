# Hồ sơ Dự án (Lưu trữ PDR)

Tài liệu này lưu trữ các quyết định thiết kế ban đầu và biên bản họp lịch sử. Nội dung động (Nhân sự, Lộ trình) vui lòng xem tại các file tương ứng.

## 🔗 Liên kết nhanh

- **Nhân sự hiện tại**: [README.md](../README.md#-team-05)
- **Lộ trình thực tế**: [docs/project-roadmap.md](./project-roadmap.md)

---

## 1. Mục tiêu Dự án

Dự án tập trung vào việc áp dụng Lý thuyết xác suất và Đạo hàm (Toán học) để giải quyết bài toán Học tăng cường (RL).

- Chứng minh Định lý Policy Gradient.
- Triển khai thuật toán REINFORCE trên môi trường CartPole-v1.

## 2. Các quyết định

| Ngày       | Quyết định                                                                                        | Bối cảnh                                                               |
| :--------- | :------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------- |
| 06/04/2026 | Ký Charter v3.0, phân chia WBS (Toán/Code/Báo cáo), chọn PyTorch 2.0.                             | Họp khởi động. Xem `reports/weekly_updates/week-03.md`.                |
| 13/04/2026 | Thanh đảm nhận Code Lead; Quỳnh đảm nhận Admin/Báo cáo.                                           | Đẩy nhanh tiến độ kỹ thuật. Xem `reports/weekly_updates/week-04.md`.   |
| 20/04/2026 | Chiến lược Toán: Tập trung Toán ứng dụng; Kế hoạch nghỉ lễ 30/4-1/5; Đóng Cột mốc 1.              | Hoàn thành logic cốt lõi sớm. Xem `reports/weekly_updates/week-05.md`. |
| 04/05/2026 | Sau kỳ nghỉ, ưu tiên làm trước toàn bộ nhánh Code để giải phóng thời gian cho toán, report, demo. | CODE-06/07/08 được triển khai theo từng branch/PR nhỏ.                 |
| 09/05/2026 | Xem PR #40 là đã merge vào `origin/main`; CODE-05..08 được xem là hoàn thành về mặt kỹ thuật.     | Tham chiếu tiến độ: GitHub issues #26, #11, #12, #17, #21 và PR #40.   |

## 3. Trạng thái hiện tại

Tính đến ngày 27/05/2026, dự án đã hoàn thành phần code, báo cáo và slide. Phần còn lại là đóng gói nộp bài và dọn repository trước khi public.

| Mảng         | Trạng thái                   | Ghi chú                                                                               |
| :----------- | :--------------------------- | :------------------------------------------------------------------------------------ |
| Toán         | ✅ Hoàn thành                | Chứng minh Policy Gradient đã được đưa vào report cuối.                               |
| Code         | ✅ Hoàn thành                | Policy, REINFORCE, train/evaluate CLI, tuning, visualization, logic explanation.      |
| Báo cáo      | ✅ Hoàn thành                | Report cuối được giữ riêng cho submission, không public link trong repo.              |
| Demo cuối kỳ | ✅ Hoàn thành                | Slide và demo assets được giữ riêng cho submission/presentation package.              |

> **Nhật ký hội họp đầy đủ:** `reports/weekly_updates/` (chính thống). Chi tiết theo từng người: `reports/detailed_reports/`.
