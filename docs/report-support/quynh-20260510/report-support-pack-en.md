# Report Support Pack for Quỳnh

## Context

- Source PDF: `tmp/documents/CS115-Policy Gradient for Reinforcement Learning (RL).pdf`
- Extracted review text: `tmp/report_latest_pypdf2_text.txt`
- Goal: help report lead complete the current draft without editing the Word/PDF directly.
- Status: support material only; human team must review before pasting into final report.

## 1. Quick Review Checklist for Quỳnh

### Critical fixes

- **Verify List of Figures/Tables**: ensure every listed figure/table belongs to this project and remove any stale template entries if present. Replace with CartPole/training figures only.
- **Remove placeholders**: replace `To be updated` and `[Link]` in Abstract.
- **Fill contribution percentage table**: page 6 currently has blank contribution percentages.
- **Complete Chapter III**: Methods currently contains headings only.
- **Complete Chapter IV**: Experiments & Results currently contains headings only.
- **Avoid unsupported critic claims**: current outline says `constant baseline (or critic)` and baseline ablation with critic. The current code uses normalized returns, not an actor-critic method.
- **Use actual code terms**: write `REINFORCE`, `PolicyNetwork`, `CartPole-v1`, `Categorical`, `log_prob`, `discounted returns`, and `normalized returns` consistently.
- **State solved evidence carefully**: current run achieves `mean_last_100 = 476.0000`, above the CartPole-v1 threshold 475, with seed/config shown below.

### Medium-priority polish

- **Fix grammar and spacing**: examples include `leaning rate` -> `learning rate`, `back propagation` -> `backpropagation`, `para meterization` -> `parameterization`.
- **Use consistent capitalization**: `Policy Gradient`, `REINFORCE`, `PyTorch`, `Gymnasium`, `CartPole-v1`.
- **Add captions under all figures**: each caption should explain what the reader should observe.
- **Align report structure with actual scope**: no distributed training, no actor-critic, no extra environments.
- **Add repository link only when final repo URL is confirmed**.

## 2. Verified Evidence from Current Outputs

### Random baseline

Source: `outputs/baseline_20260510_011932/baseline_stats.txt`

| Metric             |       Value |
| ------------------ | ----------: |
| Environment        | CartPole-v1 |
| Episodes           |         100 |
| Mean reward        |     23.2800 |
| Standard deviation |     13.0791 |
| Minimum reward     |           9 |
| Maximum reward     |          88 |

Figure candidate:

- `outputs/baseline_20260510_011932/baseline_curve.png`
- Resolution: 1000 x 500 px

### Trained REINFORCE run

Source: `outputs/run_20260510_011946/`

| Field                 | Value       |
| --------------------- | ----------- |
| Environment           | CartPole-v1 |
| Episodes              | 1000        |
| Learning rate         | 0.001       |
| Discount factor gamma | 0.99        |
| Hidden dimension      | 128         |
| Seed                  | 123         |
| Device                | CPU         |

Metrics from `metrics.txt` and `rewards.txt`:

| Metric                          |                                            Value |
| ------------------------------- | -----------------------------------------------: |
| Mean reward, last 50 episodes   |                                         476.9400 |
| Std reward, last 50 episodes    |                                          57.6664 |
| Mean reward, last 100 episodes  |                                         476.0000 |
| Std reward, last 100 episodes   |                                          56.6927 |
| Mean reward, last 200 episodes  |                                         460.1500 |
| Best episode reward             |                                         500.0000 |
| Final episode reward            |                                         500.0000 |
| Last-100 min reward             |                                         286.0000 |
| Last-100 max reward             |                                         500.0000 |
| First 100-episode window >= 475 |                    Episode 752, average 475.6200 |
| Last 10 rewards                 | 326, 500, 500, 500, 500, 500, 500, 374, 500, 500 |

Figure candidate:

- `outputs/run_20260510_011946/training_curve.png`
- Resolution: 1000 x 500 px

Suggested claim:

> Under the configuration `lr=0.001`, `gamma=0.99`, `hidden_dim=128`, and `seed=123`, the REINFORCE agent reached a last-100-episode average reward of `476.00`, exceeding the standard CartPole-v1 solved threshold of `475`. The best and final episode rewards both reached `500`, while the last-100 reward range remained stochastic (`286` to `500`), which is expected for Monte Carlo policy-gradient training.

