# Chi tiết báo cáo tiến độ - Tuần 05 (Chủ Nhật, 26/04/2026)

Dưới đây là nội dung báo cáo chi tiết từ các thành viên trong tuần 05.

---

## 👤 Đặng Chí Thanh (PM & Code Lead)

### ✅ Đã hoàn thành

- **Quản trị dự án (PM):**
  - Chủ trì họp tuần 05 (20/04, 21:18-22:00, Online Google Meet). Điều phối khi Quỳnh nghỉ ốm, ghi biên bản đầy đủ.
  - Chốt Milestone 1 (Foundation Phase) — setup & nghiên cứu nền tảng đã đạt yêu cầu.
  - Phân công và theo dõi 4 ticket chính: `[MATH-04/05]`, `[CODE-03]`, `[RPT-02]`, `[MGMT-01]`.
  - Điều chỉnh Roadmap để né kỳ nghỉ lễ 30/4 - 1/5 (Week 06), đảm bảo team được nghỉ ngơi mà không mất tiến độ tổng thể.
  - Khảo sát tiêu chí đánh giá của giảng viên và soạn mục lục chi tiết gửi duyệt trước phạm vi (MGMT-01).
  - Quyết định chiến lược **Math Strategy**: Tập trung toán ứng dụng (Applied Math), giải thích công thức qua ví dụ thực tế CartPole-v1 thay vì lý thuyết thuần túy.

- **Kỹ thuật (Code Lead) — PR #30 (merged):**
  - Tinh chỉnh logic `reinforce.py`: cải thiện độ ổn định huấn luyện, bổ sung comment nối liền **log-derivative trick** với nền tảng toán học (`J(theta)` gradient ascent).
  - Nâng cấp `train.py`: thêm hệ thống **timestamped output directories**, lưu `best_policy.pth` dựa trên reward tốt nhất, và logging có cấu trúc (in log mỗi 50 episode kèm best reward).
  - Đồng bộ hóa `README.md`, `README-vi.md`, `docs/installation.md` và kiến trúc hệ thống cho rõ ràng hơn.
  - Xóa biểu đồ tĩnh cũ, chuyển sang tạo động `training_curve.png` trong folder `outputs/run_YYYYMMDD_HHMMSS/`.
  - Code đã chạy thử nghiệm cục bộ thành công (MacOS + MPS/CUDA/CPU fallback).

- **Tài liệu hóa nội bộ — Branch `feature/math-deep-dive` (20 commits, chưa merge):**
  - Xây dựng toàn bộ **hệ thống tri thức nội bộ `docs/knowledge-base/`** (4 layer, 14 file Markdown, 7 ảnh minh họa phong cách _chalkboard_):
    - **Layer 1 — Foundations**: RL qua MDP, Probability 101, Calculus Refresher.
    - **Layer 2 — Math Proofs**: Objective Function, Log-derivative Trick, PG Theorem Proof, Variance Reduction / Baseline.
    - **Layer 3 — Code Mapping**: PyTorch Autograd trong REINFORCE, Implementation Walkthrough.
    - **Layer 4 — Application Analysis**: CartPole Case Study, Scaling-up & Giới hạn của REINFORCE.
  - Soạn **LaTeX Mathematical Notation Standards** (`docs/code-standards.md` cập nhật) để đảm bảo toàn repo render math nhất quán.
  - Viết **Knowledge Base Verification Report** (cross-reference Sutton & Barto, OpenAI Spinning Up, Stanford CS234, UC Berkeley CS285): 0 errors, 7/8 concerns đã fix, 1 observational.
  - Viết **Student Audit Report** từ góc nhìn sinh viên năm 2-3 để kiểm định tính dễ hiểu, sau đó xử lý sâu 4 gaps kiến thức (Prerequisites, Trajectory trực quan, Return G_t, Gradient Ascent intuition).
  - Xử lý audit PR #31: sync code snippets với implementation thực tế, fix toàn bộ reference links và LaTeX rendering issues (italics interference, table math, concern remediation).

### 🚧 Đang làm / Vướng

- Branch `feature/math-deep-dive` vẫn đang chờ review cuối trước khi merge vào `main` (PR dự kiến sau kỳ nghỉ).
- Tốc độ xử lý phần toán học chặt chẽ (Log-derivative trick, PG Theorem Proof) tiêu tốn nhiều thời gian hơn dự kiến — cần cân bằng giữa _độ chính xác học thuật_ và _tính dễ hiểu_.
- Chưa có phản hồi xác nhận từ Sơn về độ ổn định của Gymnasium trên Windows (ticket `[CODE-03]` giao Ý hỗ trợ).

### 📅 Tuần tới (Week 06 — Kỳ nghỉ lễ 30/4 - 1/5)

- Nghỉ lễ chính thức theo Roadmap đã điều chỉnh; không giao task nặng kỹ thuật.
- Merge `feature/math-deep-dive` vào `main` sau kỳ nghỉ, đồng bộ kiến thức nội bộ cho toàn team.
- Thu thập kết quả test môi trường Windows từ Ý / Sơn.
- Chuẩn bị sẵn sàng cho Phase Implementation (Policy MLP tinh chỉnh + Hyperparameter Tuning) ngay sau lễ.

---

## 👤 Xuân Quỳnh (Report Lead)

### ✅ Đã hoàn thành

- Hoàn thành viết Draft Abstract và Chapter 1: Introduction (Motivation, Problem Statement, Objectives & Scope, Contributions, Report Structure).
- Tổng hợp nội dung toán học hiện có vào báo cáo (Chapter 2: Section 2.3).
- Hỗ trợ Team Code test và kiểm tra setup môi trường chạy demo.
- Ghim link báo cáo vào chat Teams.

### 🚧 Đang làm / Vướng mắc

- Review và chỉnh sửa báo cáo tổng thể.
- Chuẩn bị các section còn lại của Chapter 2.
- Gắn link báo cáo vào READMEs (đã tạo PR, đang đợi review).

### 📅 Kế hoạch Tuần tới

- **Tuần 06**: Nghỉ lễ.
- **Tuần 07**:
  - Tổng hợp và hoàn thiện các section còn lại trong Chapter 2: Mathematical Foundations.
  - Hỗ trợ Team Math review và tổng hợp nội dung toán học để đảm bảo tính thống nhất.
  - Hỗ trợ Team Code nếu cần.

---

## 👤 Hoàng Sơn (Math Lead)

### ✅ Đã hoàn thành

- Đã hoàn thành bản hoàn chỉnh chứng minh Policy Gradient Theorem.
- Đã đẩy lên git.
- Đã hoàn thiện tài liệu về phần Policy Gradient.

### 🚧 Đang làm / Vướng mắc

- Đang thực hiện phần việc tiếp theo Gradient Ascent.

### 📅 Kế hoạch Tuần tới

- **Tuần 06:** Nghỉ lễ.
- **Tuần 07:**
  - Hoàn thành 2 phần toán còn lại trong đồ án.
  - Hỗ trợ mọi người về các phần khác như code hay báo cáo.

---

## 👤 Đức Ý

### ✅ Đã hoàn thành

### 🚧 Đang làm / Vướng mắc

- <https://github.com/uit-25730067-chithanh/CS115-Team05-PG/issues/3>

### 📅 Kế hoạch Tuần tới

- <https://github.com/uit-25730067-chithanh/CS115-Team05-PG/issues/5>
