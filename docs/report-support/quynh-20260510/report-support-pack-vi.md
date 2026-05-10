# Gói Hỗ Trợ Báo Cáo cho Quỳnh

## Bối cảnh

- PDF nguồn: `tmp/documents/CS115-Policy Gradient for Reinforcement Learning (RL).pdf`
- Text đã trích xuất để review: `tmp/report_latest_pypdf2_text.txt`
- Mục tiêu: hỗ trợ report lead hoàn thiện bản nháp hiện tại mà không sửa trực tiếp file Word/PDF gốc.
- Trạng thái: chỉ là tài liệu hỗ trợ; team cần đọc lại trước khi đưa vào báo cáo cuối.

## 1. Checklist Review Nhanh cho Quỳnh

### Các điểm cần sửa gấp

- **Kiểm tra List of Figures/Tables**: đảm bảo mọi hình/bảng được liệt kê đều thuộc đúng đề tài này; nếu còn mục template/stale thì bỏ. Thay bằng hình CartPole/training.
- **Xóa placeholder**: thay `To be updated` và `[Link]` trong Abstract.
- **Điền bảng phần trăm đóng góp**: trang 6 hiện còn trống phần contribution percentage.
- **Hoàn thiện Chapter III**: phần Methods hiện chủ yếu mới có heading.
- **Hoàn thiện Chapter IV**: phần Experiments & Results hiện chủ yếu mới có heading.
- **Tránh claim về critic không có trong code**: outline hiện có `constant baseline (or critic)` và ablation liên quan critic. Code hiện tại dùng normalized returns, không phải actor-critic.
- **Dùng đúng thuật ngữ theo code thật**: `REINFORCE`, `PolicyNetwork`, `CartPole-v1`, `Categorical`, `log_prob`, `discounted returns`, `normalized returns`.
- **Claim kết quả cẩn thận**: run hiện tại đạt `mean_last_100 = 476.0000`, vượt threshold CartPole-v1 là 475, với seed/config ghi bên dưới.

### Polish mức vừa

- **Sửa grammar và spacing**: ví dụ `leaning rate` -> `learning rate`, `back propagation` -> `backpropagation`, `para meterization` -> `parameterization`.
- **Thống nhất viết hoa**: `Policy Gradient`, `REINFORCE`, `PyTorch`, `Gymnasium`, `CartPole-v1`.
- **Thêm caption cho mọi hình**: mỗi caption nên nói rõ người đọc cần thấy điều gì.
- **Giữ scope đúng với dự án**: không distributed training, không actor-critic, không thêm environment khác.
- **Chỉ thêm repository link khi URL final đã được xác nhận**.

## 2. Evidence Đã Xác Minh từ Outputs Hiện Có

### Random baseline

Nguồn: `outputs/baseline_20260510_011932/baseline_stats.txt`

| Metric | Value |
| --- | ---: |
| Environment | CartPole-v1 |
| Episodes | 100 |
| Mean reward | 23.2800 |
| Standard deviation | 13.0791 |
| Minimum reward | 9 |
| Maximum reward | 88 |

Hình có thể đưa vào report:

- `outputs/baseline_20260510_011932/baseline_curve.png`
- Độ phân giải: 1000 x 500 px

### Run REINFORCE đã train

Nguồn: `outputs/run_20260510_011946/`

| Field | Value |
| --- | --- |
| Environment | CartPole-v1 |
| Episodes | 1000 |
| Learning rate | 0.001 |
| Discount factor gamma | 0.99 |
| Hidden dimension | 128 |
| Seed | 123 |
| Device | CPU |

Metrics từ `metrics.txt` và `rewards.txt`:

| Metric | Value |
| --- | ---: |
| Mean reward, last 50 episodes | 476.9400 |
| Std reward, last 50 episodes | 57.6664 |
| Mean reward, last 100 episodes | 476.0000 |
| Std reward, last 100 episodes | 56.6927 |
| Mean reward, last 200 episodes | 460.1500 |
| Best episode reward | 500.0000 |
| Final episode reward | 500.0000 |
| Last-100 min reward | 286.0000 |
| Last-100 max reward | 500.0000 |
| First 100-episode window >= 475 | Episode 752, average 475.6200 |
| Last 10 rewards | 326, 500, 500, 500, 500, 500, 500, 374, 500, 500 |

Hình có thể đưa vào report:

- `outputs/run_20260510_011946/training_curve.png`
- Độ phân giải: 1000 x 500 px

Claim đề xuất:

> Với cấu hình `lr=0.001`, `gamma=0.99`, `hidden_dim=128`, và `seed=123`, agent REINFORCE đạt average reward 100 episode cuối là `476.00`, vượt threshold chuẩn của CartPole-v1 là `475`. Best reward và final reward đều đạt `500`; reward trong 100 episode cuối vẫn dao động từ `286` đến `500`, đây là hành vi bình thường của training Policy Gradient Monte Carlo.

