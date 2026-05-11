# Tuần 07 — Đóng nhánh Code & chuyển sang Toán/Báo cáo (04/05 – 10/05/2026)

**Giai đoạn**: 2 — Triển khai Core (W7)
**Trạng thái**: ✅ Hoàn thành phần Code (10/05/2026)

---

## Họp (04/05, 21:14–21:44)

- **Hình thức**: Online (Microsoft Teams)
- **Điều phối**: Thanh | **Ghi biên**: Quỳnh
- **Tham dự**: 4/4

## Nội dung chính (Họp Tuần 07)

1. **Khởi động lại sau kỳ nghỉ lễ (Tuần 6)**
   - Tuần 6 cả nhóm tạm dừng để nghỉ lễ 30/4 trọn vẹn (không trao đổi công việc).
   - Tuần 7 chính thức khởi động tiến độ Milestone 2. Thanh nhấn mạnh tiến độ đang bị đẩy nhanh, tuần này phải xúc tiến mạnh — đặc biệt là phần Toán — để chốt nền tảng trước khi chuyển sang phần kế tiếp.

2. **Cập nhật tiến độ theo từng phần**
   - **Toán học (Sơn & Ý)**: Sơn đã hoàn thành phần chứng minh Policy Gradient Theorem đầu tiên. Ý chia sẻ phần trực quan: phân biệt Gradient Ascent vs Gradient Descent và minh hoạ ảnh hưởng khi thay đổi các biến trong công thức. Mục tiêu là giúp người nghe (kể cả không chuyên) cảm nhận được công thức hoạt động ra sao. Phân công: Sơn tập trung viết phần Proof, Ý phụ trách phần Giải thích/Minh hoạ. Sơn viết chứng minh trên giấy/LaTeX và gửi Ý review; ngược lại Sơn sẽ tinh chỉnh phần của Ý để nội dung khớp nhau.
   - **Code (Thanh)**: Phần lập trình các thuật toán liên quan tới mô hình, huấn luyện và tối ưu gần như đã hoàn tất. Cần xác định bước tiếp theo (đánh giá/so sánh kết quả) sau khi phần toán được chốt để gắn kết hai phần. Quy ước làm việc: mọi người push code/tài liệu lên branch riêng để cả nhóm dễ theo dõi update; tránh trôi tin nhắn trong group chat.
   - **Báo cáo (Quỳnh)**: Trong kỳ nghỉ lễ đã hoàn thành Chapter 1 của báo cáo. Tuần 7 sẽ tiếp tục Chapter 2, 3, 4; sau đó quay lại tinh chỉnh Chapter 1 để các chương đồng bộ. Slide: tham khảo template cô gửi — nội dung phải ngắn gọn, súc tích. Hướng làm: lên outline trước, sau đó chắt lọc các ý chính từ báo cáo để bỏ vào slide dần dần. Đề xuất nhúng phần animation/biểu đồ của Ý vào slide để giải thích công thức toán một cách trực quan.

3. **Thảo luận trọng tâm**
   - **Roadmap & Milestone**: Roadmap đã được điều chỉnh một lần, hiện chia thành 5 milestone — bắt buộc phải đi qua đủ 5. Cả nhóm đồng thuận tuần này phải đẩy nhanh tiến độ, và hoàn tất phần Toán.
   - **Phong cách đánh giá của giảng viên**: Cô có xu hướng quy chiếu về các bài học cô đã giảng để hỏi xoáy. Nhóm cần chủ động liên hệ kiến thức cũ (giải tích, đại số, các bài cô đã dạy) vào đồ án; nắm vững phần kiến thức nền sẽ giúp trả lời các câu hỏi vận dụng tốt hơn.
   - **Liên hệ với giảng viên**: Thống nhất sẽ gửi cô bản tóm tắt/đề mục để xin định hướng, nhưng phải viết ngắn gọn, súc tích. Nhiều câu hỏi cô sẽ giữ lại tới buổi thuyết trình, vì vậy nhóm cần chuẩn bị trước cả các câu cô có thể hỏi.

## Thay đổi & Quyết định bổ sung (giữa tuần)

- **Thanh (PM)**: Điều chỉnh hướng tuần 07 — ưu tiên hoàn thành sớm toàn bộ nhánh Code để dành thời gian cho toán, báo cáo, demo và final package.
- **Thanh (PM)**: Cập nhật roadmap/PDR/README: phần Code đã hoàn thành trước tiến độ, M2 hoàn thành, M3 hoàn thành sớm phần code.
- **Thanh (PM)**: Chốt quy tắc thư mục `reports/` — `detailed_reports/` dùng file phẳng (`week-XX.md`), không dùng thư mục con.
- **Cả nhóm**: Quy ước push code/tài liệu lên branch riêng để dễ theo dõi; tránh trôi tin nhắn trong group chat.

