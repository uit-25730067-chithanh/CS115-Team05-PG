# Hệ thống Tri thức Nội bộ: Từ Toán học đến Reinforcement Learning

Tài liệu này phục vụ mục đích lưu trữ và truyền đạt tri thức chuyên sâu về Reinforcement Learning (RL) cho Team 05. Mục tiêu cốt lõi là xóa bỏ khoảng cách giữa các định lý toán học trừu tượng và thực thi mã nguồn trong PyTorch.

## 0. Yêu cầu Tiên quyết (Prerequisites)

Để không bị "ngợp" khi đọc các chứng minh toán học, bạn nên tự tin với các khái niệm sau:

- **Xác suất (Probability):**
  - Định nghĩa biến ngẫu nhiên (Random Variable).
  - Giá trị kỳ vọng (Expectation) $E_{x \sim P}[f(x)]$: Cách tính và tính chất tuyến tính.
  - Phân phối xác suất rời rạc và hàm mật độ xác suất (PDF).
  - Xác suất có điều kiện và Quy tắc Bayes (Bayes' Rule).
- **Giải tích (Calculus):**
  - Đạo hàm hàm hợp (Chain Rule).
  - Gradient $\nabla_\theta$ và ý nghĩa hình học của nó (hướng tăng nhanh nhất của hàm số).
  - Đạo hàm của hàm Logarit: $\frac{d}{dx} \ln(f(x)) = \frac{f'(x)}{f(x)}$.
- **Học sâu (Deep Learning):**
  - Cấu trúc mạng Neural đơn giản (MLP).
  - Cơ chế lan truyền ngược (Backpropagation) và tối ưu hóa bằng Stochastic Gradient Descent (SGD).
- **RL cơ bản:**
  - Nắm vững các thuật ngữ: State ($s$), Action ($a$), Reward ($r$), Policy ($\pi$).

## 1. Cấu trúc Hệ thống (Knowledge Architecture)

Hệ thống tri thức được phân tách thành 4 phân lớp chức năng:

### Layer 1: Foundations (Nền tảng hệ thống)

Thiết lập ngôn ngữ chung và các tiền đề toán học.

- [01. Định nghĩa RL qua lăng kính MDP](./01-foundations/01-what-is-rl.md)
- [02. Xác suất và Khái niệm Trajectory](./01-foundations/02-probability-101.md)
- [03. Giải tích, Gradient và Bài toán tối ưu Expectation](./01-foundations/03-calculus-refresher.md)

### Layer 2: Math Proofs (Chứng minh và Định lý)

Phân tích logic toán học của thuật toán REINFORCE.

- [01. Hàm mục tiêu $J(\theta)$ và Performance Measure](./02-policy-gradient-math/01-objective-function.md)
- [02. Log-derivative Trick: Chìa khóa đạo hàm kỳ vọng](./02-policy-gradient-math/02-the-gradient-trick.md)
- [03. Chứng minh Định lý Policy Gradient](./02-policy-gradient-math/03-pg-theorem-proof.md)
- [04. Baseline và Kỹ thuật Giảm phương sai (Variance Reduction)](./02-policy-gradient-math/04-variance-reduction.md)

### Layer 3: Code Mapping (Đối sánh Mã nguồn)

Ánh xạ các thành phần toán học vào thực thi logic code.

- [01. Cơ chế tính Loss trong REINFORCE](./03-code-mapping/01-pytorch-autograd.md)
- [02. Phân tích chi tiết Implementation logic](./03-code-mapping/02-implementation-walkthrough.md)

### Layer 4: Application Analysis (Phân tích thực nghiệm)

Giải thích các hiện tượng quan sát được trong quá trình huấn luyện.

- [01. Case Study: Phân tích hội tụ trên môi trường CartPole-v1](./04-application-analysis/01-cartpole-case-study.md)
- [02. Mở rộng hệ thống và giới hạn của REINFORCE](./04-application-analysis/02-scaling-up.md)

## 3. Tài liệu Tham khảo (Core References)

Để có cái nhìn sâu sắc và học thuật hơn, Team 05 khuyến khích tham khảo các nguồn sau:

1. **Sutton & Barto, "Reinforcement Learning: An Introduction" (2nd Ed)** - [Chapter 13: Policy Gradient Methods](http://incompleteideas.net/book/the-book-2nd.html)
2. **Stanford CS234: Reinforcement Learning** - [Lecture Slides (Policy Gradients)](http://web.stanford.edu/class/cs234/slides/lecture5post.pdf) _Sao tài liệu này quen vậy trời_
3. **OpenAI Spinning Up** - [Part 3: Intro to Policy Optimization](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html)
4. **UC Berkeley CS285** - [Lecture 5: Policy Gradients](http://rail.eecs.berkeley.edu/deeprlcourse/static/slides/lec-5.pdf)
