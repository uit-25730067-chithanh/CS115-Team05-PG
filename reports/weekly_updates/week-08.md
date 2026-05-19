# Tuần 08 — Chốt Toán, Báo cáo và hướng tới Slide/Demo (11/05 – 17/05/2026)

**Giai đoạn**: 4 — Báo cáo, slide và chuẩn bị demo
**Trạng thái**: 🔄 Report/Math còn carry-over sang Tuần 09

---

## Họp (Tuần 08)

- **Hình thức**: Online (Microsoft Teams)
- **Điều phối**: Thanh | **Ghi biên**: Quỳnh
- **Tham dự**: 4/4

## Nội dung chính (Họp Tuần 08)

1. **Chuyển trọng tâm từ Code sang Math + Report + Demo**
   - Phần Code đã hoàn thành từ tuần 07 nên tuần 08 tập trung vào các nhánh toán, báo cáo Word, slide và kế hoạch rehearsal.
   - Thanh nhắc team bám dependency chính: Chapter 2 / Math Foundations cần ổn định trước để Chapter 3/4 và slide đồng bộ theo đúng nền toán.

2. **Review và chốt các PR/tài liệu toán**
   - PR #42 của Ý tiếp tục được review, tập trung vào math deep-dive, visualization explanation, formatting và notation.
   - PR #46 của Sơn được tạo từ branch `feat/son-math-files` để bổ sung tài liệu nghiên cứu/chứng minh Policy Gradient Theorem và Chapter 2 Math Foundations.
   - PR #46 vẫn ở trạng thái Draft cuối tuần 08; team cần chốt xem các file toán sẽ merge vào main hay dùng làm tài liệu tham khảo.

3. **Tổng hợp báo cáo Word**
   - Quỳnh tổng hợp và hoàn thiện nội dung Chapter 2, Chapter 3, Chapter 4 và References.
   - Quỳnh tiếp tục review wording, format và công thức toán trong báo cáo.
   - PR #45 tiếp tục được duy trì như package hỗ trợ Chapter 3 và Chapter 4; Quỳnh đã dùng nội dung package này để fill vào report.
   - Thanh chưa review final Chapter 3/4 vì cần chờ Chapter 2 của Sơn ổn định hơn để tránh lệch nền toán.

4. **Định hướng slide và rehearsal**
   - Team thống nhất tuần 09 sẽ là tuần chốt toàn bộ deliverables: report Word, slide và rehearsal.
   - Về ngôn ngữ slide, team thảo luận hướng ưu tiên dễ hiểu khi thuyết trình bằng tiếng Việt nhưng vẫn giữ thuật ngữ chuyên ngành tiếng Anh khi cần; có thể dùng hướng song ngữ hoặc tài liệu tham khảo bổ sung nếu giúp người nghe dễ theo dõi hơn.
   - Lịch báo cáo chính xác của Team 05 được xác nhận là **26/05/2026**, nên tuần 09 cần hoàn tất slide, script, Q&A và rehearsal.

## Cập nhật và quyết định trong Tuần 08

- **Thanh (PM)**: Theo dõi các nhánh đang mở sau tuần 07: PR #42, PR #45, PR #46.
- **Thanh + Sơn + Ý**: Tiếp tục review phần toán để đảm bảo nội dung PR #42/#46 khớp với report Word.
- **Quỳnh (Report)**: Cập nhật MoM tuần 08 trên Google Drive, tổng hợp Chapter 2/3/4/References và bắt đầu chuyển nội dung sang slide.
- **Team**: Xác định tuần 09 là tuần chốt report, slide, Q&A và rehearsal trước ngày báo cáo 26/05/2026.

## Đã hoàn thành

