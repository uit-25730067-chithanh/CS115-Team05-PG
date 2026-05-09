# Reports Directory Guide

Thư mục `reports/` lưu các tài liệu vận hành theo tuần của Team 05. Đây là khu vực có quy tắc cập nhật theo thời điểm và theo vai trò, không phải nơi để AI agents tự tạo báo cáo thay thành viên.

## Cấu trúc thư mục

| Thư mục | Người tạo nội dung gốc | Thời điểm cập nhật | Quy tắc |
| :------ | :--------------------- | :----------------- | :------ |
| [`detailed_reports/`](./detailed_reports/) | Các member | Cuối tuần, trước 23:00 Chủ nhật | Member tự báo cáo; Thanh copy tay vào repo. AI agents không tự tạo file trong thư mục này. |
| [`meeting_agendas/`](./meeting_agendas/) | Thanh | Trước buổi họp tối thứ Hai | Lưu agenda/khung họp do Thanh chuẩn bị trước cuộc họp. |
| [`meeting_minutes/`](./meeting_minutes/) | Quỳnh | Sau buổi họp | Lưu biên bản họp do Quỳnh ghi với vai trò thư ký; Thanh chỉ copy về repo làm tài liệu. |
| [`weekly_updates/`](./weekly_updates/) | Thanh | Sáng thứ Hai | Thanh tổng kết thực tế tuần trước đã làm đến đâu. Chỉ cập nhật trong khung giờ này hoặc khi Thanh yêu cầu rõ. |

## Quy tắc cho AI agents

- Không tự tạo `weekly_updates/week-XX.md` ngoài khung tổng kết sáng thứ Hai nếu không có yêu cầu rõ.
- Không tự tạo hoặc giả lập báo cáo thành viên trong `detailed_reports/`.
- Không tự viết thay biên bản họp trong `meeting_minutes/`.
- Nếu cần cập nhật tiến độ ngoài lịch báo cáo, ưu tiên sửa các tài liệu tổng quan trong `docs/`, ví dụ `docs/project-roadmap.md` hoặc `docs/project-overview-pdr.md`.
- Nếu phát hiện thiếu dữ liệu người thật, ghi là `Pending human confirmation` thay vì tự suy đoán.
