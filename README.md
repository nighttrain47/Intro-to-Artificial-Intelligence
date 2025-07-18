## 📚 Giới thiệu

Repository này chứa tài liệu học tập và bài tập thực hành cho môn học **Nhập môn Trí tuệ nhân tạo**. Mục đích của repo là lưu trữ và chia sẻ kiến thức, giải thích các thuật toán, và cung cấp code mẫu để giúp sinh viên hiểu rõ hơn về các khái niệm cơ bản trong AI.

## 🧠 Nội dung

Repository được tổ chức theo các bài thực hành (LAB) và bài tập về nhà (BTVN) với nội dung chi tiết như sau:

### 📚 Các bài thực hành (LAB)

#### **LAB 01: Thuật toán tìm kiếm mù (Blind Search)**

- **Mục tiêu**: Hiểu và cài đặt các thuật toán tìm kiếm cơ bản trong AI
- **Nội dung chi tiết**:
  - **Breadth-First Search (BFS)**: Tìm kiếm theo chiều rộng
    - Sử dụng cấu trúc dữ liệu Queue (FIFO)
    - Đảm bảo tìm ra đường đi ngắn nhất trên đồ thị không trọng số
    - Phân tích độ phức tạp thời gian và không gian
  - **Depth-First Search (DFS)**: Tìm kiếm theo chiều sâu
    - Sử dụng Stack hoặc đệ quy
    - Khám phá một nhánh đến tận cùng trước khi quay lại
    - So sánh ưu nhược điểm với BFS
  - **Ứng dụng thực tế**:
    - Tìm đường đi trên đồ thị không trọng số
    - Tìm đường đi trên đồ thị có trọng số
    - Phân tích kết quả và độ tối ưu của từng thuật toán
- **File**: `LAB 01/KieuThienBao_2374802010034.ipynb`

#### **LAB 03: Bài toán N-Queens và thuật toán Quay lui (Backtracking)**

- **Mục tiêu**: Giải quyết bài toán tối ưu hóa tổ hợp bằng thuật toán quay lui
- **Nội dung chi tiết**:
  - **Lý thuyết Backtracking**:
    - Kỹ thuật thiết kế thuật toán dựa trên đệ quy
    - Tìm tất cả các giải pháp cho bài toán
    - Cơ chế quay lui khi gặp bế tắc
  - **Bài toán 4-Queens**:
    - Đặt 4 quân hậu trên bàn cờ 4x4
    - Tìm tất cả các nghiệm khả thi
    - Biểu diễn nghiệm dưới dạng ma trận và tọa độ
  - **Bài toán 8-Queens**:
    - Mở rộng lên bàn cờ 8x8
    - Tối ưu hóa thuật toán để giảm thời gian thực thi
    - Phân tích số lượng nghiệm và độ phức tạp
  - **Cài đặt thuật toán**:
    - Kiểm tra tính hợp lệ của trạng thái
    - Tìm các vị trí ứng viên cho quân hậu tiếp theo
    - Thuật toán đệ quy tìm tất cả nghiệm
- **File**: `LAB 03/TH_2.ipynb`, `LAB 03/test.py`

#### **LAB 04: Thuật toán di truyền (Genetic Algorithm)**

- **Mục tiêu**: Cài đặt và tối ưu hóa thuật toán di truyền để tìm cực đại hàm số
- **Nội dung chi tiết**:
  - **Cơ sở lý thuyết GA**:
    - Mô phỏng quá trình tiến hóa tự nhiên
    - Các thành phần: quần thể, cá thể, gen, fitness
    - Chu trình tiến hóa: chọn lọc → lai ghép → đột biến
  - **Cài đặt thuật toán di truyền cơ bản**:
    - Khởi tạo quần thể ngẫu nhiên
    - Hàm fitness: `f(x) = sin(x) + cos(x)`
    - Chọn lọc theo tournament
    - Lai ghép bằng phương pháp trung bình
    - Đột biến ngẫu nhiên
  - **So sánh phương pháp chọn lọc**:
    - **Tournament Selection**: Chọn cá thể tốt nhất trong nhóm ngẫu nhiên
    - **Roulette Selection**: Chọn theo xác suất dựa trên fitness
    - Phân tích ưu nhược điểm của từng phương pháp
  - **Trực quan hóa**:
    - Biểu đồ hội tụ của quần thể qua các thế hệ
    - So sánh hiệu quả của các tham số khác nhau
    - Phân tích tốc độ hội tụ và chất lượng nghiệm
- **File**: `LAB 04/lab3.ipynb`

#### **LAB 05: [Đang cập nhật...]**

- Nội dung sẽ được bổ sung trong thời gian tới

### 🏠 Bài tập về nhà (BTVN)

#### **BTVN 1: Naive Bayes - Phân loại văn bản**

