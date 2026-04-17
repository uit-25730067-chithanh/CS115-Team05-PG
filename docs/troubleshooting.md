# Cẩm nang Xử lý Sự cố & Các Vấn đề Đã Biết (Troubleshooting & Known Issues)

Tài liệu này ghi chú lại các rủi ro kỹ thuật và lỗi tiềm tàng có thể xảy ra trong quá trình chạy mã nguồn Policy Gradient (REINFORCE) phiên bản Backup, để team kịp thời nhận diện và xử lý.

---

## 1. Lỗi trên MacOS dùng chip M-series (Apple Silicon / MPS)

- **Triệu chứng:** Khi chạy `train.py`, quá trình huấn luyện có thể đột ngột bị Crash hoặc báo lỗi liên quan đến Tensor/MPS/Multinomial. Hoặc tốc độ chạy cực kì chậm so với bình thường.
- **Nguyên nhân gốc (Root cause):** PyTorch sử dụng backend `MPS` (Metal Performance Shaders) trên MacOS để tăng tốc phần cứng. Tuy nhiên, một số hàm tính toán phân phối thống kê như `torch.distributions.Categorical.sample()` chưa được tối ưu hoặc tương thích hoàn hảo trên các phiên bản PyTorch ở môi trường MPS. Ngoài ra, với một mạng nơ-ron quá nhỏ (như bài CartPole với 1 lớp ẩn 128 nodes), thời gian gửi dữ liệu qua lại giữa RAM (CPU) và GPU (MPS) còn tốn thời gian hơn là tính toán trực tiếp trên CPU.
- **Cách khắc phục:**
  Mở file `sources/train.py`, tìm đoạn thiết lập device và ép thiết bị chạy hoàn toàn bằng CPU:

  ```python
  # Thay vì để auto-detect MPS, hãy hard-code CPU cho project này:
  device = torch.device("cpu")
  ```

## 2. Kết quả Train ra biểu đồ không đồng nhất (Reproducibility Issue)

- **Triệu chứng:** Team chạy ra kết quả đạt 500 reward. Nhưng khi demo cho giảng viên xem hoặc chạy lại bằng đúng code đó thì Reward lại sụt giảm, đường biểu đồ (learning curve) có hình thù khác hẳn.
- **Nguyên nhân gốc (Root cause):**
  Dù đã cố cố định Random Seed của PyTorch và NumPy bằng `torch.manual_seed(42)` và `np.random.seed(42)`, bản thân môi trường tương tác `Gymnasium` vẫn tiếp tục sinh ra các state ở trạng thái ngẫu nhiên độc lập trong mỗi lần `reset()`.
- **Cách khắc phục:**
  Nếu yêu cầu báo cáo cần sự nhất quán 100% trong hình dáng biểu đồ khi chạy lại, hãy đưa parameter seed vào hàm reset của môi trường tại episode đầu tiên hoặc trong suốt training (mặc dù điều này làm mất đi tính tổng quát của Agent):

  ```python
  # Ở lần reset đầu tiên, hoặc mỗi khi cần agent chạy đúng một lịch trình:
  state, _ = env.reset(seed=42)
  # Nhớ thiết lập action_space seed trước lúc chạy
  env.action_space.seed(42)
  ```

## 3. Lỗi Tràn RAM (OOM - Out Of Memory) - [Khó xảy ra với CartPole]

- **Triệu chứng:** Python báo lỗi `MemoryError` hoặc hệ thống bị treo cứng (freeze).
- **Nguyên nhân gốc (Root cause):** Việc thuật toán REINFORCE lặp qua từng time step và đưa loss vào một list (`policy_loss.append(-log_prob * G_t)`) sẽ lưu giữ lại toàn bộ Computation Graph của PyTorch trong bộ nhớ cho đến lúc thực thi xong hàm `backward()`. Nếu số step trong 1 episode kéo dài đến vài chục ngàn bước, Graph này phình to và nuốt sạch RAM.
- **Cách khắc phục:**
  Với bài CartPole (Max = 500 steps), lỗi này là **gần như không thể**. Nếu chuyển mô hình sang các bài toán khác có vô hạn steps, buộc phải chuyển sang kỹ thuật giới hạn batch (cắt ngắn Rollout thành các batch nhỏ như trong thuật toán A2C hay PPO).