## 3. Technical Content Pack — Chapter III Methods

### 3.1 REINFORCE Algorithm

The project implements the REINFORCE algorithm, a Monte Carlo policy-gradient method that directly optimizes a stochastic policy. Instead of learning an action-value table and deriving a policy indirectly, REINFORCE parameterizes the policy as `pi_theta(a|s)` and updates the policy parameters in the direction that increases the probability of actions that produced high returns.

For each episode, the agent collects a trajectory of states, sampled actions, log-probabilities, and rewards. After the episode terminates, the algorithm computes the discounted return for each time step:

`G_t = R_t + gamma R_{t+1} + gamma^2 R_{t+2} + ...`

The implementation computes this value backward from the end of the episode, which reuses the future return already computed and keeps the computation linear in the episode length. The policy update is based on the loss:

`L(theta) = - sum_t log pi_theta(a_t | s_t) G_t`

The negative sign is required because PyTorch optimizers minimize a loss, while policy-gradient training aims to maximize expected return. Minimizing the negative log-probability weighted by return is therefore equivalent to performing gradient ascent on the expected reward objective.

The implementation also normalizes the returns within an episode:

`G_t <- (G_t - mean(G)) / (std(G) + epsilon)`

This normalization acts as a simple variance-reduction technique. It does not introduce a learned critic; instead, it stabilizes training by reducing the scale variation of Monte Carlo returns.

### 3.2 Environment Setup

The experiment uses `CartPole-v1` from Gymnasium. The state is a four-dimensional continuous vector containing cart position, cart velocity, pole angle, and pole angular velocity. The action space is discrete with two actions: push the cart left or push the cart right. The environment gives a reward of `+1` for every time step in which the pole remains balanced, and the maximum episode return is `500`.

This environment is suitable for the project because it is simple enough to connect the mathematical derivation to implementation, while still requiring sequential decision-making under uncertainty. It also has a standard solved criterion: an average reward of at least `475` over 100 consecutive episodes.

### 3.3 Policy Network Architecture

The policy is represented by a small multilayer perceptron implemented in PyTorch. The network receives the four-dimensional CartPole state as input, maps it through one hidden layer with a ReLU activation, and outputs a probability distribution over the two available actions using Softmax.

During training, the action is sampled from a `Categorical` distribution constructed from the output probabilities. This stochastic sampling is important because REINFORCE learns from sampled trajectories; using greedy action selection too early would reduce exploration and could trap the agent in a weak policy. During evaluation, the implementation uses the action with the highest probability to measure the learned policy more deterministically.

### 3.4 Training Pipeline

The training pipeline follows an episode-based loop. At the beginning of each run, the script creates the Gymnasium environment, initializes the policy network, configures the optimizer, and sets the random seed for reproducibility. For each episode, the agent repeatedly observes the current state, samples an action from the policy, applies the action to the environment, and stores the corresponding reward and log-probability.

After the episode ends, the algorithm computes discounted returns, normalizes them, builds the policy loss, and performs backpropagation through the saved log-probabilities. The run saves checkpoints, raw rewards, configuration, metrics, and the training curve under a timestamped output directory.

Suggested hyperparameter table:

| Hyperparameter        |       Value | Meaning                           |
| --------------------- | ----------: | --------------------------------- |
| Environment           | CartPole-v1 | Benchmark control task            |
| Episodes              |        1000 | Number of training episodes       |
| Learning rate         |       0.001 | Step size for optimizer           |
| Discount factor gamma |        0.99 | Weight assigned to future rewards |
| Hidden dimension      |         128 | Hidden units in policy network    |
| Seed                  |         123 | Reproducibility seed              |

## 4. Technical Content Pack — Chapter IV Experiments & Results

### 4.1 Experimental Setup

The experiments evaluate whether the REINFORCE implementation can learn a policy that balances the CartPole for a long duration. The random baseline is used to show the performance of an untrained policy, while the trained run measures the learning behavior of the policy-gradient agent.

The main training configuration uses `CartPole-v1`, 1000 episodes, learning rate `0.001`, discount factor `0.99`, hidden dimension `128`, and seed `123`. The performance is evaluated using episode rewards, moving-average reward trends, and the standard CartPole-v1 solved threshold of average reward `475` over 100 consecutive episodes.

