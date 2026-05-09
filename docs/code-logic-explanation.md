# CODE-05: Tài liệu giải thích logic REINFORCE

## Mục đích

Tài liệu này chuẩn bị nội dung giải thích cho CODE-05 để Thanh có thể trình bày lại implementation REINFORCE cuối cùng cho Sơn và Quỳnh. Đây là evidence cho phần tài liệu trong PR. Tuy nhiên, quality gate của con người vẫn bắt buộc: ticket chỉ nên được xem là hoàn tất sau khi team xác nhận phần hỏi đáp.

## 1. Trạng thái, hành động và phần thưởng trong CartPole

`CartPole-v1` cung cấp cho agent một vector trạng thái liên tục gồm bốn giá trị:

- **Vị trí xe đẩy**: xe đang nằm ở đâu trên trục ngang.
- **Vận tốc xe đẩy**: xe đang di chuyển nhanh hay chậm.
- **Góc nghiêng của cột**: cột lệch khỏi phương thẳng đứng bao nhiêu.
- **Vận tốc góc của cột**: cột đang xoay nhanh hay chậm.

Không gian hành động là rời rạc:

- **Action 0**: đẩy xe sang trái.
- **Action 1**: đẩy xe sang phải.

Môi trường trả reward `+1` cho mỗi time step mà cột vẫn được giữ thăng bằng. Episode return càng cao nghĩa là policy giữ cột đứng được càng lâu.

## 2. `PolicyNetwork`: từ trạng thái sang xác suất hành động

`PolicyNetwork` trong `sources/models/policy.py` là một MLP nhỏ:

- **Input**: một vector trạng thái CartPole.
- **Hidden layer**: `Linear(state_dim, hidden_dim)` rồi qua ReLU.
- **Output layer**: `Linear(hidden_dim, action_dim)`.
- **Softmax**: chuyển raw scores thành phân phối xác suất trên các hành động.

Thành phần này hiện thực stochastic policy:

$$
\pi_\theta(a \mid s)
$$

Trong code, `forward()` trả về xác suất, ví dụ `[0.45, 0.55]`, nghĩa là policy hiện tại gán 45% xác suất cho action 0 và 55% xác suất cho action 1.

## 3. `select_action()`: vì sao training dùng sample thay vì argmax

Trong training, `select_action()` dùng `Categorical(probs).sample()` thay vì `argmax`.

Sampling là cần thiết vì REINFORCE học từ các trajectory ngẫu nhiên. Nếu model luôn chọn action có xác suất lớn nhất quá sớm, agent có thể ngừng khám phá và bị kẹt ở một policy yếu. Sampling cho phép cả hai hành động được thử theo phân phối hiện tại của policy; sau đó update sẽ tăng hoặc giảm xác suất dựa trên return quan sát được.

Trong evaluation, `scripts/evaluate.py` dùng `torch.argmax(probs, dim=-1)` bên trong `torch.no_grad()` vì evaluation cần đo policy đã học theo cách xác định hơn, không tiếp tục exploration.

## 4. `log_prob`: liên hệ với log-derivative trick

Policy Gradient Theorem dùng công thức:

$$
\nabla_\theta J(\theta) = \mathbb{E}\left[\nabla_\theta \log \pi_\theta(a_t \mid s_t) G_t\right]
$$

Đối tượng quan trọng là `log_prob`, không chỉ là `prob`. Trong `select_action()`, code lưu:

```python
log_prob = m.log_prob(action)
```

Đây là giá trị tương ứng trong code của:

$$
\log \pi_\theta(a_t \mid s_t)
$$

PyTorch giữ computation graph từ tham số mạng đến `log_prob`, nên `policy_loss.backward()` có thể tính gradient cho policy network.

## 5. `compute_returns()`: Monte-Carlo return

`compute_returns(rewards, gamma)` trong `sources/reinforce.py` tính discounted Monte-Carlo return:

$$
G_t = R_t + \gamma R_{t+1} + \gamma^2 R_{t+2} + \dots
$$

Code duyệt ngược qua danh sách rewards:

```python
G_t = r + gamma * G_t
```

Cách này hiệu quả vì mỗi giá trị mới tái sử dụng return đã tính cho time step tương lai. Trong CartPole, `gamma` điều khiển mức độ agent coi trọng việc sống sót ở các bước sau, không chỉ reward `+1` ngay tại hiện tại.

## 6. `update_policy()`: vì sao loss có dấu âm

Mục tiêu toán học là maximize expected return `J(theta)`. REINFORCE cần cập nhật tham số theo hướng gradient ascent:

$$
\theta \leftarrow \theta + \alpha G_t \nabla_\theta \log \pi_\theta(a_t \mid s_t)
$$

Optimizer của PyTorch mặc định minimize loss. Để biến bài toán maximize thành minimize, implementation dùng:

```python
policy_loss.append(-log_prob * G_t)
```

Do đó, minimize `-log_prob * G_t` tương đương maximize `log_prob * G_t`.

Hàm này cũng chuẩn hóa returns khi episode có nhiều hơn một step:

$$
G_t \leftarrow \frac{G_t - \mu(G)}{\sigma(G) + \epsilon}
$$

Đây là một dạng baseline đơn giản để giảm variance. Nó không đổi mục tiêu học tổng thể, nhưng giúp gradient bớt nhiễu hơn.

## 7. `scripts/train.py`: vòng đời của một training run

Một training run đi qua các bước sau:

