import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical

class PolicyNetwork(nn.Module):
    """
    Mạng nơ-ron (MLP) cho Policy Gradient (REINFORCE)
    Biểu diễn stochastic policy pi_theta(a_t | s_t).

    Với CartPole-v1, state là s_t in R^4:
    [cart position, cart velocity, pole angle phi, pole angular velocity].
    Thành phần state[2] là góc nghiêng phi; không dùng theta cho pole angle
    vì theta được dành cho policy parameters.
    """
    def __init__(self, state_dim, action_dim, hidden_dim=128):
        super(PolicyNetwork, self).__init__()
        
        # Lớp ẩn ẩn (Hidden layer)
        self.fc1 = nn.Linear(state_dim, hidden_dim)
        
        # Lớp đầu ra (Output layer)
        self.fc2 = nn.Linear(hidden_dim, action_dim)
        
    def forward(self, x):
        """
        Forward pass qua mạng.
        Trả về phân phối xác suất của các hành động (softmax).
        """
        x = F.relu(self.fc1(x))
        out = self.fc2(x)
        # Softmax để tạo ra xác suất trên trục cuối (hành động)
        return F.softmax(out, dim=-1)
        
    def select_action(self, state, device="cpu"):
        """
        Chọn hành động a_t dựa trên xác suất pi_theta(a_t | s_t).

        Returns:
            action: Hành động (số nguyên)
            log_prob: Log-xác suất của hành động được chọn
                log pi_theta(a_t | s_t)
        """
        # Chuyển numpy state s_t in R^4 thành torch tensor.
        # Với CartPole, state[2] là pole angle phi.
        state_tensor = torch.from_numpy(state).float().unsqueeze(0).to(device)
        
        # Forward để lấy xác suất của mỗi action
        probs = self.forward(state_tensor)
        
        # Tạo object phân phối Categorical dựa trên xác suất trên
        m = Categorical(probs)
        
        # Rút thăm (Sample) ngẫu nhiên hành động dựa trên xác suất
        action = m.sample()
        
        # Tính log-probability để dùng trong log-derivative trick
        log_prob = m.log_prob(action)
        
        return action.item(), log_prob