- [x] **Thanh (PM/Code Lead)**: Theo dõi PR #42, PR #45, PR #46; nhắc team chuyển trọng tâm sang Math + Report + Demo.
- [x] **Thanh (Math/Report Support)**: Review trực tiếp với Ý cho PR #42 và góp ý với Sơn cho PR #46, đặc biệt phần Chapter 2 / math foundation.
- [x] **Thanh (Report Support)**: Duy trì PR #45 như package hỗ trợ Methods + Experiments; nội dung đã được Quỳnh dùng để fill vào report.
- [x] **Sơn (Math Lead)**: Bổ sung bộ tài liệu toán trong `math/`, gồm tài liệu chứng minh/nghiên cứu Policy Gradient Theorem và Chapter 2 Math Foundations bản tiếng Anh/tiếng Việt.
- [x] **Sơn (Math Lead)**: Tạo PR #46 `Docs: Add research documents on Policy Gradient Theorem` từ branch `feat/son-math-files`.
- [x] **Quỳnh (Report Lead)**: Cập nhật MoM tuần 08 trên Google Drive; tổng hợp và hoàn thiện nội dung Chapter 2, 3, 4 và References.
- [x] **Quỳnh (Report Lead)**: Review và chỉnh sửa báo cáo tổng thể về wording, format và công thức toán.
- [x] **Ý (Math Support)**: Báo cáo đã hoàn thành phần chứng minh toán; PR #42 vẫn là phần cần tiếp tục xử lý.

## Quyết định chính (Tuần 08)

- **Team**: Không mở thêm code task lớn; ưu tiên hoàn thiện toán, báo cáo, slide và rehearsal.
- **Team**: Chapter 2 / Math Foundations là dependency chính trước khi review final Chapter 3/4 và chuyển nội dung sang slide.
- **Team**: PR #42 và PR #46 cần được chốt cẩn thận để tránh lệch notation/công thức giữa tài liệu toán và report Word.
- **Team**: Slide sẽ thuyết trình bằng tiếng Việt, nhưng có thể giữ thuật ngữ tiếng Anh hoặc triển khai song ngữ khi cần để đảm bảo đúng chuyên ngành và dễ hiểu.
- **Team**: Ngày báo cáo chính xác của Team 05 là **26/05/2026**.

## Ticket được phân công

| Ticket   | Description                                   | PIC   | Support    |
| :------- | :-------------------------------------------- | :---- | :--------- |
| [PR #42] | Deep dive documentation for Policy Gradient   | Ý     | Sơn, Thanh |
| [PR #46] | Research documents on Policy Gradient Theorem | Sơn   | Thanh      |
| [PR #45] | Report support package for Chapter 3/4        | Thanh | Quỳnh      |
| [RPT-03] | Report Word Chapter 2/3/4/References          | Quỳnh | Sơn, Thanh |
| [RPT-04] | Slide thuyết trình                            | Quỳnh | Cả nhóm    |
| [FINAL]  | Demo package, rehearsal và Q&A                | Thanh | Cả nhóm    |

## Kết quả so với mục tiêu Tuần 08

- [x] **Thanh (PM)**: Gom detailed reports và chuẩn bị cơ sở soạn agenda tuần 09.
- [x] **Thanh + Sơn + Ý**: Review phần toán ở PR #42/#46, nhưng chưa chốt merge cuối vì cần đồng bộ với report Word.
- [x] **Quỳnh (Report)**: Tổng hợp Chapter 2, 3, 4 và References vào báo cáo.
- [x] **Sơn (Math)**: Tạo PR #46 và bổ sung tài liệu toán phục vụ Chapter 2.

## Việc chuyển sang Tuần 09

- **Team**: Chốt cuối PR #42 và PR #46.
- **Thanh**: Review final Chapter 3/4 sau khi Chapter 2 ổn định.
- **Quỳnh**: Chuyển nội dung chính sang slide và share cho team review.

## Trở ngại

- **Toán**: PR #42 vẫn cần chốt sau review; PR #46 còn Draft và cần quyết định merge hay dùng làm tài liệu tham khảo.
- **Báo cáo**: Chapter 3/4 đã có nội dung nhưng chưa nên final review khi Chapter 2 chưa ổn định.
- **Slide**: Slide đang trong giai đoạn chuyển nội dung từ report; cần thống nhất cách dùng tiếng Việt/tiếng Anh cho thuật ngữ chuyên ngành.
- **Timeline**: Team 05 báo cáo ngày 26/05/2026, nên tuần 09 phải chốt report, slide, Q&A và rehearsal.

## Trọng tâm Tuần 09

- **Tối thứ Hai**: Chốt báo cáo Word/PDF, outline slide, phân công phần nói, chuẩn bị Q&A và rehearsal trước ngày báo cáo 26/05/2026.
