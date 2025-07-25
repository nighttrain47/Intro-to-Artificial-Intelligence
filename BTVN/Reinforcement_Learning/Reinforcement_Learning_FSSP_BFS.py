import matplotlib.pyplot as plt
import numpy as np
from collections import deque

# hướng di chuyển có thể: lên, xuống, trái, phải
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class FSSP_BFS:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])
        
    # kiểm tra vị trí có nằm trong dạng lưới & vị trí có bị chặn hay không
    def is_valid(self, position):
        r, c = position
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == 0
        
    # tìm kiếm theo chiều rộng để tìm đường đi ngắn nhất từ điểm bắt đầu đến điểm kết thúc
    def bfs(self):
        queue = deque([(self.start, [self.start])])
        visited = set([self.start])
        
        while queue:
            current, path = queue.popleft()
            
            # nếu vị trí hiện tại là mục tiêu, trả về đường dẫn
            if current == self.goal:
                return path

            # khám phá tất cả các đường đi có thể (lên, xuống, trái, phải)
            for move in MOVES:
                next_r, next_c = current[0] + move[0], current[1] + move[1]
                next_position = (next_r, next_c)
                
                if self.is_valid(next_position) and next_position not in visited:
                    visited.add(next_position)
                    queue.append((next_position, path + [next_position]))
                    
        return None  # trả về None nếu không có đường dẫn đến đích
        
    # hầm trực quan dạng lưới và đường dẫn
    def visualize(self, path):
        grid_np = np.array(self.grid)
        
        # tạo hình và trục số
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.imshow(grid_np, cmap='Greys', alpha=0.8)
        
        # đánh dấu điểm bắt đầu và điểm kết thúc bằng các ký hiệu đặc biệt
        ax.text(self.start[1], self.start[0], 'Start', color='green', fontsize=25, fontweight='bold', ha='center', va='center')
        ax.text(self.goal[1], self.goal[0], 'Goal', color='red', fontsize=25, fontweight='bold', ha='center', va='center')
        
        # về đường đi nếu tìm thấy
        if path:
            path_np = np.array(path)
            ax.plot(path_np[:, 1], path_np[:, 0], color='blue', linewidth=4.0, marker='o', markersize=10, markerfacecolor='yellow', label='Path')
            
        # kiểu dạng lưới và gần nhân
        ax.set_xticks(np.arange(self.cols))
        ax.set_yticks(np.arange(self.rows))
        ax.set_xticklabels(np.arange(self.cols))
        ax.set_yticklabels(np.arange(self.rows))
        ax.grid(which='both', color='black', linewidth=2.0)
        
        # add tiêu đề dạng lưới và trực quan biểu đồ
        plt.title("Grid and Path Visualization", fontsize=20, fontweight='bold')
        plt.tight_layout()
        plt.show()

# dạng lưới (0 = ô trống, 1 = chướng ngại vật)
grid = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]

# vị trí điểm bắt đầu và điểm đích
start = (0, 0)
goal = (4, 4)

# hàm FSSP_BFS- tìm kiếm chiều rộng
planner = FSSP_BFS(grid, start, goal)
path = planner.bfs()

if path:
    print(f"Path found: {path}")
    # trực quan đường dẫn
    planner.visualize(path)
else:
    print("No path found")
