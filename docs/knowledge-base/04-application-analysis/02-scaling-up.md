# Mở rộng hệ thống và Tầm quan trọng thực tiễn

Kiến thức về Policy Gradient và thuật toán REINFORCE mà Team 05 thực hiện trên CartPole không chỉ dừng lại ở một bài tập lý thuyết. Đây là nền tảng của nhiều đột phá công nghệ quan trọng nhất trong những năm gần đây.

## 1. RLHF trong Large Language Models (LLMs)

Các mô hình như ChatGPT hay Claude sử dụng một kỹ thuật gọi là **Reinforcement Learning from Human Feedback (RLHF)** để căn chỉnh (align) câu trả lời của AI với mong muốn của con người.

*   **Policy:** Chính là mô hình ngôn ngữ (Transformer).
*   **Action:** Việc sinh ra một từ (token) tiếp theo.
*   **Reward:** Được tính từ một mô hình khác (Reward Model) đã học cách đánh giá câu trả lời của con người.
*   **Algorithm:** Các biến thể của Policy Gradient (thường là PPO - một phiên bản ổn định hơn của REINFORCE) được dùng để cập nhật trọng số của LLM.

Hiểu được cách REINFORCE đẩy xác suất của một hành động "tốt" lên cao chính là hiểu được cách ChatGPT học cách trả lời lịch sự và hữu ích.

## 2. Từ REINFORCE đến các thuật toán hiện đại

REINFORCE là điểm khởi đầu. Trong thực tế công nghiệp, người ta sử dụng các cải tiến để khắc phục nhược điểm phương sai:

1.  **Actor-Critic:** Thay vì dùng trung bình Return làm Baseline, người ta dùng một mạng neural (Critic) để dự đoán phần thưởng kỳ vọng của từng trạng thái cụ thể.
2.  **Proximal Policy Optimization (PPO):** Giới hạn độ thay đổi của chính sách trong mỗi bước cập nhật để tránh hiện tượng "quên thảm khốc" (catastrophic forgetting) mà chúng ta thấy ở tập 600 của CartPole.
3.  **Deep Q-Learning (DQN):** Một hướng tiếp cận khác dựa trên hàm giá trị (Value-based) thay vì trực tiếp tối ưu hóa chính sách.

## 3. Lời kết cho Team 05

Dự án CS115 này đã giúp chúng ta xây dựng nền tảng vững chắc về:
*   Cách toán học giải quyết các bài toán quyết định tuần tự.
*   Cách hiện thực hóa các công thức đạo hàm phức tạp bằng mã nguồn PyTorch.
*   Cách phân tích và xử lý các vấn đề thực tế như phương sai và hội tụ.

Dù CartPole là một môi trường đơn giản, nhưng các nguyên lý về MDP, Trajectory, và Log-derivative trick là những tri thức bất biến trong thế giới AI hiện đại.

---

## Nguồn tham khảo

- **Sutton & Barto (2018).** *Reinforcement Learning: An Introduction*, 2nd Ed. — §13.5 Actor-Critic Methods (p.332). [Online](http://incompleteideas.net/book/the-book-2nd.html)
- **Schulman, J. et al. (2017).** "Proximal Policy Optimization Algorithms." [arXiv:1707.06347](https://arxiv.org/abs/1707.06347) — PPO algorithm.
- **Mnih, V. et al. (2015).** "Human-level Control through Deep Reinforcement Learning." *Nature*, 518, 529-533. — DQN paper.
- **Ouyang, L. et al. (2022).** "Training Language Models to Follow Instructions with Human Feedback." [arXiv:2203.02155](https://arxiv.org/abs/2203.02155) — InstructGPT/RLHF.
- **Christiano, P. et al. (2017).** "Deep Reinforcement Learning from Human Preferences." NIPS. [arXiv:1706.03741](https://arxiv.org/abs/1706.03741) — RLHF foundations.
