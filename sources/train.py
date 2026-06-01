import gymnasium as gym
import torch
import torch.optim as optim
import matplotlib
import numpy as np
import os

from datetime import datetime

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Sử dụng paths tương đối đối với module gốc
from models.policy import PolicyNetwork
from reinforce import compute_returns, update_policy

# Constants
DEFAULT_ENV = "CartPole-v1"      
DEFAULT_EPISODES = 1000          
DEFAULT_LR = 1e-3                # Learning rate cho optimizer
DEFAULT_GAMMA = 0.99             # Hệ số chiết khấu phần thưởng tương lai
DEFAULT_HIDDEN_DIM = 128         # Số neuron ẩn trong policy network
DEFAULT_SEED = 123               # Seed ngẫu nhiên; thực nghiệm cho thấy hội tụ ổn định với CartPole-v1

def _write_training_outputs(save_dir, config, episode_rewards, best_reward):
    rewards_path = os.path.join(save_dir, "rewards.txt")
    config_path = os.path.join(save_dir, "run_config.txt")
    metrics_path = os.path.join(save_dir, "metrics.txt")
    readme_path = os.path.join(save_dir, "README.txt")

    with open(rewards_path, "w", encoding="utf-8") as f:
        for episode, reward in enumerate(episode_rewards, start=1):
            f.write(f"{episode}\t{reward}\n")

    with open(config_path, "w", encoding="utf-8") as f:
        for key, value in config.items():
            f.write(f"{key}: {value}\n")

    last_rewards = episode_rewards[-50:]
    mean_last_50 = float(np.mean(last_rewards)) if last_rewards else 0.0
    std_last_50 = float(np.std(last_rewards)) if last_rewards else 0.0
    final_reward = episode_rewards[-1] if episode_rewards else 0.0
    best_value = best_reward if episode_rewards else 0.0

    with open(metrics_path, "w", encoding="utf-8") as f:
        f.write(f"mean_last_50: {mean_last_50:.4f}\n")
        f.write(f"std_last_50: {std_last_50:.4f}\n")
        f.write(f"best_reward: {best_value:.4f}\n")
        f.write(f"final_reward: {final_reward:.4f}\n")
        f.write(f"total_episodes: {len(episode_rewards)}\n")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(f"REINFORCE Training Run\n")
        f.write(f"======================\n\n")
        f.write(f"Environment: {config['env']}\n")
        f.write(f"Seed: {config['seed']}\n")
        f.write(f"Episodes: {config['episodes']}\n")
        f.write(f"Learning Rate: {config['lr']}\n")
        f.write(f"Gamma: {config['gamma']}\n")
        f.write(f"Hidden Dim: {config['hidden_dim']}\n")
        f.write(f"Device: {config['device']}\n\n")
        f.write(f"Results:\n")
        f.write(f"- Mean (last 50): {mean_last_50:.2f}\n")
        f.write(f"- Std (last 50): {std_last_50:.2f}\n")
        f.write(f"- Best Reward: {best_value:.2f}\n")
        f.write(f"- Final Reward: {final_reward:.2f}\n")

