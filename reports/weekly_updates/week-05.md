# Week 05 — Milestone 1 Wrap-up (Apr 20-26, 2026)

**Phase**: 1 — Foundation (W3-W5)
**Status**: 🔄 In Progress (Closing Milestone 1)

---

## Meeting (Apr 20, 21:18-22:00)

- **Format**: Online (Google Meet/YouTube Record)
- **Facilitator**: Thanh | **Scribe**: Thanh (Quỳnh nghỉ ốm)
- **Attendance**: 3/4 (Vắng: Quỳnh)

## Completed (Week 04 Review)

- [x] Đã chứng minh xong công thức toán cơ bản (Policy Gradient Theorem).
- [x] Sơn đã gửi file toán (LaTeX), chuẩn bị đẩy lên GitHub (`math/` folder).
- [x] Demo thành công code chạy thử bằng thư viện (BaseLine).
- [x] Môi trường Gymnasium hoạt động ổn định trên Linux/MacOS.

## Key Decisions

- **Milestone 1**: Chốt các phần setup và nghiên cứu nền tảng. Chuyển trọng tâm sang Core Logic từ Tuần 06.
- **Math Strategy**: Tập trung vào toán ứng dụng (Applied Math). Giải thích công thức thông qua ví dụ thực tế (CartPole-v1) để dễ hiểu, tránh sa đà vào lý thuyết thuần túy.
- **Code Strategy**: Giữ kiến trúc mạng Policy đơn giản (Simple MLP). Sử dụng môi trường `CartPole-v1` làm benchmark chính.
- **Quality Control**: Thanh sẽ liên hệ khảo sát tiêu chí đánh giá của giảng viên để điều chỉnh nội dung báo cáo đúng trọng tâm.
- **Holiday Plan**: Đẩy nhanh tiến độ hoàn thiện toán và báo cáo trước kỳ nghỉ lễ 30/4 - 1/5 để cả nhóm được nghỉ ngơi.

## Tickets Assigned

| Ticket       | Description                                      | PIC        | Support |
| :----------- | :----------------------------------------------- | :--------- | :------ |
| [MATH-04/05] | Hoàn thiện chứng minh Theorem & Objective Function | Sơn        | Ý       |
| [CODE-03]    | Test môi trường trên Windows & chuẩn bị Training | Ý          | Thanh   |
| [RPT-02]     | Hoàn thiện Chapter 1 & 2 (Intro & Foundation)    | Quỳnh      | Thanh   |
| [MGMT-01]    | Khảo sát tiêu chí đánh giá & Rà soát mục lục     | Thanh      | —       |

## In Progress

- [ ] Tài liệu hóa phần chứng minh toán (8 nguồn tài liệu tham khảo).
- [ ] Soạn thảo mục lục chi tiết gửi giảng viên duyệt trước phạm vi.
- [ ] Gắn phần toán vào khung báo cáo Chapter 2.

## Blockers

- **Math Complexity**: Phần chứng minh Log-derivative trick và Theorem tốn nhiều thời gian xử lý dữ liệu để đảm bảo tính dễ hiểu.
- **OS Compatibility**: Cần xác nhận sự ổn định của Gymnasium trên Windows (máy của Sơn).

## Next Meeting

Monday evening (Week 06) - Bắt đầu giai đoạn Implementation.