### 4.2 Main Results

The random baseline achieved a mean reward of `23.28` over 100 episodes, with a maximum reward of `88`. This confirms that random actions cannot solve the task and provides a low-performance reference point for comparison.

The trained REINFORCE agent achieved a last-100-episode average reward of `476.00`, exceeding the standard CartPole-v1 solved threshold. The best episode reward and final episode reward both reached `500`, which is the maximum return of the environment. The first 100-episode window whose average reward exceeded `475` appeared at episode `752`, with an average reward of `475.62`.

These results show that the implementation successfully improves the policy from near-random behavior to a policy capable of solving CartPole-v1 under the selected configuration.

### 4.3 Discussion

The learning curve is expected to be noisy because REINFORCE is a Monte Carlo policy-gradient algorithm. Each update depends on sampled trajectories, and the return can vary significantly across episodes even after the policy becomes strong. This behavior appears in the last 100 episodes: rewards range from `286` to `500`, while the average remains above the solved threshold.

The results are consistent with the Policy Gradient Theorem. Actions that lead to higher returns receive larger positive reinforcement through the term `log pi_theta(a_t|s_t) G_t`, increasing their probability in similar future states. Return normalization helps reduce training variance and makes optimization more stable, but it does not remove all stochastic fluctuations.

### 4.4 Suggested Figures and Captions

- **Figure 1. Random baseline reward curve on CartPole-v1.** This figure shows the reward obtained by a random policy over 100 episodes. The low mean reward indicates that random actions are insufficient to keep the pole balanced.
- **Figure 2. REINFORCE training curve over 1000 episodes.** This figure shows how the episode reward improves during training. The moving average increases toward the maximum return, indicating that the policy learns to balance the pole.
- **Table 1. Hyperparameter configuration.** This table reports the training settings used for the main experiment.
- **Table 2. Baseline versus trained policy performance.** This table compares the random baseline and the trained REINFORCE policy using mean reward and maximum reward.

Suggested comparison table:

| Method                   | Episodes |           Mean reward | Best/Max reward | Note                         |
| ------------------------ | -------: | --------------------: | --------------: | ---------------------------- |
| Random baseline          |      100 |               23.2800 |              88 | Untrained policy             |
| REINFORCE trained policy |     1000 | 476.0000 last-100 avg |             500 | Solves CartPole-v1 threshold |

## 5. Full Report Completion Plan

### Quỳnh — Report Lead

- **Fix formatting leftovers**: List of Figures, placeholders, contribution percentage table.
- **Paste and adapt Chapter III/IV content**: use the technical content above, then rewrite in her own style.
- **Insert figures**: baseline curve and training curve.
- **Update captions and table numbering**.
- **Ensure final PDF has no placeholders**.

### Thanh — Code Lead

- **Provide final evidence**: output paths, hyperparameters, metrics, and figure files.
- **Confirm method wording**: normalized returns, not critic.
- **Check all claims against actual code**.
- **Optionally run a final evaluation command** if the team wants separate evaluation stats from `best_policy.pth`.

### Sơn — Math Lead

- **Complete missing math subsections**: value function, policy parameterization, stochastic policy, Softmax, variance, baseline theorem, advantage function.
- **Check symbols**: make notation consistent across Chapter II and III.
- **Ensure the proof connects to code**: `log_prob`, `G_t`, and policy update.

### Đức Ý — Supporter

- **Proofread formatting**: page numbering, headings, tables, figure references.
- **Check references**: make sure every citation appears in the reference list.
- **Check final PDF**: no broken equations or missing images.

## 6. Recommended Next Actions

1. Quỳnh fixes obvious placeholders and unrelated figures first.
2. Thanh gives Quỳnh the metrics and figure files listed above.
3. Sơn completes the missing theory sections before the final writing pass.
4. Quỳnh integrates Chapter III/IV content, then exports PDF.
5. Thanh performs one final claim-vs-code review before submission.

## 7. Open Questions Before Final Submission

- What is the final public repository URL to put in the Abstract?
- What contribution percentages should be listed?
- Does the instructor require Vietnamese or English report style? The current report is English.
- Should the report include final evaluation stats from `scripts/evaluate.py`, or is training evidence enough?
- Does the team want to keep ablation studies, or simplify them because the current report/code evidence mainly supports one final configuration plus baseline?
