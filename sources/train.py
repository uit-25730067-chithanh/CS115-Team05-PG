import gymnasium as gym
import torch
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np
import os

from datetime import datetime

# Sử dụng paths tương đối đối với module gốc
from models.policy import PolicyNetwork
from reinforce import compute_returns, update_policy

def train_reinforce(env_name="CartPole-v1", max_episodes=1000, lr=1e-3, gamma=0.99, save_dir=None):
    # Nếu không cung cấp save_dir, tự động tạo thư mục timestamp trong 'outputs/' 
    # để tránh xung đột với package 'models' của dự án.
    if save_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_dir = os.path.join("outputs", f"run_{timestamp}")

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
    
    # Tạo thư mục lưu kết quả cho lượt chạy này
    os.makedirs(save_dir, exist_ok=True)
    best_reward = -float('inf')
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
    print(f"Huấn luyện hoàn tất! Kết quả lưu tại: {save_dir}")
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
    # Đặt seed để dễ dàng tái lập kết quả (reproducibility)
    torch.manual_seed(42)
    np.random.seed(42)
    
    # Tạo folder output theo timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = os.path.join("outputs", f"run_{timestamp}")
    
    # Chạy huấn luyện và lưu vào folder tương ứng
    rewards_history = train_reinforce(max_episodes=1000, save_dir=run_dir)
    
    # Lưu đồ thị vào cùng folder kết quả
    plot_learning_curve(rewards_history, save_path=os.path.join(run_dir, "training_curve.png"))