- **Mục tiêu**: Xây dựng hệ thống phân loại văn bản sử dụng thuật toán Naive Bayes
- **Nội dung chi tiết**:
  - **Lý thuyết Naive Bayes**:
    - Định lý Bayes và giả thiết độc lập có điều kiện
    - Ứng dụng trong phân loại văn bản
    - Xử lý văn bản và vector hóa
  - **Cài đặt mô hình**:
    - Tiền xử lý dữ liệu văn bản (tokenization, stemming)
    - Xây dựng từ điển và ma trận đặc trưng
    - Huấn luyện mô hình Naive Bayes
    - Đánh giá độ chính xác bằng confusion matrix
  - **Ứng dụng web**:
    - Giao diện web với Streamlit
    - Phân loại văn bản giáo dục theo sentiment
    - Hiển thị kết quả và độ tin cậy
  - **Dữ liệu**:
    - `Education.csv`: Dữ liệu văn bản giáo dục
    - `drug200.csv`: Dữ liệu phân loại thuốc
- **Cấu trúc project**:

  ```text
  BTVN/Naive_Bayes/
  ├── Code/                    # Jupyter notebooks và Python files
  ├── Data/                    # Datasets
  ├── naive_bayes_classifier/  # Package chính
  ├── naive-bayes-web-app/     # Ứng dụng web
  └── Ảnh/                     # Hình ảnh minh họa
  ```

#### **BTVN 2: CNN - Mạng nơ-ron tích chập**

- **Mục tiêu**: Hiểu và cài đặt mạng nơ-ron tích chập cho nhận dạng chữ số
- **Nội dung chi tiết**:
  - **Lý thuyết CNN**:
    - Cấu trúc và nguyên lý hoạt động của CNN
    - Các tầng: Convolution, Pooling, Fully Connected
    - Backpropagation trong CNN
  - **Cài đặt CNN**:
    - Sử dụng thư viện TensorFlow/Keras
    - Xây dựng kiến trúc mạng cho MNIST
    - Huấn luyện và fine-tuning tham số
  - **Dataset MNIST**:
    - 70,000 ảnh chữ số viết tay (0-9)
    - Tiền xử lý: chuẩn hóa, reshape
    - Chia dataset: train/validation/test
  - **Đánh giá mô hình**:
    - Accuracy, precision, recall, F1-score
    - Confusion matrix và classification report
    - Trực quan hóa kết quả dự đoán
  - **Tối ưu hóa**:
    - Điều chỉnh learning rate
    - Batch size và epochs
    - Dropout và regularization
- **File**: `BTVN/CNN/CNN-LAB.ipynb`
- **Dữ liệu**: `BTVN/CNN/data/MNIST/` (raw data)

## 💻 Cài đặt

Để chạy các bài thực hành trong repository này, bạn cần:

```bash
# Cài đặt Python (phiên bản 3.7 trở lên)
# Cài đặt các thư viện cần thiết cho machine learning và deep learning
pip install jupyter numpy matplotlib pandas scikit-learn tensorflow keras streamlit nltk
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
- Các thư viện Python chính:
  - **Cơ bản**: numpy, matplotlib, pandas
  - **Machine Learning**: scikit-learn, nltk
  - **Deep Learning**: tensorflow, keras
  - **Web App**: streamlit, flask
  - **Visualization**: seaborn, plotly

## 📂 Cấu trúc thư mục

```text
Intro-to-Artificial-Intelligence/
│
├── LAB 01/
│   ├── KieuThienBao_2374802010034.ipynb
│   └── README.md
│
├── LAB 03/
│   ├── TH_2.ipynb
│   ├── test.py
│   ├── README.md
│   └── Thực hành - Lab 02 - Artificial Intelligence.pdf
│
├── LAB 04/
│   ├── lab3.ipynb
│   └── README.md
│
├── LAB 05/
│   └── [Đang cập nhật...]
│
├── BTVN/
│   ├── Naive_Bayes/
│   │   ├── Code/
│   │   ├── Data/
│   │   ├── naive_bayes_classifier/
│   │   ├── naive-bayes-web-app/
│   │   └── Ảnh/
│   │
│   └── CNN/
│       ├── CNN-LAB.ipynb
│       └── data/MNIST/
│
├── README.md
└── requirements.txt
```

- **LAB 01/**: Thuật toán tìm kiếm mù (BFS, DFS)
- **LAB 03/**: Bài toán N-Queens và thuật toán Backtracking
- **LAB 04/**: Thuật toán di truyền (Genetic Algorithm)
- **LAB 05/**: [Đang cập nhật...]
- **BTVN/Naive_Bayes/**: Bài tập về nhà - Phân loại văn bản với Naive Bayes
- **BTVN/CNN/**: Bài tập về nhà - Mạng nơ-ron tích chập cho nhận dạng chữ số
- **README.md**: Tài liệu hướng dẫn chung cho repository
- **requirements.txt**: Danh sách các thư viện Python cần thiết

## 👨‍🏫 Đóng góp

Mọi đóng góp để cải thiện tài liệu và mã nguồn đều được hoan nghênh. Vui lòng:

1. Fork repository
2. Tạo branch mới (`git checkout -b feature/your-feature`)
3. Commit thay đổi (`git commit -m 'Add some feature'`)
4. Push lên branch của bạn (`git push origin feature/your-feature`)
5. Tạo Pull Request

## 📧 Liên hệ

Nếu có bất kỳ câu hỏi hoặc góp ý nào, vui lòng tạo issue hoặc liên hệ qua email: <thienbao2256@gmail.com>

---

© 2025 | Nhập môn Trí tuệ nhân tạo