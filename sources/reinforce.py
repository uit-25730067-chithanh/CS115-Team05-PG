import torch

def compute_returns(rewards, gamma):
    """
    Tính Discounted Returns (G_t) cho một episode.
    
    Args:
        rewards (list): Mảng phần thưởng môi trường [R_0, R_1, ..., R_T]
        gamma (float): Discount factor
        
    Returns:
        list: Returns G_t cho mỗi time step, trong đó G_t = sum_{k=t}^T (gamma^{k-t} * R_k)
    """
    returns = []
    G_t = 0
    # Tính lùi từ bước cuối cùng về đầu
    for r in reversed(rewards):
        G_t = r + gamma * G_t
        returns.append(G_t)

    returns.reverse()
    return returns

def update_policy(optimizer, log_probs, returns, device="cpu"):
    """
    Thực hiện bước cập nhật Gradient Ascent (nhưng trong code là Gradient Descent của Loss âm)
    dựa trên Policy Gradient Theorem.
    
    Args:
        optimizer: torch.optim optimizer
        log_probs: list của torch.Tensor log_prob của các action
        returns: list của G_t
        device (str hoặc torch.device): Thiết bị dùng để đưa tensor lên, ví dụ
            "cpu", "cuda", hoặc "mps"
    """
    returns = torch.tensor(returns, dtype=torch.float32).to(device)
    
    # Kỹ thuật quan trọng: Chuẩn hóa returns (Baseline cơ bản nhất) để giảm Variance
    # (G_t - mean(G)) / (std(G) + epsilon)
    # Epsilon (1e-8) giúp tránh chia cho 0
    if len(returns) > 1:
        returns = (returns - returns.mean()) / (returns.std() + 1e-8)
        
    policy_loss = []
    
    for log_prob, G_t in zip(log_probs, returns):
        # Loss = - log_prob(a|s, theta) * G_t
        # Đây là log-derivative trick: gradient of J(theta) = E[ grad log pi(a|s) * G_t ]
        # Dấu âm vì PyTorch thực hiện Gradient Descent mà ta cần Gradient Ascent cho J(theta)
        policy_loss.append(-log_prob * G_t)
        
    # Tính tổng loss của toàn memory (episode)
    # Cần phải dùng torch.stack để list tensor -> 1D tensor -> tổng hợp gradient graph
    policy_loss = torch.stack(policy_loss).sum()
    
    # Backpropagation
    optimizer.zero_grad()      # Reset gradient cũ
    policy_loss.backward()     # Tính toán gradient mới (backprop)
    optimizer.step()           # Cập nhật weights theta