## 3. Gói Nội Dung Kỹ Thuật — Chapter III Methods

### 3.1 REINFORCE Algorithm

Dự án triển khai thuật toán REINFORCE, một phương pháp Monte Carlo Policy Gradient tối ưu trực tiếp stochastic policy. Thay vì học action-value table rồi suy ra policy gián tiếp, REINFORCE tham số hóa policy dưới dạng `pi_theta(a|s)` và cập nhật tham số policy theo hướng tăng xác suất của các action tạo ra return cao.

Ở mỗi episode, agent thu thập trajectory gồm state, sampled action, log-probability và reward. Sau khi episode kết thúc, thuật toán tính discounted return cho từng time step:

`G_t = R_t + gamma R_{t+1} + gamma^2 R_{t+2} + ...`

Implementation tính giá trị này ngược từ cuối episode về đầu, giúp tái sử dụng future return đã tính và giữ độ phức tạp tuyến tính theo độ dài episode. Policy update dựa trên loss:

`L(theta) = - sum_t log pi_theta(a_t | s_t) G_t`

Dấu âm cần thiết vì optimizer của PyTorch minimize loss, trong khi Policy Gradient muốn maximize expected return. Vì vậy minimize negative log-probability weighted by return tương đương gradient ascent trên expected reward objective.

Implementation cũng normalize returns trong mỗi episode:

`G_t <- (G_t - mean(G)) / (std(G) + epsilon)`

Normalization này là kỹ thuật giảm variance đơn giản. Nó không thêm learned critic; nó chỉ giúp ổn định training bằng cách giảm scale variation của Monte Carlo returns.

### 3.2 Environment Setup

Thí nghiệm dùng `CartPole-v1` từ Gymnasium. State là vector liên tục 4 chiều gồm cart position, cart velocity, pole angle, và pole angular velocity. Action space rời rạc có hai action: đẩy xe sang trái hoặc đẩy xe sang phải. Environment cho reward `+1` ở mỗi time step mà pole vẫn cân bằng; maximum episode return là `500`.

Environment này phù hợp vì đủ đơn giản để nối toán với code, nhưng vẫn là bài toán sequential decision-making dưới uncertainty. Nó cũng có solved criterion chuẩn: average reward ít nhất `475` trên 100 consecutive episodes.

### 3.3 Policy Network Architecture

Policy được biểu diễn bằng một multilayer perceptron nhỏ trong PyTorch. Network nhận state 4 chiều của CartPole, qua một hidden layer với ReLU activation, rồi output probability distribution trên 2 actions bằng Softmax.

Trong training, action được sample từ `Categorical` distribution tạo từ output probabilities. Sampling stochastic này quan trọng vì REINFORCE học từ sampled trajectories; nếu dùng greedy action quá sớm thì exploration giảm và policy có thể kẹt ở behavior yếu. Trong evaluation, implementation dùng action có probability cao nhất để đo policy đã học theo cách xác định hơn.

### 3.4 Training Pipeline

Training pipeline theo vòng lặp episode-based. Đầu mỗi run, script tạo Gymnasium environment, khởi tạo policy network, cấu hình optimizer, và set seed để tăng reproducibility. Ở mỗi episode, agent quan sát state hiện tại, sample action từ policy, apply action vào environment, rồi lưu reward và log-probability tương ứng.

Sau khi episode kết thúc, thuật toán tính discounted returns, normalize chúng, xây policy loss, và backpropagate qua saved log-probabilities. Run lưu checkpoints, raw rewards, configuration, metrics, và training curve vào output directory theo timestamp.

Bảng hyperparameter đề xuất:

| Hyperparameter | Value | Meaning |
| --- | ---: | --- |
| Environment | CartPole-v1 | Benchmark control task |
| Episodes | 1000 | Number of training episodes |
| Learning rate | 0.001 | Step size for optimizer |
| Discount factor gamma | 0.99 | Weight assigned to future rewards |
| Hidden dimension | 128 | Hidden units in policy network |
| Seed | 123 | Reproducibility seed |

## 4. Gói Nội Dung Kỹ Thuật — Chapter IV Experiments & Results

### 4.1 Experimental Setup

Thí nghiệm đánh giá liệu implementation REINFORCE có học được policy giữ cân bằng CartPole trong thời gian dài hay không. Random baseline dùng để cho thấy performance của untrained policy, còn trained run đo learning behavior của Policy Gradient agent.

Cấu hình chính: `CartPole-v1`, 1000 episodes, learning rate `0.001`, discount factor `0.99`, hidden dimension `128`, seed `123`. Performance được đánh giá bằng episode rewards, moving-average reward trend, và threshold chuẩn CartPole-v1 là average reward `475` trên 100 consecutive episodes.

### 4.2 Main Results

