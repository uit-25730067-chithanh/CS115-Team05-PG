# Chi tiết báo cáo tiến độ - Tuần 04 (Chủ Nhật, 19/04/2026)

Dưới đây là nội dung báo cáo chi tiết từ các thành viên trong tuần 04.

---

## 👤 Đặng Chí Thanh (PM & Code Lead)

### ✅ Đã hoàn thành

- **Quản trị dự án (PM):**
  - Chính thức kiêm nhiệm vai trò Code Lead để đẩy nhanh tiến độ kỹ thuật.
  - Tái cấu trúc lộ trình dự án (Roadmap) theo hướng song song hóa Math & Code (PR #28).
  - Thiết lập bộ quy chuẩn `docs/` để tối ưu hóa việc cộng tác với AI (Pair Programming).
  - Thống nhất quy trình làm việc trên Git: branch → PR → Code Review → Merge main.
- **Kỹ thuật (Code Lead):**
  - Cài đặt môi trường huấn luyện (Gymnasium, PyTorch 2.0+, Numpy, Matplotlib).
  - Triển khai thành công Baseline REINFORCE cho không gian hành động rời rạc (CartPole-v1).
  - Hoàn thiện cấu trúc mạng nơ-ron Policy (PolicyNetwork) sử dụng MLP với kiến trúc linh hoạt.
  - Viết logic tính toán Discounted Returns ($G_t$) và kỹ thuật Simple Baseline (chuẩn hóa Returns) để giảm phương sai (Variance reduction).
  - Hoàn thiện kịch bản huấn luyện chính (`train.py`) tích hợp visualization (biểu đồ training curve).

### 🚧 Đang làm / Vướng

- Đang hỗ trợ Sơn (Math Lead) hoàn thiện các bản nháp chứng minh Policy Gradient Theorem trong thư mục `math/`.
- Cần theo dõi thêm hiệu quả của việc chuẩn hóa Returns khi môi trường trở nên phức tạp hơn.
- Vai trò Code Lead mới tiếp nhận đòi hỏi phải review kỹ lại phần code của các thành viên khác trong các tuần tới.

### 📅 Tuần tới

- Phối hợp với team hoàn thiện phần Introduction và Math Foundations cho báo cáo tổng kết.
- Bắt đầu phase huấn luyện chuyên sâu, tinh chỉnh Hyperparameters (Learning rate, Gamma, Hidden dimensions) để đạt kết quả hội tụ ổn định.
- Hỗ trợ team member cài đặt môi trường đồng nhất để test code trên nhiều máy khác nhau.

---

## 👤 Xuân Quỳnh (Report Lead)

### ✅ Đã hoàn thành

- Soạn khung báo cáo Word với format đồ án (heading styles, numbering, TOC tự động, caption figure/table).
- Phân rã mục lục dự kiến 4 chương:
  1. Chapter 1: Introduction
  2. Chapter 2: Mathematical Foundations
  3. Chapter 3: Methods
  4. Chapter 4: Experiments
- Nghiên cứu tổng quan thuật toán Policy Gradient (6 module chính: MDP → Policy → PG Theorem → Variance/Baseline → Implementation → Evaluation).
- Lưu trữ và chia sẻ báo cáo với Team trên OneDrive.

### 🚧 Đang làm / Vướng

- Soạn mô tả/chú thích nội dung từng mục outline để các thành viên khác nắm đúng phạm vi.
- Chuẩn bị viết Abstract và Chapter 1 (Introduction): Motivation, Problem Statement, Objectives & Scope, Contributions, Report Structure.

### 📅 Tuần tới

- Báo cáo: Viết Draft Abstract và Chapter 1 → gửi cho team review.
- Phối hợp Team Math: Review khung Chapter 2 để đảm bảo mạch báo cáo thống nhất.
- Phối hợp Team Code: Hỗ trợ kiểm tra setup môi trường.

---

## 👤 Hoàng Sơn (Math Lead)

### ✅ Đã hoàn thành

- Hoàn thành chứng minh công thức Policy Gradient Theorem.

### 🚧 Đang làm / Vướng

- Thêm các ví dụ cụ thể và dễ hiểu nhất cho phần Policy Gradient.

### 📅 Tuần tới

- Đưa phần công thức Policy bản Word vào báo cáo.
- Đưa 1 phần toán trọng số và estimate cho Ý chuẩn bị.

---

## 👤 Đức Ý

### ✅ Đã hoàn thành

- Cài đặt môi trường (đã bàn giao lại cho Thanh).

### 🚧 Đang làm / Vướng

- Giải thích công thức toán (phụ Sơn nếu cần).

### 📅 Tuần tới

- Hỗ trợ Sơn phần toán học.
