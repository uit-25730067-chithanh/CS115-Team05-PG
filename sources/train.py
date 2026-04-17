import os
import gymnasium as gym
import torch
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np

# Sử dụng paths tương đối đối với module gốc
from models.policy import PolicyNetwork
from reinforce import compute_returns, update_policy

def train_reinforce(env_name="CartPole-v1", max_episodes=1000, lr=1e-3, gamma=0.99):
    print(f"Bắt đầu huấn luyện REINFORCE trên môi trường {env_name}...")
    
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
    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.n
    
    # Khởi tạo mô hình và Optimizer
    policy_net = PolicyNetwork(state_dim, action_dim).to(device)
    optimizer = optim.Adam(policy_net.parameters(), lr=lr)
    
    # Mảng để vẽ đồ thị
    episode_rewards = []
    
    # Vòng lặp chính huấn luyện
    for episode in range(1, max_episodes + 1):
        state, _ = env.reset()
        
        log_probs = []
        rewards = []
        
        done = False
        truncated = False
        
        # Rollout 1 episode
        while not (done or truncated):
            action, log_prob = policy_net.select_action(state, device)
            
            next_state, reward, done, truncated, _ = env.step(action)
            
            # Lưu trữ history
            log_probs.append(log_prob)
            rewards.append(reward)
            
            state = next_state
            
        # Kết thúc 1 episode, tổng hợp kết quả
        total_reward = sum(rewards)
        episode_rewards.append(total_reward)
        
        # Cập nhật Gradient theo REINFORCE rule
        returns = compute_returns(rewards, gamma)
        update_policy(optimizer, log_probs, returns, device)
        
        # In log ra màn hình sau mỗi 50 tập
        if episode % 50 == 0:
            avg_reward = np.mean(episode_rewards[-50:])
            print(f"Episode {episode}\t Tính trung bình 50 tập: {avg_reward:.2f}")
            
    print("Huấn luyện hoàn tất!")
    env.close()
    return episode_rewards

def plot_learning_curve(rewards, save_path="training_curve.png"):
    # Làm mượt (smooth) curve
    window = min(50, len(rewards))
    smoothed = np.convolve(rewards, np.ones(window)/window, mode='valid')
    
    plt.figure(figsize=(10, 5))
    plt.plot(rewards, alpha=0.3, color='blue', label='Raw Reward')
    plt.plot(np.arange(window-1, len(rewards)), smoothed, color='red', label='Smoothed (MA 50)')
    
    plt.title('REINFORCE Learning Curve on CartPole-v1')
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.legend()
    plt.grid(True, alpha=0.5)
    
    # Lưu file đồ thị
    plt.savefig(save_path)
    print(f"Đã lưu biểu đồ thành công tại {save_path}")

if __name__ == "__main__":
    import pathlib
    
    # Đặt seed để dễ dàng tái lập kết quả (reproducibility)
    torch.manual_seed(42)
    np.random.seed(42)
    
    # Chạy cấu hình cơ bản (1000 tập là đủ để CartPole solve nếu thuật toán chạy tốt)
    rewards_history = train_reinforce(max_episodes=1000)
    
    # Lưu đồ thị vào thư mục hiện tại (hoặc có thể chỉnh sửa dời sang data/figures)
    plot_learning_curve(rewards_history)