Random baseline đạt mean reward `23.28` trên 100 episodes, với maximum reward `88`. Điều này cho thấy random actions không thể solve task và là mốc so sánh performance thấp.

Trained REINFORCE agent đạt last-100-episode average reward `476.00`, vượt threshold chuẩn của CartPole-v1. Best episode reward và final episode reward đều đạt `500`, là maximum return của environment. Window 100 episodes đầu tiên có average reward vượt `475` xuất hiện tại episode `752`, với average reward `475.62`.

Kết quả này cho thấy implementation cải thiện policy thành công từ gần-random behavior thành policy có khả năng solve CartPole-v1 với cấu hình đã chọn.

### 4.3 Discussion

Learning curve có nhiễu là điều bình thường vì REINFORCE là thuật toán Monte Carlo Policy Gradient. Mỗi update phụ thuộc vào sampled trajectories, và return có thể dao động đáng kể giữa các episode ngay cả khi policy đã mạnh. Điều này thể hiện trong 100 episode cuối: reward dao động từ `286` đến `500`, nhưng average vẫn vượt threshold solved.

Kết quả phù hợp với Policy Gradient Theorem. Các action dẫn đến return cao nhận reinforcement dương lớn hơn qua term `log pi_theta(a_t|s_t) G_t`, làm tăng probability của chúng trong các state tương tự sau này. Return normalization giúp giảm variance và ổn định optimization, nhưng không loại bỏ toàn bộ stochastic fluctuation.

### 4.4 Suggested Figures and Captions

- **Figure 1. Random baseline reward curve on CartPole-v1.** Hình này cho thấy reward của random policy trên 100 episodes. Mean reward thấp cho thấy random action không đủ để giữ pole cân bằng.
- **Figure 2. REINFORCE training curve over 1000 episodes.** Hình này cho thấy episode reward cải thiện trong quá trình training. Moving average tăng dần về maximum return, thể hiện policy đã học được cách cân bằng pole.
- **Table 1. Hyperparameter configuration.** Bảng này ghi lại training settings của main experiment.
- **Table 2. Baseline versus trained policy performance.** Bảng này so sánh random baseline và trained REINFORCE policy theo mean reward và maximum reward.

Bảng comparison đề xuất:

| Method | Episodes | Mean reward | Best/Max reward | Note |
| --- | ---: | ---: | ---: | --- |
| Random baseline | 100 | 23.2800 | 88 | Untrained policy |
| REINFORCE trained policy | 1000 | 476.0000 last-100 avg | 500 | Solves CartPole-v1 threshold |

## 5. Kế Hoạch Hoàn Thiện Report

### Quỳnh — Report Lead

- **Sửa formatting leftovers**: List of Figures, placeholders, contribution percentage table.
- **Paste và adapt Chapter III/IV content**: dùng nội dung kỹ thuật ở trên, rồi rewrite theo văn phong của Quỳnh.
- **Chèn figures**: baseline curve và training curve.
- **Update captions và table numbering**.
- **Đảm bảo final PDF không còn placeholder**.

### Thanh — Code Lead

- **Cung cấp final evidence**: output paths, hyperparameters, metrics, và figure files.
- **Xác nhận wording phương pháp**: normalized returns, không phải critic.
- **Check mọi claim với code thật**.
- **Có thể chạy final evaluation command** nếu team muốn thêm stats riêng từ `best_policy.pth`.

### Sơn — Math Lead

- **Hoàn thiện các math subsection còn thiếu**: value function, policy parameterization, stochastic policy, Softmax, variance, baseline theorem, advantage function.
- **Check symbols**: thống nhất notation giữa Chapter II và III.
- **Đảm bảo proof nối được với code**: `log_prob`, `G_t`, và policy update.

### Đức Ý — Supporter

- **Proofread formatting**: page numbering, headings, tables, figure references.
- **Check references**: đảm bảo citation nào cũng có trong reference list.
- **Check final PDF**: không broken equations, không mất hình.

## 6. Next Actions Đề Xuất

1. Quỳnh sửa placeholders và stale figure/table entries trước.
2. Thanh gửi Quỳnh metrics và figure files đã liệt kê.
3. Sơn hoàn thiện theory sections còn thiếu trước writing pass cuối.
4. Quỳnh tích hợp Chapter III/IV, rồi export PDF.
5. Thanh review claim-vs-code lần cuối trước khi nộp.

## 7. Câu Hỏi Còn Mở Trước Khi Nộp Final

- Repository URL public final để đưa vào Abstract là gì?
- Contribution percentages nên ghi như thế nào?
- Giảng viên yêu cầu report tiếng Việt hay tiếng Anh? Bản hiện tại đang là tiếng Anh.
- Report có cần thêm final evaluation stats từ `scripts/evaluate.py`, hay training evidence hiện tại là đủ?
- Team có muốn giữ ablation studies không, hay nên simplify vì evidence/code hiện chủ yếu support một final configuration cộng baseline?
