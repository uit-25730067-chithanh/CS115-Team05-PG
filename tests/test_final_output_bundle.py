import sys
from pathlib import Path

import torch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = PROJECT_ROOT / "sources"
if str(SOURCE_DIR) not in sys.path:
    sys.path.insert(0, str(SOURCE_DIR))

from models.policy import PolicyNetwork


FINAL_RUN_DIR = PROJECT_ROOT / "outputs" / "final" / "reinforce-cartpole-v1"
FINAL_EVAL_DIR = PROJECT_ROOT / "outputs" / "final" / "evaluation"
BASELINE_DIR = PROJECT_ROOT / "outputs" / "final" / "random-baseline"


def read_config(path):
    config = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        config[key.strip()] = value.strip()
    return config


def test_final_output_bundle_has_expected_files():
    expected_paths = [
        FINAL_RUN_DIR / "best_policy.pth",
        FINAL_RUN_DIR / "final_policy.pth",
        FINAL_RUN_DIR / "training_curve.png",
        FINAL_RUN_DIR / "metrics.txt",
        FINAL_RUN_DIR / "rewards.txt",
        FINAL_RUN_DIR / "run_config.txt",
        FINAL_EVAL_DIR / "eval_stats.txt",
        FINAL_EVAL_DIR / "eval_log.txt",
        BASELINE_DIR / "baseline_curve.png",
        BASELINE_DIR / "baseline_stats.txt",
        BASELINE_DIR / "baseline_log.txt",
    ]

    for path in expected_paths:
        assert path.exists(), f"Missing final output artifact: {path}"


def test_final_checkpoint_matches_recorded_hidden_dim():
    config = read_config(FINAL_RUN_DIR / "run_config.txt")

    assert config["env"] == "CartPole-v1"
    assert config["hidden_dim"] == "128"

    policy = PolicyNetwork(state_dim=4, action_dim=2, hidden_dim=128)
    state_dict = torch.load(
        FINAL_RUN_DIR / "best_policy.pth",
        map_location=torch.device("cpu"),
        weights_only=True,
    )
    policy.load_state_dict(state_dict)