1. Parse CLI arguments: environment, số episode, learning rate, discount factor, hidden dimension, seed và output directory.
2. Tạo output directory dưới `outputs/run_YYYYMMDD_HHMMSS/` nếu không truyền `--save-dir`.
3. Gọi `train_reinforce()` từ `sources/train.py`.
4. Seed PyTorch, NumPy và Gymnasium action space để tăng khả năng tái lập.
5. Tạo `CartPole-v1`, suy ra `state_dim` và `action_dim`, rồi khởi tạo `PolicyNetwork`.
6. Với mỗi episode: sample action, thu `log_probs` và rewards, tính returns, rồi update policy.
7. Lưu `best_policy.pth`, `final_policy.pth`, `rewards.txt`, `run_config.txt`, `metrics.txt`, `README.txt` và `training_curve.png`.

Demo command:

```bash
python3 scripts/train.py --episodes 50 --seed 42
```

## 8. `scripts/evaluate.py`: đánh giá checkpoint

Evaluation load một checkpoint đã lưu vào cùng kiến trúc `PolicyNetwork`. Tham số `--hidden-dim` phải khớp với training run đã tạo checkpoint.

Evaluation dùng greedy action xác định:

```python
action = torch.argmax(probs, dim=-1).item()
```

Script ghi ra:

- **`eval_log.txt`**: reward theo từng evaluation episode.
- **`eval_stats.txt`**: checkpoint path, environment, số episode, seed, device, mean reward, standard deviation, best reward và worst reward.

Demo command:

```bash
python3 scripts/evaluate.py --checkpoint outputs/<run>/best_policy.pth --episodes 10 --hidden-dim <hidden_dim>
```

## 9. Cách đọc `training_curve.png` và final figures

`training_curve.png` gồm:

- **Raw reward curve**: reward từng episode có thể dao động mạnh vì REINFORCE có tính ngẫu nhiên.
- **Moving average curve**: xu hướng mượt hơn trên các episode gần nhất.
- **Pattern kỳ vọng**: moving average nên tăng dần nếu training đang cải thiện.

`scripts/visualize.py` sinh các figure sẵn sàng đưa vào report từ experiment logs:

- **`learning_curve_best.png`**: reward curve của run tốt nhất.
- **`baseline_vs_trained.png`**: so sánh random baseline với best trained run, nếu có baseline log.
- **`hp_comparison.png`**: ranking hyperparameter theo reward gần đây.
- **`summary_grid.png`**: bảng tóm tắt compact của experiment results.
- **`figure_summary.txt`**: tóm tắt text của các figure đã sinh.

Demo command:

```bash
python3 scripts/visualize.py --experiment outputs/experiments/<experiment-dir> --baseline outputs/baseline_<timestamp>/baseline_log.txt
```

## Bảng đối chiếu math-to-code

| Toán học | Code | File |
| --- | --- | --- |
| $s_t$ | `state` | `sources/train.py` |
| $a_t$ | `action` | `sources/models/policy.py`, `sources/train.py` |
| $\pi_\theta(a \mid s)$ | `PolicyNetwork.forward()` | `sources/models/policy.py` |
| Sample action từ policy | `Categorical(probs).sample()` | `sources/models/policy.py` |
| $\log \pi_\theta(a_t \mid s_t)$ | `m.log_prob(action)` | `sources/models/policy.py` |
| Episode rewards | `rewards.append(reward)` | `sources/train.py` |
| $G_t$ | `compute_returns()` | `sources/reinforce.py` |
| Chuẩn hóa return | `(returns - returns.mean()) / (returns.std() + 1e-8)` | `sources/reinforce.py` |
| $-\log \pi_\theta(a_t \mid s_t)G_t$ | `policy_loss.append(-log_prob * G_t)` | `sources/reinforce.py` |
| Gradient update | `policy_loss.backward()` và `optimizer.step()` | `sources/reinforce.py` |
| Training entrypoint | `train_reinforce()` | `sources/train.py`, `scripts/train.py` |
| Evaluation entrypoint | `policy_net.load_state_dict(...)` và greedy action | `scripts/evaluate.py` |
| Figure generation | `find_runs()` và các plot functions | `scripts/visualize.py` |

## Checklist demo

Dùng các lệnh sau trong buổi review. Thay placeholder bằng đường dẫn thật trên máy local.

```bash
python3 scripts/train.py --episodes 50 --seed 42
python3 scripts/evaluate.py --checkpoint outputs/<run>/best_policy.pth --episodes 10 --hidden-dim <hidden_dim>
python3 scripts/visualize.py --experiment outputs/experiments/<experiment-dir> --baseline outputs/baseline_<timestamp>/baseline_log.txt
```

Evidence kỳ vọng:

- Training command tạo một thư mục `outputs/run_.../` mới.
- Evaluation command tạo một thư mục `outputs/eval_.../` mới.
- Visualization command tạo các figure report-ready dưới `outputs/figures/.../`.
- Các output path đã sinh nên được ghi lại trong GitHub issue hoặc PR description.

## Checklist hỏi đáp với team

CODE-05 chưa hoàn tất thật sự cho đến khi checklist này được team xác nhận.

- [ ] Sơn hiểu vì sao `log_prob` cần thiết cho log-derivative trick.
- [ ] Sơn hiểu `compute_returns()` map với $G_t$ như thế nào.
- [ ] Quỳnh hiểu cách mô tả `training_curve.png`, evaluation stats và final figures trong report.
- [ ] Thanh xác nhận phần giải thích dấu âm trong loss.
- [ ] Các hành vi RL không ổn định, nếu có, được ghi lại kèm seed, command và output path.
- [ ] Kết quả hỏi đáp cuối được ghi vào GitHub issue #11 hoặc append vào tài liệu này.

## Trạng thái hiện tại

- **Đã chuẩn bị trong PR**: tài liệu giải thích, bảng math-to-code, demo commands và checklist hỏi đáp.
- **Vẫn còn human gate**: Thanh cần trình bày nội dung này cho Sơn và Quỳnh trước khi CODE-05 được xem là hoàn tất đầy đủ.
