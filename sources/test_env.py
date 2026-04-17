import gymnasium as gym

def test_environment():
    try:
        # Create CartPole environment with local rendering
        env = gym.make("CartPole-v1", render_mode="human")
        
        # Reset the environment to initial state
        state, info = env.reset()
        print(f"✅ Khởi tạo CartPole-v1 thành công!")
        print(f"👉 State shape: {env.observation_space.shape}")
        print(f"👉 Action shape: {env.action_space}")
        
        # Run a random episode
        done = False
        truncated = False
        steps = 0
        
        print("\nChạy thử agent với hành động ngẫu nhiên...")
        while not (done or truncated) and steps < 100:
            # Sample random action
            action = env.action_space.sample()
            
            # Step in the environment
            state, reward, done, truncated, info = env.step(action)
            steps += 1
            
        print(f"🎉 Agent chạy được {steps} steps trước khi kết thúc episode.")
        env.close()
        
    except Exception as e:
        print(f"❌ Lỗi khi khởi tạo môi trường: {str(e)}")

if __name__ == "__main__":
    test_environment()
