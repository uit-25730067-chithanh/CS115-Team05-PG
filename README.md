# [CS115] Policy Gradient for Reinforcement Learning (RL) - Team 05

[![GitHub Projects](https://img.shields.io/badge/Project-Tracking-blue?logo=github)](https://github.com/users/uit-25730067-chithanh/projects/1)
![Python](https://img.shields.io/badge/Python-3.9+-yellow?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red?logo=pytorch)
![Gymnasium](https://img.shields.io/badge/Gymnasium-RL-green)

Explore math foundations & practical implementation of **Policy Gradient** (REINFORCE algorithm) on classic control problems using `Gymnasium`.

> Course: _CS115 - Math for Computer Science_ | University of Information Technology (UIT)

---

## 👥 Team 05

| ID       | Name               | Role                    | Support              | GitHub                                                             |
| :------- | :----------------- | :---------------------- | :------------------- | :----------------------------------------------------------------- |
| 25730067 | Đặng Chí Thanh     | Team Leader & Code Lead | All                  | [@uit-25730067-chithanh](https://github.com/uit-25730067-chithanh) |
| 25730061 | Hoàng Cao Sơn      | Math Lead               | Code & Report        | [@uit-25730061-caoson](https://github.com/uit-25730061-caoson)     |
| 26210070 | Phạm Vũ Xuân Quỳnh | Report Lead             | Admin & Code Support | [@xuanquynhphamvu](https://github.com/xuanquynhphamvu)             |
| 25730094 | Nguyễn Đức Ý       | Supporter               | General              | [@ducy11](https://github.com/ducy11)                               |

---

## 🗺️ Roadmap & Progress

The project is currently in the parallel implementation phase of Math & Code (Week 04).

| Phase       | Main Content           | Status               |
| :---------- | :--------------------- | :------------------- |
| **Phase 1** | Math proof & Env setup | In Progress          |
| **Phase 2** | Policy Net & REINFORCE | Completed (Refining) |
| **Phase 3** | Training & Tuning      | Upcoming             |

🚀 View detailed roadmap and Gantt chart at: **[docs/project-roadmap.md](./docs/project-roadmap.md)**

---

## 🦴 4 Core Pillars

### 1. Math Core

- **Objective Function** $J(\theta)$: Expected total reward.
- **Log-derivative Trick**: Transform gradient to computable form.
- **Gradient Ascent**: Maximize probability of high-reward actions.

### 2. Environment (Gymnasium)

- **Problem**: `CartPole-v1` (balance the pole).
- **Loop**: State → Action → Reward.

### 3. Policy Network (PyTorch)

- **Arch**: Simple DNN.
- **Input**: Environment states → **Output**: Action probability distribution.

### 4. Training & Analytics

- Episode-based trajectory collection.
- Backprop with reward-weighted loss.
- Learning curve visualization.

---

## 🚀 Usage

For detailed instructions on environment setup and training the REINFORCE algorithm, please refer to our:

👉 **[Installation & Usage Guide](./docs/installation.md)**

---

## 📄 Report

### For Lecturer

Access our final report here: _Will be updated when project is completed._

### For Team Members

Access our working report here: [**Policy Gradient Project Report**](https://bit.ly/cs115-team05-report)

> **Note:** To view the report with correct formatting (no broken math equations), please use one of these two options:
> - **Open with Microsoft Word software** — renders 100% correctly and allows comment directly.
> - **If using Word on web**, export to PDF to read → go back to the relevant section on the web version and leave comment there (if needed).
---

## 📐 Policy Gradient Theorem

Optimize expected reward $J(\theta)$ by adjusting parameters $\theta$ of stochastic policy $\pi_{\theta}(a|s)$.

$$
\nabla_{\theta} J(\theta) = \mathbb{E}_{\pi_{\theta}} \left[ \sum_{t=0}^{T} \nabla_{\theta} \log \pi_{\theta}(a_t|s_t) \hat{A}_t \right]
$$

- $\pi_{\theta}(a_t|s_t)$: Prob of action $a_t$ in state $s_t$.
- $\hat{A}_t$: Advantage estimate or cumulative return $G_t$.
- **Log-derivative Trick**: $\nabla_{\theta} \pi_{\theta}(a|s) = \pi_{\theta}(a|s) \nabla_{\theta} \log \pi_{\theta}(a|s)$.

---

## 🛠 Work Breakdown Structure (WBS Summary)

| Module     | Owner              | Support       |
| :--------- | :----------------- | :------------ |
| **Math**   | Hoàng Cao Sơn      | Chí Thanh     |
| **Code**   | Đặng Chí Thanh     | Hoàng Cao Sơn |
| **Report** | Phạm Vũ Xuân Quỳnh | Chí Thanh     |

---

## 🤝 Team Charter (v3.0 Summary)

- **Comms**: MS Teams (primary) | Zalo (urgent only).
- **SLA**: 12-24h response. Quiet hours: 23h-07h & 18h30-21h.
- **Sprint deadline**: 23:00 Sun weekly.
- **AI policy**: Reference only, no copy-paste. Rephrase in own words.
- **Quality**: "Logic Explanation" — owner must explain logic to reviewer.
- **Conflict**: Direct dialogue → 15min meeting → Leader decides.
- **Goal**: A+ (9.0-10.0). Learn for real, no shortcuts.

---

## 📤 Submission (Semester)

### Final Project (Deadline: Jul 1, 2026)

- **Opens:** Sat, May 30, 2026 (12:00 AM)
- **Due:** Wed, Jul 01, 2026 (11:59 PM)
- **Components:** Slides, demo/results, source code & data, report (optional), video (if no live presentation).
- **Format:** Single `.zip` → `ID_group.zip`. If >100MB, submit `.txt` with public Google Drive link.

---

© 2026 CS115 - University of Information Technology (UIT)