## Đã hoàn thành

- [x] **Thanh (Code Lead)**: Merge PR #37 — reproducible entrypoints (`scripts/train.py`, `scripts/evaluate.py`) với seed/config/output tái lập.
- [x] **Thanh (Code Lead)**: Merge PR #38 — hyperparameter tuning runner (`scripts/run_experiments.py`) với grid search và ranked summary.
- [x] **Thanh (Code Lead)**: Merge PR #39 — visualization script (`scripts/visualize.py`) sinh figure report-ready 300 DPI.
- [x] **Thanh (Code Lead)**: Merge PR #40 — logic explanation & math-to-code mapping (`docs/code-logic-explanation.md`).
- [x] **Thanh (Code Lead)**: Merge PR #41 — đồng bộ README, roadmap, PDR và docs sau CODE-05..08.
- [x] **Sơn (Math/Code)**: Merge PR #44 — Windows training outputs (CPU, 1000 episodes, mean_last_50 = 476.94, best/final = 500).
- [x] **Ý (Math)**: Hoàn thành MATH-02 (Log-derivative trick, Objective Function) và MATH-03 (Gradient estimate, PG vs DQN).
- [x] **Quỳnh (Report)**: Cập nhật MoM tuần 7, hoàn thiện Chapter 2 Mathematical Foundations, lên outline slide thuyết trình.
- [x] **Thanh (PM)**: Đóng Master Project Tracker issue #26; chuẩn hóa quy tắc thư mục `reports/`.

## Quyết định chính (Họp Tuần 07)

- **Cả nhóm**: Code Phase (CODE-03..08) chính thức hoàn thành. Chuyển trọng tâm sang Math (PR #42) và Report (Chapter 3/4 + Slide).
- **Thanh (Code Lead)**: Kết quả chính thức — last-100 average 476.00, vượt threshold CartPole-v1 (475), best/final reward đều 500.
- **Sơn (Math)**: Tập trung viết phần Proof, Ý phụ trách phần Giải thích/Minh hoạ. Push bản hoàn chỉnh lên Git.
- **Quỳnh (Report)**: Tiếp tục Chapter 2, 3, 4; lên outline Slide trước, sau đó chắt lọc nội dung từ báo cáo để bỏ vào slide. Đề xuất xin animation/biểu đồ của Ý để minh họa trong slide.
- **Thanh (PM)**: Soạn nội dung gửi cô về tiêu chí đánh giá Milestone 1; quyết định thời điểm gửi và cách trình bày sao cho ngắn gọn, súc tích.

## Ticket được phân công

| Ticket        | Description                                    | PIC   | Support |
| :------------ | :--------------------------------------------- | :---- | :------ |
| [MATH-02]     | Log-derivative trick & Objective Function      | Sơn     | Ý     |
| [MATH-03]     | Gradient estimate & PG vs Value-based          | Sơn     | Ý     |
| [CODE-05..08] | Reproducible entrypoints, HP tuning, viz, docs | Thanh | —       |
| [PR #42]      | Deep dive documentation for Policy Gradient    | Ý   | Sơn   |
| [RPT-03]      | Chapter 2, 3 & 4 (Math, Methods & Experiments) | Quỳnh | Thanh   |
| [RPT-04]      | Slide thuyết trình                             | Quỳnh | Cả nhóm |
| [FINAL-02]    | Final run, demo package, rehearsal             | Thanh | Cả nhóm |

## Việc cần làm (Hạn: Chủ nhật 10/05, 23:00)

- [x] **Sơn (Math)**: Hoàn thiện chứng minh Policy Gradient Theorem trên giấy/LaTeX; tinh chỉnh phần của Ý để thống nhất.
- [x] **Thanh (Code Lead)**: Hoàn thành & merge CODE-05..08.
- [x] **Quỳnh (Report)**: Viết Chapter 2, 3, 4; lên outline Slide.
- [x] **Ý (Math)**: Hoàn thành MATH-02/MATH-03; push file giải thích/biểu diễn cho Sơn review.

## Trở ngại

- **Sơn (Math)**: PR #42 vẫn open — cần review/chốt lỗi formatting LaTeX/Markdown trước khi merge.
- **Thanh (Code Lead)**: CODE-05 walkthrough/Q&A với Sơn & Quỳnh vẫn cần ghi nhận evidence người thật nếu cần.
- **Quỳnh (Report)**: Báo cáo Word cần integrate Chapter 3/4 rồi Thanh review PDF.

## Họp tiếp theo

- **Tuần 08**: Tối thứ Hai — Review PR #42, chốt báo cáo Word, bàn demo & rehearsal.
