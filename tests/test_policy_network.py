import sys
from pathlib import Path

import torch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = PROJECT_ROOT / "sources"
if str(SOURCE_DIR) not in sys.path:
    sys.path.insert(0, str(SOURCE_DIR))

from models.policy import PolicyNetwork


def test_policy_network_returns_valid_action_distribution():
    policy = PolicyNetwork(state_dim=4, action_dim=2, hidden_dim=8)
    state = torch.zeros((1, 4), dtype=torch.float32)

    probabilities = policy(state)

    assert probabilities.shape == (1, 2)
    assert torch.all(probabilities >= 0)
    assert torch.allclose(probabilities.sum(dim=-1), torch.ones(1), atol=1e-6)


def test_select_action_returns_cartpole_action_and_log_probability():
    torch.manual_seed(123)
    policy = PolicyNetwork(state_dim=4, action_dim=2, hidden_dim=8)
    state = torch.zeros(4).numpy()

    action, log_prob = policy.select_action(state)

    assert action in {0, 1}
    assert log_prob.ndim == 1
    assert torch.isfinite(log_prob).all()
