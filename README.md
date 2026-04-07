# [CS115] Policy Gradient for Reinforcement Learning (RL) - Team 05

[![GitHub Projects](https://img.shields.io/badge/Project-Tracking-blue?logo=github)](https://github.com/users/uit-25730067-chithanh/projects/1)
![Python](https://img.shields.io/badge/Python-3.9+-yellow?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red?logo=pytorch)
![Gymnasium](https://img.shields.io/badge/Gymnasium-RL-green)

This project explores the mathematical foundations and practical implementation of **Policy Gradient** methods, specifically the **REINFORCE** algorithm, applied to classic control problems from the `Gymnasium` library.

---

## 📐 Mathematical Core: The Policy Gradient Theorem

Our main objective is to optimize the expected reward $J(\theta)$ by adjusting the parameters $\theta$ of a stochastic policy $\pi_{\theta}(a|s)$.

### Key Formula:
$$ \nabla_{\theta} J(\theta) = \mathbb{E}_{\pi_{\theta}} \left[ \sum_{t=0}^{T} \nabla_{\theta} \log \pi_{\theta}(a_t|s_t) \hat{A}_t \right] $$

Where:
- $\pi_{\theta}(a_t|s_t)$: Probability of taking action $a_t$ in state $s_t$.
- $\hat{A}_t$: Advantage estimate or cumulative reward (Return $G_t$).
- **Log-derivative Trick**: $\nabla_{\theta} \pi_{\theta}(a|s) = \pi_{\theta}(a|s) \nabla_{\theta} \log \pi_{\theta}(a|s)$.

---

## 🛠 Project Structure (WBS)

| Module | Focus | Lead |
| :--- | :--- | :--- |
| **Math** | Proof of PG theorem, Log-derivative trick, LaTeX docs | Anh Sơn, Anh Ý |
| **Code** | Gymnasium Env, PyTorch Policy Network, REINFORCE | Anh Ý, Quỳnh |
| **Review** | Hyperparameter tuning, Analytics, Report synthesis | Quỳnh, Anh Sơn |

---

## 📂 Repository Organization

- `math/`: LaTeX sources and mathematical derivations.
- `sources/`: Core implementation of RL agent and network architectures.
- `reports/`: Weekly updates and experimental analysis.
- `scripts/`: Helper scripts for training and visualization.
- `data/`: Model checkpoints and training logs.

---

## 📅 Action Plan: Week 3 (Kick-off)

- [x] Repository initialization & Git setup.
- [x] Initial project planning & WBS.
- [ ] Research: "Reinforce Algorithm" for discrete action spaces.
- [ ] Baseline: Implementation of `CartPole-v1` with random actions.

---

## 🤝 Team 05 - Charter
- **Response Time**: 12-24 hours.
- **Commitment**: No copy-pasting code without understanding. 
- **Tooling**: GitHub Projects for tracking, Python for core logic, LaTeX for reporting.

---

© 2026 CS115 - University of Information Technology (UIT)
