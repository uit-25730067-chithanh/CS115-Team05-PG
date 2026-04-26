# Tuần 05 — Đóng Milestone 1 (20/04 – 26/04/2026)

**Giai đoạn**: 1 — Nền tảng (W3–W5)
**Trạng thái**: ✅ Hoàn thành (27/04/2026)

---

## Họp (20/04, 21:18–22:00)

- **Hình thức**: Online (Google Meet/YouTube Record)
- **Điều phối**: Thanh | **Ghi biên**: Thanh (Quỳnh nghỉ ốm)
- **Tham dự**: 3/4 (Vắng: Quỳnh)

## Thay đổi & Quyết định bổ sung (giữa tuần)

Không có.

## Đã hoàn thành

- [x] **Thanh (Code Lead)**: Triển khai thành công thuật toán REINFORCE (`sources/reinforce.py`).
- [x] **Thanh (Code Lead)**: Tích hợp Policy MLP (`sources/models/policy.py`).
- [x] **Thanh (Code Lead)**: Huấn luyện thành công trên `CartPole-v1` (Reward ~440+).
- [x] **Thanh (Code Lead)**: Xuất biểu đồ `training_curve.png` & tổ chức lại folder `outputs/`.

## Quyết định chính (Họp Tuần 05)

- **Cả nhóm**: Chốt Milestone 1. Chuyển trọng tâm sang Core Logic từ Tuần 06.
- **Sơn (Math)**: Math Strategy — tập trung toán ứng dụng (Applied Math), giải thích qua ví dụ CartPole-v1.
- **Thanh (Code Lead)**: Code Strategy — giữ kiến trúc Policy MLP đơn giản, dùng `CartPole-v1` làm benchmark.
- **Thanh (PM)**: Quality Control — liên hệ GV khảo sát tiêu chí đánh giá, điều chỉnh nội dung báo cáo.
- **Cả nhóm**: Holiday Plan — đẩy nhanh toán & báo cáo trước nghỉ lễ 30/4–1/5.

## Ticket được phân công

| Ticket       | Description                                        | PIC   | Support |
| :----------- | :------------------------------------------------- | :---- | :------ |
| [MATH-04/05] | Hoàn thiện chứng minh Theorem & Objective Function | Sơn   | Ý       |
| [CODE-03]    | Test môi trường trên Windows & chuẩn bị Training   | Ý     | Thanh   |
| [RPT-02]     | Hoàn thiện Chapter 1 & 2 (Intro & Foundation)      | Quỳnh | Thanh   |
| [MGMT-01]    | Khảo sát tiêu chí đánh giá & Rà soát mục lục       | Thanh | —       |

## Việc cần làm (Hạn: Chủ nhật 26/04, 23:00)

- [🔄] **Sơn (Math)**: Tài liệu hóa phần chứng minh toán (8 nguồn tài liệu tham khảo).
- [🔄] **Thanh (PM)**: Soạn thảo mục lục chi tiết gửi giảng viên duyệt trước phạm vi.
- [x] **Quỳnh (Report)**: Gắn phần toán vào khung báo cáo Chapter 2.
- [🔄] **Ý (Code/Support)**: Kiểm thử môi trường Windows (Gymnasium + PyTorch), chờ phản hồi từ máy Sơn.

## Trở ngại

- **Sơn (Math)**: Math Complexity — chứng minh Log-derivative trick & Theorem tốn thời gian để đảm bảo dễ hiểu. Cần bổ sung ví dụ trực quan.
- **Ý (Code/Support)**: OS Compatibility — chưa xác nhận Gymnasium ổn định trên Windows (máy Sơn). Đang kiểm thử.
- **Cả nhóm**: Nghỉ lễ 30/4–1/5 — task kỹ thuật nặng tạm dừng, ưu tiên nghỉ ngơi.

## Họp tiếp theo

- **Tuần 06**: Nghỉ lễ 30/4–1/5, không họp chính thức.
- **Tuần 07**: Tối thứ Hai — Bắt đầu giai đoạn Implementation (tuning hyperparameters, viết proof toán, chuẩn bị slides).
