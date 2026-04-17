# CS115: Policy Gradient for RL - Team 05

> Project Design Review (PDR) — Last updated: Apr 16, 2026

---

## Team

| ID       | Name               | Owner Role  | Support Role | Key Responsibility                                      |
| :------- | :----------------- | :---------- | :----------- | :------------------------------------------------------ |
| 25730067 | Đặng Chí Thanh     | Team Leader | All          | Coordinate, roadmap, conflict resolution, risk mgmt     |
| 25730061 | Hoàng Cao Sơn      | Math Lead   | Report       | PG proof → LaTeX → review report                        |
| 25730094 | Nguyễn Đức Ý       | Code Lead   | Math         | Gymnasium setup → PyTorch training → explain code logic |
| 26210070 | Phạm Vũ Xuân Quỳnh | Report Lead | Code         | Compile content → run experiments → review code         |

---

## 1. Math Focus

- **Foundation**: MDP (Markov Decision Process), Bellman Equation.
- **Proof**: Policy Gradient Theorem (Log-derivative trick).
- **Algorithm**: REINFORCE first, Actor-Critic if time permits.
- **Optimization**: Baseline subtraction to reduce variance.

## 2. Tech Stack

- **Language**: Python 3.9+.
- **Framework**: PyTorch 2.0+ (direct gradient access).
- **Environment**: Gymnasium (`CartPole-v1`).
- **Reporting**: Word for report drafts. LaTeX for math.

## 3. Teamwork & Git

- **Git flow**:
  - `main`: Clean code, finalized reports.
  - Feature branches → PR → code review → merge.
- **Ignore (leader pref)**: `CLAUDE.md`, `AGENTS.md`, `plans/` not pushed.
- **WBS**:
  - **Math**: Sơn (Lead) + Ý (Support). Prove PG, Log-derivative, write LaTeX.
  - **Code**: Ý (Lead) + Quỳnh (Support). Gymnasium setup, PyTorch training loop.
  - **Report**: Quỳnh (Lead) + Sơn (Support). Run experiments, compile report.
- **Tools**: GitHub Projects (Kanban), MS Teams (comms), Zalo (urgent).

## 4. Quality Control

- **"Logic Explanation"**: Owner explains 100% of their logic to reviewer before approval.
- **Deadline discipline**: Late once → 24h grace. Twice → warning. Three → escalate to instructor.
- **AI policy**: Reference/learning only. No direct copy-paste.

## 5. KPIs (Charter v3.0)

| Category             | Weight | Sub-KPI                      | Detail                                     |
| :------------------- | :----- | :--------------------------- | :----------------------------------------- |
| General Contribution | 40%    | Ideas & Solutions (20%)      | Min 1 adopted idea per member              |
|                      |        | Presence & Interaction (20%) | >80% meeting attendance + SLA compliance   |
| Task Completion      | 30%    | Deadline (15%)               | On-time delivery, no project bottleneck    |
|                      |        | Technical Quality (15%)      | Math correct, code runs, report formatted  |
| Collaboration        | 20%    | Logic Explanation (10%)      | Explain own work to ≥1 teammate            |
|                      |        | Review & Support (10%)       | Cross-review with actionable feedback      |
| Initiative           | 10%    | Improvement & Docs (10%)     | External research + optimization proposals |

## 6. Meeting Log

### Week 03 — Kick-off (Apr 6, 2026, 21:30-23:00)

- **Format**: Online (MS Teams). Facilitator: Thanh. Scribe: Quỳnh.
- **Decisions**:
  - WBS finalized (Math/Code/Report split).
  - Charter rules agreed: 12-24h response, limit AI copy-paste.
  - Roadmap approach instead of rigid targets to reduce pressure.
  - Evaluation criteria to be refined by leader.
- **Actions**:
  - All: Read & understand REINFORCE algorithm.
  - Thanh: Send detailed assignments by 21h Apr 7.
  - Thanh: Create GitHub Project board ✅.
  - Thanh: Setup repo structure ✅.

### Week 04 — Foundation Expansion (Apr 13, 2026, 21:30-22:30)

- **Format**: Online (MS Teams). Facilitator: Thanh. Scribe: Quỳnh.
- **Decisions**:
  - Report tool: Word.
  - Task mgmt: GitHub Kanban → comment on tickets for support.
  - Code: feature branches, PR before merge.
  - Weekly report deadline: 23:00 Sun.
  - Python 3.9, PyTorch 2.0.
- **Tickets assigned**:
  - [MATH-02/03] Read docs, prove formulas → Sơn (Support: Ý, Thanh).
  - [CODE-01/02] Setup environment → Ý (Support: Quỳnh, Thanh).
  - [RPT-01] Draft report framework → Quỳnh (Support: Sơn, Thanh).
  - All: Weekly progress report before 23h Sun.

## 7. Current Status (Week 04)

- **Phase**: 1 — Foundation (W3-W5).
- **On track**: Repo setup, WBS, Charter finalized.
- **In progress**: Math derivation, env setup, report framework.
- **Next meeting**: After Monday class, Week 05.
