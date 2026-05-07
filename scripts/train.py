import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = PROJECT_ROOT / "sources"
if str(SOURCE_DIR) not in sys.path:
    sys.path.insert(0, str(SOURCE_DIR))

from train import plot_learning_curve, train_reinforce


def parse_args():
    parser = argparse.ArgumentParser(description="Train REINFORCE on a Gymnasium environment.")
    parser.add_argument("--env", default="CartPole-v1")
    parser.add_argument("--episodes", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--gamma", type=float, default=0.99)
    parser.add_argument("--hidden-dim", type=int, default=128)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--save-dir", default=None)
    return parser.parse_args()


def main():
    args = parse_args()
    save_dir = args.save_dir
    if save_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_dir = str(PROJECT_ROOT / "outputs" / f"run_{timestamp}")

    rewards = train_reinforce(
        env_name=args.env,
        max_episodes=args.episodes,
        lr=args.lr,
        gamma=args.gamma,
        hidden_dim=args.hidden_dim,
        seed=args.seed,
        save_dir=save_dir,
    )

    plot_learning_curve(rewards, save_path=os.path.join(save_dir, "training_curve.png"))
    print(f"Training outputs saved to: {save_dir}")


if __name__ == "__main__":
    main()
