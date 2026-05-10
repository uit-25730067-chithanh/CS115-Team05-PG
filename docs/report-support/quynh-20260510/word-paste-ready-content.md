# Word Paste-Ready Content

## ABSTRACT — replacement suggestion

In this project, we study Policy Gradient methods in reinforcement learning, with a focus on connecting mathematical foundations to a practical implementation. The main objective is to derive the key ideas behind the Policy Gradient Theorem and implement the REINFORCE algorithm for the CartPole-v1 control problem. The system is implemented in PyTorch and uses Gymnasium for environment simulation. The agent learns from complete episodes by sampling actions from a stochastic policy, computing discounted returns, and updating the policy parameters through gradient-based optimization.

The experimental results show that the implemented REINFORCE agent can improve significantly over a random baseline. In the latest training run, the agent achieved a last-100-episode average reward of 476.00, exceeding the standard CartPole-v1 solved threshold of 475. The best and final episode rewards both reached the maximum value of 500. These results demonstrate how mathematical concepts such as stochastic policies, the log-derivative trick, Monte Carlo returns, and policy-gradient optimization can be translated into a working reinforcement learning pipeline.

## Chapter III. METHODS

### 3.1. REINFORCE Algorithm

This project implements the REINFORCE algorithm, a Monte Carlo policy-gradient method that directly optimizes a stochastic policy. Instead of estimating an action-value function and deriving a policy indirectly, REINFORCE represents the policy as a parameterized probability distribution \(\pi_\theta(a|s)\). The policy receives a state as input and outputs the probability of selecting each possible action. The parameters \(\theta\) are updated so that actions that lead to higher returns become more likely in similar future states.

For each episode, the agent collects a trajectory consisting of states, sampled actions, action log-probabilities, and rewards. After the episode terminates, the algorithm computes the discounted return for each time step:

\[
G_t = R_t + \gamma R_{t+1} + \gamma^2 R_{t+2} + \cdots
\]

The implementation computes these returns backward from the end of the episode. This is efficient because each return reuses the future return already computed at the next time step. The policy update is based on the REINFORCE objective:

\[
\nabla_\theta J(\theta) \approx \sum_t \nabla_\theta \log \pi_\theta(a_t|s_t)G_t
\]

In implementation, PyTorch optimizers minimize a loss function. Therefore, the training code uses the following loss:

\[
L(\theta) = -\sum_t \log \pi_\theta(a_t|s_t)G_t
\]

The negative sign converts the maximization of expected return into a minimization problem. Minimizing this loss is equivalent to increasing the log-probability of actions that produced higher returns.

The implementation also normalizes the returns within each episode:

\[
G_t \leftarrow \frac{G_t - \mu(G)}{\sigma(G) + \epsilon}
\]

This normalization acts as a simple variance-reduction technique. It stabilizes training by reducing the scale variation of Monte Carlo returns. The project does not implement a separate critic network; the variance reduction comes from normalized returns only.

### 3.2. Environment Setup

The experiment uses CartPole-v1 from Gymnasium. CartPole-v1 is a classic control environment in which an agent must move a cart left or right to keep a pole balanced. The state is a four-dimensional continuous vector:

| State variable | Meaning |
| --- | --- |
| Cart position | Horizontal position of the cart |
| Cart velocity | Horizontal velocity of the cart |
| Pole angle | Angle of the pole from the vertical axis |
| Pole angular velocity | Angular velocity of the pole |

The action space is discrete and contains two actions:

| Action | Meaning |
| --- | --- |
| 0 | Push the cart to the left |
| 1 | Push the cart to the right |

The environment gives a reward of +1 for every time step in which the pole remains balanced. An episode terminates when the pole angle or cart position exceeds the allowed threshold, or when the episode reaches the maximum length. The maximum return for one episode is 500. The standard CartPole-v1 solved criterion is an average reward of at least 475 over 100 consecutive episodes.

CartPole-v1 is suitable for this project because it is simple enough to support mathematical analysis while still requiring sequential decision-making under uncertainty. Its low-dimensional state space and discrete action space make the connection between the Policy Gradient formula and the code implementation clear.

### 3.3. Policy Network Architecture

The policy is represented by a small multilayer perceptron implemented in PyTorch. The network receives the four-dimensional CartPole state as input, applies one hidden layer with a ReLU activation function, and outputs a probability distribution over the two possible actions using Softmax.

The architecture is summarized as follows:

| Component | Description |
| --- | --- |
| Input layer | Four CartPole state variables |
| Hidden layer | Fully connected layer with ReLU activation |
| Output layer | Two action scores |
| Softmax | Converts action scores into action probabilities |

During training, the agent samples an action from a categorical distribution created from the output probabilities. This stochastic action selection is important because REINFORCE learns from sampled trajectories. If the agent always selected the action with the highest probability during training, exploration would be reduced and the policy could become stuck in a weak behavior. During evaluation, the implementation uses the action with the highest probability to measure the learned policy more deterministically.

### 3.4. Training Pipeline

The training pipeline follows an episode-based loop. At the beginning of each run, the script creates the Gymnasium environment, initializes the policy network, configures the optimizer, and sets the random seed for reproducibility. During each episode, the agent observes the current state, samples an action from the policy, applies the action to the environment, and stores the reward and log-probability of the selected action.

After the episode ends, the algorithm computes discounted returns, normalizes them, builds the policy loss, and performs backpropagation through the saved log-probabilities. The optimizer then updates the policy network parameters. The run also saves checkpoints, raw rewards, configuration files, metrics, and the training curve into a timestamped output directory.

