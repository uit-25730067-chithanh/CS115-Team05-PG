# Chi tiết báo cáo tiến độ - Tuần 07 (Chủ Nhật, 10/05/2026)

Dưới đây là nội dung báo cáo chi tiết từ các thành viên trong tuần 07.

---

## 👤 Đặng Chí Thanh (PM & Code Lead)

### ✅ Đã hoàn thành

- **Quản trị dự án (PM):**
  - Khởi động lại tiến độ sau kỳ nghỉ Week 06, chuẩn bị agenda họp tuần 07 và rà soát các tồn đọng từ tuần 05.
  - Điều chỉnh hướng tuần 07: ưu tiên hoàn thành sớm toàn bộ nhánh Code để dành thời gian cho toán, báo cáo, demo và final package.
  - Cập nhật roadmap/PDR/README theo trạng thái mới: phần Code đã hoàn thành trước tiến độ, M2 hoàn thành, M3 hoàn thành sớm phần code.
  - Cập nhật và đóng Master Project Tracker issue #26; chuẩn hóa quy tắc thư mục reports/.

- **Kỹ thuật (Code Lead):**
  - Hoàn thành chuỗi CODE-05..08 qua các PR đã merge:
    - PR #37: thêm scripts/train.py, scripts/evaluate.py, seed/config/output tái lập.
    - PR #38: thêm hyperparameter tuning runner scripts/run_experiments.py.
    - PR #39: thêm visualization script scripts/visualize.py để sinh figure report-ready.
    - PR #40: viết tài liệu giải thích logic REINFORCE và bảng math-to-code mapping.
    - PR #41: đồng bộ README, roadmap, PDR và docs sau khi CODE-05..08 hoàn thành.
  - Hoàn thiện baseline CartPole-v1 qua PR #35: random baseline 100 episodes, mean reward khoảng 22.5.
  - Review/đồng bộ PR #44: thêm kết quả training Windows/CPU 1000 episodes, REINFORCE đạt mean_last_50 = 476.94, best_reward = 500, final_reward = 500.

- **Hỗ trợ báo cáo:**
  - Review bản report mới của Quỳnh, góp ý phần Abstract, List of Figures/Tables, Chapter III Methods và Chapter IV Experiments.
  - Chuẩn bị nội dung tiếng Anh paste-ready cho Quỳnh đưa vào báo cáo: Abstract, Methods, Experiments & Results.
  - Tạo PR #45 dạng draft/support package cho Quỳnh, gồm file Word-ready, Markdown source và README hướng dẫn.
  - Chuẩn bị số liệu và figure chính cho báo cáo:
    - Baseline: [outputs/baseline_20260510_011932/baseline_curve.png]
    - Training: [outputs/run_20260510_011946/training_curve.png]
    - Kết quả chính: last-100 average 476.00, vượt threshold CartPole-v1 475, best/final reward đều 500.

### 🚧 Đang làm / Vướng

- PR #42 feature/math-deep-dive vẫn đang open, cần review thêm phần toán/LaTeX trước khi merge.
- PR #45 chỉ là package hỗ trợ Quỳnh, không cần merge vào main nếu chỉ dùng để chia sẻ tài liệu.
- CODE-05 đã xong kỹ thuật, nhưng walkthrough/Q&A với Sơn và Quỳnh vẫn nên ghi nhận thật nếu cần evidence người thật.
- Báo cáo Word cần Quỳnh integrate Chapter III/IV rồi Thanh review lại PDF.

### 📅 Tuần tới

- Review và chốt PR #42 về phần toán.
- Hỗ trợ Quỳnh hoàn thiện Chapter III/IV trong report Word.
- Chốt final figures/results cho báo cáo và demo.
- Chuẩn bị bước tiếp theo cho FINAL-02: final run/evaluation nếu cần, demo package, rehearsal và Q&A.

---

## 👤 Xuân Quỳnh (Report Lead)

### ✅ Đã hoàn thành

