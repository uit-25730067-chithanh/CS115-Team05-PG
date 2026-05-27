import torch

def compute_returns(rewards, gamma):
    """
    Tính discounted reward-to-go G_t cho một episode.
    
    Args:
        rewards (list): Mảng phần thưởng môi trường [r_1, r_2, ..., r_{T+1}]
        gamma (float): Discount factor
        
    Returns:
        list: Returns G_t cho mỗi time step, trong đó
            G_t = sum_{k=t}^T gamma^{k-t} * r_{k+1}
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
    r"""
    Thực hiện bước cập nhật theo Policy Gradient Theorem.

    Trong PyTorch, policy_loss là L(\theta):
        L(\theta) = -sum_t log pi_theta(a_t | s_t) * G_t
    Optimizer minimize L(\theta), tương đương maximize objective J(\theta).
    
    Args:
        optimizer: torch.optim optimizer
        log_probs: list của torch.Tensor log_prob của các action
        returns: list của G_t
        device (str hoặc torch.device): Thiết bị dùng để đưa tensor lên, ví dụ
            "cpu", "cuda", hoặc "mps"
    """
    returns = torch.tensor(returns, dtype=torch.float32).to(device)
    
    # Kỹ thuật quan trọng: standardization làm baseline đơn giản để giảm variance.
    # G_t <- (G_t - mu(G)) / (sigma(G) + \varepsilon)
    # \varepsilon = 1e-8 giúp tránh chia cho 0.
    if len(returns) > 1:
        returns = (returns - returns.mean()) / (returns.std() + 1e-8)
        
    policy_loss = []
    
    for log_prob, G_t in zip(log_probs, returns):
        # Loss = -log pi_theta(a_t | s_t) * G_t
        # Đây là log-derivative trick:
        # grad J(\theta) = E[grad log pi_theta(a_t | s_t) * G_t]
        # Dấu âm vì PyTorch thực hiện gradient descent trên L(theta),
        # tương đương gradient ascent cho J(\theta).
        policy_loss.append(-log_prob * G_t)
        
    # Tính tổng loss của toàn memory (episode)
    # Cần phải dùng torch.stack để list tensor -> 1D tensor -> tổng hợp gradient graph
    policy_loss = torch.stack(policy_loss).sum()
    
    # Backpropagation
    optimizer.zero_grad()      # Reset gradient cũ
    policy_loss.backward()     # Tính toán gradient mới (backprop)
    optimizer.step()           # Cập nhật weights theta