The main training configuration used for the final experiment is shown below:

| Hyperparameter | Value | Description |
| --- | ---: | --- |
| Environment | CartPole-v1 | Benchmark control task |
| Number of episodes | 1000 | Total training episodes |
| Learning rate | 0.001 | Optimizer step size |
| Discount factor \(\gamma\) | 0.99 | Weight assigned to future rewards |
| Hidden dimension | 128 | Number of hidden units in the policy network |
| Seed | 123 | Reproducibility seed |
| Device | CPU | Hardware used for the recorded run |

## Chapter IV. EXPERIMENTS & RESULTS

### 4.1. Experimental Setup

The experiments evaluate whether the REINFORCE implementation can learn a policy that balances the CartPole for a long duration. A random baseline is used as the reference performance of an untrained policy. The trained REINFORCE run is then compared against this baseline using episode rewards and moving-average reward trends.

The main experiment uses CartPole-v1, 1000 training episodes, learning rate 0.001, discount factor 0.99, hidden dimension 128, and seed 123. Performance is evaluated using the reward obtained in each episode, the average reward over recent episodes, the best episode reward, and the standard CartPole-v1 solved threshold of 475 average reward over 100 consecutive episodes.

### 4.2. Random Baseline

The random baseline runs the environment with actions selected randomly. This baseline provides a reference point for understanding how difficult the task is without learning. Over 100 episodes, the random baseline achieved the following results:

| Metric | Value |
| --- | ---: |
| Environment | CartPole-v1 |
| Episodes | 100 |
| Mean reward | 23.2800 |
| Standard deviation | 13.0791 |
| Minimum reward | 9 |
| Maximum reward | 88 |

The low mean reward shows that random actions cannot keep the pole balanced for a long time. This confirms that learning is necessary to solve the task.

Suggested figure caption:

Figure 1. Random baseline reward curve on CartPole-v1. The random policy receives low and unstable rewards, showing that random action selection is insufficient for solving the environment.

Figure file:

`outputs/baseline_20260510_011932/baseline_curve.png`

### 4.3. REINFORCE Training Results

The trained REINFORCE agent shows a large improvement over the random baseline. The latest recorded training run used 1000 episodes and achieved a last-100-episode average reward of 476.00, which exceeds the standard CartPole-v1 solved threshold of 475. The best episode reward and the final episode reward both reached 500, the maximum possible return in CartPole-v1.

| Metric | Value |
| --- | ---: |
| Total training episodes | 1000 |
| Mean reward over last 50 episodes | 476.9400 |
| Standard deviation over last 50 episodes | 57.6664 |
| Mean reward over last 100 episodes | 476.0000 |
| Standard deviation over last 100 episodes | 56.6927 |
| Mean reward over last 200 episodes | 460.1500 |
| Best episode reward | 500.0000 |
| Final episode reward | 500.0000 |
| First 100-episode window above 475 | Episode 752, average 475.6200 |

These results indicate that the implemented REINFORCE algorithm successfully learns a policy that can solve CartPole-v1 under the selected configuration.

Suggested figure caption:

Figure 2. REINFORCE training curve over 1000 episodes. The episode reward is noisy because the policy is stochastic, but the moving-average trend increases toward the maximum reward, indicating successful learning.

Figure file:

`outputs/run_20260510_011946/training_curve.png`

### 4.4. Baseline vs Trained Policy Comparison

The comparison between the random baseline and the trained REINFORCE agent demonstrates the effect of policy-gradient learning. The random baseline achieved a mean reward of only 23.28, while the trained agent reached a last-100-episode average reward of 476.00.

| Method | Episodes | Main metric | Best reward | Interpretation |
| --- | ---: | ---: | ---: | --- |
| Random baseline | 100 | Mean reward = 23.2800 | 88 | Untrained behavior |
| REINFORCE trained policy | 1000 | Last-100 average = 476.0000 | 500 | Solves CartPole-v1 threshold |

The trained policy is therefore much more effective than random action selection. This supports the theoretical expectation of the Policy Gradient method: actions that lead to higher returns are reinforced through the gradient update, increasing their probability in similar future states.

### 4.5. Discussion

The learning curve remains noisy even after the agent becomes strong. This is expected because REINFORCE is a Monte Carlo policy-gradient algorithm. Each update depends on sampled trajectories, and the reward may vary from episode to episode due to stochastic action sampling and environment dynamics. In the last 100 episodes, rewards ranged from 286 to 500, but the average reward remained above the solved threshold.

The results are consistent with the Policy Gradient Theorem. The term \(\log \pi_\theta(a_t|s_t)G_t\) increases the probability of actions that appear in high-return trajectories and decreases the relative probability of actions associated with lower returns. Return normalization helps reduce the variance of the update and improves training stability, but it does not remove all stochastic fluctuation.

### 4.6. Conclusion

This project successfully connects the mathematical foundation of Policy Gradient methods with a practical REINFORCE implementation. The agent starts from near-random behavior and learns a policy that solves CartPole-v1 under the recorded configuration. The experiment demonstrates how stochastic policies, discounted returns, the log-derivative trick, and gradient-based optimization work together in a complete reinforcement learning pipeline.

## Optional: revised List of Figures and Tables

LIST OF FIGURES AND TABLES

Figure 1. Random baseline reward curve on CartPole-v1

Figure 2. REINFORCE training curve over 1000 episodes

Table 1. CartPole-v1 state variables

Table 2. CartPole-v1 action space

Table 3. Main training hyperparameter configuration

Table 4. Random baseline performance

Table 5. REINFORCE training performance

Table 6. Baseline versus trained policy comparison
