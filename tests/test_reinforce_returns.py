import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = PROJECT_ROOT / "sources"
if str(SOURCE_DIR) not in sys.path:
    sys.path.insert(0, str(SOURCE_DIR))

from reinforce import compute_returns


def test_compute_returns_discounted_reward_to_go():
    returns = compute_returns([1.0, 1.0, 1.0], gamma=0.99)

    assert returns == pytest.approx([2.9701, 1.99, 1.0])


def test_compute_returns_handles_single_reward():
    returns = compute_returns([5.0], gamma=0.99)

    assert returns == [5.0]


def test_compute_returns_handles_empty_episode():
    returns = compute_returns([], gamma=0.99)

    assert returns == []
