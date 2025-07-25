import numpy as np
import matplotlib.pyplot as plt

# các siêu tham số
n_states = 16
n_actions = 4
goal_state = 15
Q_table = np.zeros((n_states, n_actions))
alpha = 0.1  # hệ số alpha
gamma = 0.9  # hệ số gamma
exploration_prob = 0.2
epochs = 1000  # hệ số tập

# quy trình của Q learning
for epoch in range(epochs):
    current_state = np.random.randint(0, n_states)
    while current_state != goal_state:
        # khám phá so với khai thác (e-chính sách tham lam)
        if np.random.rand() < exploration_prob:
            action = np.random.randint(0, n_actions)
        else:
            action = np.argmax(Q_table[current_state])
            
        # chuyển sang trạng thái tiếp theo
        next_state = (current_state + 1) % n_states
        
        # phần thưởng 1 nếu đạt được goal_state, 0 nếu không đạt 
        reward = 1 if next_state == goal_state else 0
        
        # cập nhật giá trị Q
        Q_table[current_state, action] = Q_table[current_state, action] + alpha * (reward + gamma * np.max(Q_table[next_state]) - Q_table[current_state, action])
        
        current_state = next_state  # cập nhật trạng thái hiện tại

# trực quan bảng Q dạng lưới
q_values_grid = np.max(Q_table, axis=1).reshape((4, 4))

# biểu đồ dạng lưới các giá trị Q
plt.figure(figsize=(6, 6))
plt.imshow(q_values_grid, cmap='coolwarm', interpolation='nearest')
plt.colorbar(label='Q-value')
plt.title('Learned Q-values for each state')
plt.xticks(np.arange(4), ['0', '1', '2', '3'])
plt.yticks(np.arange(4), ['0', '1', '2', '3'])
plt.gca().invert_yaxis()

# bố cục dạng lưới
plt.grid(True)

# các giá trị Q dạng lưới
for i in range(4):
    for j in range(4):
        plt.text(j, i, f'{q_values_grid[i, j]:.2f}', ha='center', va='center', color='black')

plt.show()

# xuất ra bảng Q đã học
print("Learned Q-table:")
print(Q_table)
