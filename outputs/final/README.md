# Final Output Bundle

This folder keeps the selected evidence artifacts for the public repository.
Timestamped development runs are generated artifacts and are ignored by git.

## Contents

| Path | Purpose |
| --- | --- |
| `reinforce-cartpole-v1/` | Selected REINFORCE training run for CartPole-v1 |
| `random-baseline/` | Selected random policy baseline |
| `evaluation/` | Greedy-policy evaluation for the selected checkpoint |

## Selected Training Run

- Environment: `CartPole-v1`
- Episodes: `1000`
- Learning rate: `0.001`
- Gamma: `0.99`
- Hidden dimension: `128`
- Seed: `123`
- Mean reward over final 50 episodes: `476.94`
- Best reward: `500.00`
- Final reward: `500.00`

Evaluate the selected checkpoint:

```bash
python3 scripts/evaluate.py \
  --checkpoint outputs/final/reinforce-cartpole-v1/best_policy.pth \
  --episodes 10 \
  --hidden-dim 128
```