def train_reinforce(env_name=DEFAULT_ENV, max_episodes=DEFAULT_EPISODES, lr=DEFAULT_LR, gamma=DEFAULT_GAMMA, hidden_dim=DEFAULT_HIDDEN_DIM, seed=DEFAULT_SEED, save_dir=None):
    # Nếu không cung cấp save_dir, tự động tạo thư mục timestamp trong 'outputs/'
    # để tránh xung đột với package 'models' của dự án.
    if save_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_dir = os.path.join("outputs", f"run_{timestamp}")

    print(f"Bắt đầu huấn luyện REINFORCE trên môi trường {env_name}...")
    torch.manual_seed(seed)
    np.random.seed(seed)

    # Thiết lập device (Mac M-series có MPS, Windows/Linux có CUDA, fallback là CPU)
    if torch.backends.mps.is_available():
        device = torch.device("mps")
        print("Đang sử dụng Apple MPS device")
    elif torch.cuda.is_available():
        device = torch.device("cuda")
        print("Đang sử dụng CUDA device")
    else:
        device = torch.device("cpu")
        print("Đang sử dụng CPU device")

    env = gym.make(env_name)
    if hasattr(env.action_space, "seed"):
        env.action_space.seed(seed)
    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.n

    # Khởi tạo mô hình và Optimizer
    policy_net = PolicyNetwork(state_dim, action_dim, hidden_dim=hidden_dim).to(device)
    optimizer = optim.Adam(policy_net.parameters(), lr=lr)

    # Tạo thư mục lưu kết quả cho lượt chạy này
    os.makedirs(save_dir, exist_ok=True)
    best_reward = -float('inf')
    episode_rewards = []
    config = {
        "env": env_name,
        "episodes": max_episodes,
        "lr": lr,
        "gamma": gamma,
        "hidden_dim": hidden_dim,
        "seed": seed,
        "device": device,
    }

    # Vòng lặp chính huấn luyện
    for episode in range(1, max_episodes + 1):
        if episode == 1:
            state, _ = env.reset(seed=seed)
        else:
            state, _ = env.reset()

        log_probs = []
        rewards = []

        done = False
        truncated = False

        # Rollout 1 episode
        while not (done or truncated):
            action, log_prob = policy_net.select_action(state, device)

            # env.step(action) sinh transition (s_t, a_t, r_{t+1}, s_{t+1}).
            # next_state ứng với s_{t+1}; reward ứng với immediate reward r_{t+1}.
            next_state, reward, done, truncated, _ = env.step(action)

            # Lưu trữ history
            log_probs.append(log_prob)
            rewards.append(reward)

            state = next_state

        # Kết thúc 1 episode, total_reward là một mẫu Monte-Carlo của
        # trajectory return R(tau); episode_rewards dùng để ước lượng J(\theta).
        total_reward = sum(rewards)
        episode_rewards.append(total_reward)

        # Cập nhật Gradient theo REINFORCE rule
        returns = compute_returns(rewards, gamma)
        update_policy(optimizer, log_probs, returns, device)

        # Lưu model tốt nhất dựa trên tổng phần thưởng (total_reward) của tập đó.
        # Việc lưu 'best_policy' giúp ta giữ lại trạng thái mạng neural đạt hiệu suất cao nhất
        # trước khi bị ảnh hưởng bởi tính ngẫu nhiên của các episode sau.
        if total_reward > best_reward:
            best_reward = total_reward
            torch.save(policy_net.state_dict(), os.path.join(save_dir, "best_policy.pth"))

        # In log sau mỗi 50 tập: Khoảng cách này đủ để quan sát sự hội tụ trung bình
        # mà không gây loãng (spam) cửa sổ console.
        if episode % 50 == 0:
            avg_reward = np.mean(episode_rewards[-50:])
            print(f"Episode {episode}\t Tính trung bình 50 tập: {avg_reward:.2f}\t Best: {best_reward:.2f}")

    # Lưu model cuối cùng
    torch.save(policy_net.state_dict(), os.path.join(save_dir, "final_policy.pth"))
    _write_training_outputs(save_dir, config, episode_rewards, best_reward)
    print(f"Huấn luyện hoàn tất! Kết quả lưu tại: {save_dir}")
    env.close()
    return episode_rewards

def plot_learning_curve(rewards, save_path="training_curve.png", seed=None):
    if not rewards:
        plt.figure(figsize=(10, 5))
        title = 'REINFORCE Learning Curve on CartPole-v1'
        if seed is not None:
            title += f' (seed={seed})'
        plt.title(title)
        plt.xlabel('Episode')
        plt.ylabel('Total Reward')
        plt.grid(True, alpha=0.5)
        plt.savefig(save_path)
        print(f"Đã lưu biểu đồ rỗng tại {save_path}")
        return

    # Làm mượt (smooth) curve
    window = min(50, len(rewards))
    smoothed = np.convolve(rewards, np.ones(window)/window, mode='valid')

    plt.figure(figsize=(10, 5))
    plt.plot(rewards, alpha=0.3, color='blue', label='Raw Reward')
    plt.plot(np.arange(window-1, len(rewards)), smoothed, color='red', label='Smoothed (MA 50)')

    title = 'REINFORCE Learning Curve on CartPole-v1'
    if seed is not None:
        title += f' (seed={seed})'
    plt.title(title)
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.legend()
    plt.grid(True, alpha=0.5)

    # Lưu file đồ thị
    plt.savefig(save_path)
    print(f"Đã lưu biểu đồ thành công tại {save_path}")

if __name__ == "__main__":
    # Đặt seed để dễ dàng tái lập kết quả (reproducibility)
    seed = DEFAULT_SEED
    torch.manual_seed(seed)
    np.random.seed(seed)

    # Tạo folder output theo timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = os.path.join("outputs", f"run_{timestamp}")

    # Tạo thư mục trước khi chạy training
    os.makedirs(run_dir, exist_ok=True)

    # Chạy huấn luyện và lưu vào folder tương ứng
    rewards_history = train_reinforce(max_episodes=DEFAULT_EPISODES, seed=seed, save_dir=run_dir)

    # Lưu đồ thị vào cùng folder kết quả
    plot_learning_curve(rewards_history, save_path=os.path.join(run_dir, "training_curve.png"), seed=seed)
