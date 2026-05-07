import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

import gymnasium as gym
import numpy as np
import torch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = PROJECT_ROOT / "sources"
if str(SOURCE_DIR) not in sys.path:
    sys.path.insert(0, str(SOURCE_DIR))

from models.policy import PolicyNetwork


def positive_int(value):
    parsed_value = int(value)
    if parsed_value < 1:
        raise argparse.ArgumentTypeError("value must be at least 1")
    return parsed_value


def parse_args():
    parser = argparse.ArgumentParser(description="Evaluate a trained REINFORCE policy.")
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--env", default="CartPole-v1")
    parser.add_argument("--episodes", type=positive_int, default=10)
    parser.add_argument("--hidden-dim", type=int, default=128)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--save-dir", default=None)
    return parser.parse_args()


def select_device():
    if torch.backends.mps.is_available():
        return torch.device("mps")
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def write_evaluation_outputs(save_dir, rewards, args, device):
    stats_path = os.path.join(save_dir, "eval_stats.txt")
    log_path = os.path.join(save_dir, "eval_log.txt")
    mean_reward = float(np.mean(rewards)) if rewards else 0.0
    std_reward = float(np.std(rewards)) if rewards else 0.0
    best_reward = float(np.max(rewards)) if rewards else 0.0
    worst_reward = float(np.min(rewards)) if rewards else 0.0

    with open(log_path, "w", encoding="utf-8") as f:
        for episode, reward in enumerate(rewards, start=1):
            f.write(f"{episode}\t{reward}\n")

    with open(stats_path, "w", encoding="utf-8") as f:
        f.write(f"checkpoint: {args.checkpoint}\n")
        f.write(f"env: {args.env}\n")
        f.write(f"episodes: {args.episodes}\n")
        f.write(f"hidden_dim: {args.hidden_dim}\n")
        f.write(f"seed: {args.seed}\n")
        f.write(f"device: {device}\n")
        f.write(f"mean_reward: {mean_reward:.4f}\n")
        f.write(f"std_reward: {std_reward:.4f}\n")
        f.write(f"best_reward: {best_reward:.4f}\n")
        f.write(f"worst_reward: {worst_reward:.4f}\n")


def main():
    args = parse_args()
    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    if args.save_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_dir = PROJECT_ROOT / "outputs" / f"eval_{timestamp}"
    else:
        save_dir = Path(args.save_dir)
    save_dir.mkdir(parents=True, exist_ok=True)

    device = select_device()
    env = gym.make(args.env)
    if hasattr(env.action_space, "seed"):
        env.action_space.seed(args.seed)

    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.n
    policy_net = PolicyNetwork(state_dim, action_dim, hidden_dim=args.hidden_dim).to(device)
    policy_net.load_state_dict(torch.load(args.checkpoint, map_location=device))
    policy_net.eval()

    rewards = []
    with torch.no_grad():
        for episode in range(1, args.episodes + 1):
            if episode == 1:
                state, _ = env.reset(seed=args.seed)
            else:
                state, _ = env.reset()

            done = False
            truncated = False
            total_reward = 0.0

            while not (done or truncated):
                state_tensor = torch.from_numpy(state).float().unsqueeze(0).to(device)
                probs = policy_net(state_tensor)
                action = torch.argmax(probs, dim=-1).item()
                state, reward, done, truncated, _ = env.step(action)
                total_reward += reward

            rewards.append(total_reward)

    env.close()
    write_evaluation_outputs(str(save_dir), rewards, args, device)
    print(f"Evaluation outputs saved to: {save_dir}")
    mean_reward = float(np.mean(rewards)) if rewards else 0.0
    print(f"Mean reward: {mean_reward:.2f}")


if __name__ == "__main__":
    main()
