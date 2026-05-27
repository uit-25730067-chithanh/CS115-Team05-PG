<div align="center">
  <img src="docs/assets/hero-banner.jpg" alt="Policy Gradient for RL Banner" width="100%" style="border-radius: 8px;">

# [CS115] Policy Gradient for Reinforcement Learning — Team 05

**University Project — Math for Computer Science (CS115)**  
 _Topic: Explore math foundations & practical implementation of REINFORCE on CartPole-v1._

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Gymnasium](https://img.shields.io/badge/Gymnasium-RL-green?style=for-the-badge)](https://gymnasium.farama.org/)
[![Course: CS115](https://img.shields.io/badge/Course-CS115%20Math%20for%20CS-blueviolet?style=for-the-badge)](https://www.uit.edu.vn/)
[![University: UIT](https://img.shields.io/badge/University-UIT%20VNU--HCM-orange?style=for-the-badge)](https://www.uit.edu.vn/)

</div>

<br/>

## Table of Contents

- [Course Context](#course-context)
- [Project Objectives](#project-objectives)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Academic Details](#academic-details)
  - [Roadmap & Progress](#roadmap--progress)
  - [The Math](#the-math)
  - [Work Breakdown Structure](#work-breakdown-structure)
  - [Team Charter](#team-charter)
  - [Report & Submission](#report--submission)

---

## Course Context

- **Course:** CS115 — Mathematics for Computer Science
- **Institution:** University of Information Technology (UIT), Vietnam National University — Ho Chi Minh City (VNU-HCM)
- **Instructor:** TS. Dương Việt Hằng (<hangdv@hcmuit.edu.vn>) — KHMT, UIT
- **Semester:** 2025–2026 (2nd Semester)

## Project Objectives

This project demonstrates the theoretical foundations and practical implementation of **Policy Gradient methods** in Reinforcement Learning. Specifically, we implement the **REINFORCE algorithm** to solve the `CartPole-v1` control problem via `PyTorch` and `Gymnasium`.

**Learning Outcomes:**

1. Derive the Policy Gradient Theorem from first principles.
2. Implement a stochastic policy network and train it with Monte-Carlo returns.
3. Analyze convergence behavior and visualize learning curves.
4. Document the full pipeline following academic software-engineering standards.

> **Full documentation** (system design, math proofs, team workflows):  
> See the **[Project Design Report (PDR)](./docs/project-overview-pdr.md)**.

---

## Tech Stack

| Category         | Technologies                                                                                                                                                                                      |
| :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Core ML / RL** | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white) ![Gymnasium](https://img.shields.io/badge/Gymnasium-008000?style=flat-square)              |
| **Math & Viz**   | ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square)                  |
| **Environment**  | ![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python&logoColor=white) ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) |

---

## Project Structure

```text
CS115-Team05-PG/
│
├── docs/                   # Project documentation (PDR, roadmap, architecture)
├── math/                   # LaTeX math proofs & derivations
├── reports/                # Weekly updates, meeting agendas, meeting minutes
├── scripts/                # Reproducible CLI entrypoints
│   ├── train.py            # Train REINFORCE with configurable seed/hyperparameters
│   ├── evaluate.py         # Evaluate a saved policy checkpoint
│   ├── run_experiments.py  # Compact hyperparameter grid runner
│   └── visualize.py        # Report-ready figure generation
├── sources/                # Core implementation
│   ├── models/             # Policy network (PyTorch)
│   ├── train.py            # Training loop implementation
│   ├── test_env.py         # Environment sanity check
│   └── reinforce.py        # REINFORCE algorithm core
│
└── outputs/                # Generated checkpoints, metrics, experiments and figures
```

> _For detailed team responsibilities, see the [Team Workflows](./docs/project-overview-pdr.md)._

---

## Getting Started

### 1. Prerequisites

- **Python 3.9+**
- **Git**

### 2. Installation

```bash
git clone <repository-url>
cd CS115-Team05-PG

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
# .\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Training

Run the reproducible training entrypoint:

```bash
python3 scripts/train.py --episodes 500 --seed 42 --hidden-dim 64
```

Trained policy weights, raw rewards, metrics and training curves will be saved to a timestamped subdirectory under `outputs/` (e.g., `outputs/run_YYYYMMDD_HHMMSS/`).

### 4. Evaluation

Evaluate a saved checkpoint:

```bash
python3 scripts/evaluate.py --checkpoint outputs/run_YYYYMMDD_HHMMSS/best_policy.pth --episodes 10 --hidden-dim 64
```

### 5. Test Environment

Verify the Gymnasium environment is working correctly:

```bash
python3 sources/test_env.py
```

---

## Academic Details

> The following sections contain mandatory deliverables and metadata required for **course assessment** (CS115).

---

### Roadmap & Progress

The project is currently in Week 07. The Code track has been completed ahead of schedule so the team can reserve more time for math explanation, report writing, demo preparation and final packaging.

| Phase       | Main Content                       | Status                  |
| :---------- | :--------------------------------- | :---------------------- |
| **Phase 1** | Math proof & Env setup             | Completed               |
| **Phase 2** | Policy Net & REINFORCE             | Completed               |
| **Phase 3** | Training, tuning & visualization   | Completed ahead of plan |
| **Phase 4** | Report, slides & final explanation | In progress             |

Completed code milestones include baseline evaluation, PolicyNetwork, REINFORCE training, reproducible train/evaluate entrypoints, compact hyperparameter tuning, report-ready visualization, and PR #40 for logic explanation.

View detailed Gantt chart at: **[docs/project-roadmap.md](./docs/project-roadmap.md)**

---

### The Math

Optimize expected reward $J(\theta)$ by adjusting parameters $\theta$ of stochastic policy $\pi_\theta(a_t \mid s_t)$.

$$
\nabla_\theta J(\theta)
= \mathbb{E}_{\tau \sim \pi_\theta}
\left[
\sum_{t=0}^{T}\nabla_\theta \log \pi_\theta(a_t \mid s_t)G_t
\right]
$$

- **$\pi_\theta(a_t \mid s_t)$**: Probability of action $a_t$ in state $s_t$.
- **$G_t$**: Reward-to-go, $G_t = \sum_{k=t}^{T}\gamma^{k-t}r_{k+1}$.
- **Log-derivative Trick**: $\nabla_\theta f(\theta) = f(\theta)\nabla_\theta \log f(\theta)$.

> _For the full derivation, see our [Project Design Report (PDR)](./docs/project-overview-pdr.md)._

---

### Work Breakdown Structure

| Module     | Owner              | Support        |
| :--------- | :----------------- | :------------- |
| **Math**   | Hoàng Cao Sơn      | Đặng Chí Thanh |
| **Code**   | Đặng Chí Thanh     | Hoàng Cao Sơn  |
| **Report** | Phạm Vũ Xuân Quỳnh | Đặng Chí Thanh |

---

### Team Charter (v3.0 Summary)

- **Comms**: MS Teams (primary) | Zalo (urgent only).
- **SLA**: 12-24h response. Quiet hours: 23h-07h & 18h30-21h.
- **Sprint deadline**: 23:00 Sun weekly.
- **AI policy**: Reference only, no copy-paste. Rephrase in own words.
- **Quality**: "Logic Explanation" — owner must explain logic to reviewer.
- **Conflict**: Direct dialogue → 15min meeting → Leader decides.
- **Goal**: A+ (9.0-10.0). Learn for real, no shortcuts.

### Team Roster — Team 05

| Student ID | Full Name          | Role                    | GitHub                                                             |
| :--------- | :----------------- | :---------------------- | :----------------------------------------------------------------- |
| 25730067   | Đặng Chí Thanh     | Team Leader & Code Lead | [@uit-25730067-chithanh](https://github.com/uit-25730067-chithanh) |
| 25730061   | Hoàng Cao Sơn      | Math Lead               | [@uit-25730061-caoson](https://github.com/uit-25730061-caoson)     |
| 26210070   | Phạm Vũ Xuân Quỳnh | Report Lead             | [@xuanquynhphamvu](https://github.com/xuanquynhphamvu)             |
| 25730094   | Nguyễn Đức Ý       | Supporter               | [@ducy11](https://github.com/ducy11)                               |

---

### Report & Submission

#### For Lecturer

Access our final report here: _Will be updated when project is completed._

#### For Team Members

Access our working report here: [**Policy Gradient Project Report**](https://bit.ly/cs115-team05-report)

> **Note:** To view the report with correct formatting (no broken math equations), please use one of these two options:
>
> - **Open with Microsoft Word software** — renders 100% correctly and allows comment directly.
> - **If using Word on web**, export to PDF to read → go back to the relevant section on the web version and leave comment there (if needed).

#### Submission (Semester)

- **Opens:** Sat, May 30, 2026 (12:00 AM)
- **Due:** Wed, Jul 01, 2026 (11:59 PM)
- **Components:** Slides, demo/results, source code & data, report (optional), video (if no live presentation)
- **Format:** Single `.zip` → `ID_group.zip`. If >100MB, submit `.txt` with public Google Drive link.

<br/>

<div align="center">
  <i>CS115 — Mathematics for Computer Science</i><br/>
  <i>University of Information Technology (UIT) · VNU-HCM · 2026</i>
</div>