- Cập nhật MoM cho meeting tuần 7.
- Tổng hợp nội dung toán và hoàn thiện các section còn lại trong Chapter 2: Mathematical Foundations.
- Review và chỉnh sửa báo cáo tổng thể.
- Thêm nội dung anh Thanh gửi Chapter 3 & 4 vào báo cáo.
- Lên outline cho slide thuyết trình.

### 🚧 Đang làm / Vướng mắc

- Chỉnh sửa outline và thêm vào những nội dung chính cho slide (sẽ share cho nhóm vào tuần tới).
- Hoàn thiện wording và reference cho Chapter 2.

### 📅 Kế hoạch Tuần tới

- Hoàn thiện Chapter 2: Mathematical Foundations.
- Tổng hợp nội dung Chapter 3 & Chapter 4.
- Share slide thuyết trình với nhóm, tổng hợp những nội dung chính từ báo cáo vào slide.

---

## 👤 Hoàng Cao Sơn (Math Lead)

### ✅ Đã hoàn thành

- Đã tiếp tục hoàn thiện phần toán sau tuần 05, tập trung vào Gradient Ascent, Objective Function $J(\theta)$, Log-derivative Trick và cách liên hệ với Policy Gradient.
- Đã phối hợp với phần code bằng cách chạy thử nghiệm huấn luyện trên Windows cho CartPole-v1.
- Đã thêm kết quả Windows training baseline và kết quả huấn luyện hội tụ:
  - 1000 episodes
  - lr = 0.001
  - gamma = 0.99
  - hidden_dim = 128
  - seed = 123
  - device = CPU
  - best_reward = 500.0
  - final_reward = 500.0
  - mean_last_50 = 476.94
- Đã đẩy kết quả training lên GitHub qua branch feat/windows-training-baseline.
- PR #44 "Feat: Add Windows Training Outputs" đã được merge vào main.

### 🚧 Đang làm / Vướng mắc

- PR #42 "Add deep dive documentation for Policy Gradient research" vẫn đang mở, cần review/chốt một số lỗi formatting LaTeX/Markdown trước khi merge.
- Các issue MATH-02 và MATH-03 trên GitHub vẫn đang mở, cần cập nhật checklist hoặc đóng issue sau khi tài liệu toán được merge/chốt chính thức.
- Branch feat/math-docs-and-config đã có thêm tài liệu deep dive PDF nhưng chưa thấy PR riêng trên GitHub, cần tạo PR hoặc gộp vào PR toán hiện tại.
- Cần rà lại lần cuối cách trình bày công thức để thống nhất với chuẩn LaTeX của repo.

### 📅 Kế hoạch Tuần tới

- Hoàn tất review PR #42 và hỗ trợ sửa các lỗi formatting còn lại nếu cần.
- Tạo PR hoặc merge phần tài liệu deep dive PDF từ branch feat/math-docs-and-config vào main.
- Cập nhật trạng thái các issue MATH-02, MATH-03 sau khi phần toán được chốt.
- Hỗ trợ nhóm đưa phần Gradient Ascent, Objective Function $J(\theta)$, Log-derivative Trick vào báo cáo chính.
- Tiếp tục hỗ trợ phần code/báo cáo nếu nhóm cần đối chiếu giữa công thức toán và kết quả huấn luyện CartPole-v1.

---

## 👤 Đức Ý

### ✅ Đã hoàn thành

- **MATH-02:**
  - Giải thích tại sao cần Log-derivative trick.
  - Trình bày mục tiêu tối ưu hóa.
- **MATH-03:**
  - Giải thích cơ chế cập nhật trọng số.
  - Viết công thức gradient estimate.
  - So sánh sự khác biệt giữa Policy Gradient và Value-based (DQN).
  - Hoàn thiện tài liệu math/policy_gradient_deep_dive.md.
- **CODE:**
  - Cài đặt môi trường trên Windows (đã xác nhận chạy được).

### 🚧 Đang làm / Vướng

- Không.

### 📅 Kế hoạch Tuần tới

- Chưa có task.
