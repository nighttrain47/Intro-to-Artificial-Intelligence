## 📚 Giới thiệu

Repository này chứa tài liệu học tập và bài tập thực hành cho môn học **Nhập môn Trí tuệ nhân tạo**. Mục đích của repo là lưu trữ và chia sẻ kiến thức, giải thích các thuật toán, và cung cấp code mẫu để giúp sinh viên hiểu rõ hơn về các khái niệm cơ bản trong AI.

## 🧠 Nội dung

Repository được tổ chức theo các bài thực hành (LAB) với nội dung được cập nhật liên tục:

- **LAB 01**: Thuật toán tìm kiếm mù (Blind Search)
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Ứng dụng trên đồ thị không trọng số và có trọng số

- **LAB 03**: Bài toán N-Queens và thuật toán Quay lui (Backtracking)
  - Giải quyết bài toán 4-Queens
  - Giải quyết bài toán 8-Queens
  - Cài đặt thuật toán quay lui để tìm tất cả lời giải
  - Biểu diễn lời giải trên bàn cờ và dạng tọa độ

- **LAB 04**: Thuật toán di truyền (Genetic Algorithm)
  - Cài đặt thuật toán di truyền cơ bản
  - Tìm cực đại của hàm số
  - So sánh các phương pháp lựa chọn (Tournament vs Roulette)
  - Trực quan hóa quá trình hội tụ của quần thể

- **Các LAB tiếp theo sẽ được cập nhật...**

## 💻 Cài đặt

Để chạy các bài thực hành trong repository này, bạn cần:

```bash
# Cài đặt Python (phiên bản 3.7 trở lên)
# Cài đặt các thư viện cần thiết
pip install jupyter numpy matplotlib pandas
```

## 🚀 Cách sử dụng

1. Clone repository về máy local:
```bash
git clone https://github.com/yourusername/Intro-to-Artificial-Intelligence.git
cd Intro-to-Artificial-Intelligence
```

2. Mở và chạy các file Jupyter notebook:
```bash
jupyter notebook
```

3. Trong giao diện Jupyter, chọn file `.ipynb` tương ứng với bài thực hành bạn muốn thực hiện.

## ⚙️ Yêu cầu hệ thống

- Python 3.7+
- Jupyter Notebook/Lab
- Các thư viện Python: numpy, matplotlib, pandas (và các thư viện khác được liệt kê trong từng bài lab)

## 📂 Cấu trúc thư mục

````markdown
Intro-to-Artificial-Intelligence/
│
├── LAB01_BFS_DFS/
│   ├── lab01_bfs.ipynb
│   ├── lab01_dfs.ipynb
│   └── README.md
│
├── LAB03_N_Queens_Backtracking/
│   ├── lab03_n_queens.ipynb
│   └── README.md
│
├── LAB04_Genetic_Algorithm/
│   ├── lab04_genetic_algorithm.ipynb
│   ├── lab04_tournament_selection.ipynb
│   ├── lab04_roulette_selection.ipynb
│   └── README.md
│
├── README.md
└── requirements.txt
````

- **LAB01_BFS_DFS/**: Chứa các bài thực hành về thuật toán tìm kiếm mù.
- **LAB03_N_Queens_Backtracking/**: Chứa các bài thực hành về bài toán N-Queens và thuật toán quay lui.
- **LAB04_Genetic_Algorithm/**: Chứa các bài thực hành về thuật toán di truyền.
- **README.md**: Tài liệu hướng dẫn chung cho repository.
- **requirements.txt**: Danh sách các thư viện Python cần thiết cho các bài thực hành.

## 👨‍🏫 Đóng góp

Mọi đóng góp để cải thiện tài liệu và mã nguồn đều được hoan nghênh. Vui lòng:
1. Fork repository
2. Tạo branch mới (`git checkout -b feature/your-feature`)
3. Commit thay đổi (`git commit -m 'Add some feature'`)
4. Push lên branch của bạn (`git push origin feature/your-feature`)
5. Tạo Pull Request

## 📧 Liên hệ

Nếu có bất kỳ câu hỏi hoặc góp ý nào, vui lòng tạo issue hoặc liên hệ qua email: thienbao2256@gmail.com

---
© 2025 | Nhập môn Trí tuệ nhân tạo