import gymnasium as gym
import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def test_environment():
    """Sanity check: chạy 1 episode random để verify môi trường hoạt động."""
    try:
        env = gym.make("CartPole-v1", render_mode="human")
        state, info = env.reset()
        print("Khởi tạo CartPole-v1 thành công!")
        print(f"State shape: {env.observation_space.shape}")
        print(f"Action shape: {env.action_space}")

        done = False
        truncated = False
        steps = 0

        print("\nChạy thử agent với hành động ngẫu nhiên...")
        while not (done or truncated) and steps < 100:
            action = env.action_space.sample()
            state, reward, done, truncated, info = env.step(action)
            steps += 1

        print(f"Agent chạy được {steps} steps trước khi kết thúc episode.")
        env.close()

    except Exception as e:
        print(f"Lỗi khi khởi tạo môi trường: {str(e)}")


def evaluate_baseline(env_name="CartPole-v1", n_episodes=100, save_dir=None):
    """Chạy n_episodes random để thu thập baseline scores.

    Args:
        env_name: Tên môi trường Gymnasium.
        n_episodes: Số episode random chạy (mặc định 100).
        save_dir: Thư mục lưu kết quả. Nếu None, tự tạo timestamp trong outputs/.

    Returns:
        list: Rewards từng episode.
    """
    if save_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_dir = os.path.join("outputs", f"baseline_{timestamp}")
    os.makedirs(save_dir, exist_ok=True)

    env = gym.make(env_name)
    rewards = []

    print(f"\nBắt đầu đánh giá baseline random: {n_episodes} episodes...")
    for ep in range(1, n_episodes + 1):
        state, _ = env.reset()
        ep_reward = 0
        done = truncated = False
        while not (done or truncated):
            action = env.action_space.sample()
            state, reward, done, truncated, _ = env.step(action)
            ep_reward += reward
        rewards.append(ep_reward)
        if ep % 10 == 0:
            print(f"Episode {ep}/{n_episodes} done")
    env.close()

    # Stats
    mean_r = float(np.mean(rewards))
    std_r = float(np.std(rewards))
    min_r = int(np.min(rewards))
    max_r = int(np.max(rewards))

    print(f"\nBaseline Stats ({n_episodes} episodes):")
    print(f"  Mean: {mean_r:.2f}")
    print(f"  Std:  {std_r:.2f}")
    print(f"  Min:  {min_r}")
    print(f"  Max:  {max_r}")

    # 1. Plot
    plt.figure(figsize=(10, 5))
    plt.plot(rewards, alpha=0.3, color="blue", label="Raw Reward")
    window = min(10, len(rewards))
    if window > 1:
        smoothed = np.convolve(rewards, np.ones(window) / window, mode="valid")
        plt.plot(np.arange(window - 1, len(rewards)), smoothed, color="red", label=f"Smoothed (MA {window})")
    plt.axhline(mean_r, color="green", linestyle="--", label=f"Mean: {mean_r:.2f}")
    plt.title(f"Random Agent Baseline — {env_name} ({n_episodes} Episodes)")
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.legend()
    plt.grid(True, alpha=0.5)
    plot_path = os.path.join(save_dir, "baseline_curve.png")
    plt.savefig(plot_path)
    print(f"Đã lưu plot: {plot_path}")

    # 2. Stats file
    stats_path = os.path.join(save_dir, "baseline_stats.txt")
    with open(stats_path, "w", encoding="utf-8") as f:
        f.write(f"Environment: {env_name}\n")
        f.write(f"Episodes:    {n_episodes}\n")
        f.write(f"Mean:        {mean_r:.4f}\n")
        f.write(f"Std:         {std_r:.4f}\n")
        f.write(f"Min:         {min_r}\n")
        f.write(f"Max:         {max_r}\n")
    print(f"Đã lưu stats: {stats_path}")

    # 3. Raw log
    log_path = os.path.join(save_dir, "baseline_log.txt")
    with open(log_path, "w", encoding="utf-8") as f:
        for i, r in enumerate(rewards, 1):
            f.write(f"{i}\t{r}\n")
    print(f"Đã lưu raw log: {log_path}")

    print(f"\nTất cả kết quả lưu tại: {save_dir}")
    return rewards


if __name__ == "__main__":
    test_environment()
    evaluate_baseline(n_episodes=100)
