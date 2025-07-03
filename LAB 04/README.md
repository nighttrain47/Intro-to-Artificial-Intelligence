# 📊 Lab 4 — Thuật Toán Di Truyền (Genetic Algorithm)

## 📌 Giới thiệu

Bài tập này báo cáo và hướng dẫn cài đặt và thực nghiệm thuật toán di truyền (Genetic Algorithm - GA) để tìm cực đại của một hàm số đơn giản. Qua bài tập, ta sẽ hiểu rõ:
- Cấu trúc cơ bản của GA
- Các thành phần trong GA
- Cách điều chỉnh tham số ảnh hưởng đến kết quả tối ưu
- Trực quan hóa quá trình hội tụ của quần thể
- Thầy Anh đẹp trai

### 1️ Cài đặt thuật toán di truyền cơ bản

#### Hàm mục tiêu:
```python
def fitness_function(x):
    return math.sin(x) + math.cos(x)
```
-> Hàm tính giá trị phù hợp (fitness) của mỗi cá thể.

#### Khởi tạo quần thể:
```python
def initialize_population(pop_size, min_val, max_val):
    return [random.uniform(min_val, max_val) for _ in range(pop_size)]
```
-> Tạo danh sách các giá trị ngẫu nhiên trong khoảng [min_val, max_val].

#### Chọn lọc (Tournament Selection):
```python
def select_parents(population, fitness_values, tournament_size=3):
    selected = random.sample(range(len(population)), tournament_size)
    best_idx = max(selected, key=lambda i: fitness_values[i])
    return population[best_idx]
```
-> Chọn tournament_size cá thể ngẫu nhiên, lấy cá thể tốt nhất làm cha/mẹ.

#### Lai ghép:
```python
def crossover(parent1, parent2, crossover_rate=0.8):
    if random.random() < crossover_rate:
        return (parent1 + parent2) / 2
    return parent1
```
-> Ghép hai cá thể bằng cách lấy trung bình, với xác suất crossover_rate.

#### Đột biến:
```python
def mutate(individual, mutation_rate=0.1, min_val=0, max_val=2*math.pi):
    if random.random() < mutation_rate:
        return random.uniform(min_val, max_val)
    return individual
```
-> Thay đổi ngẫu nhiên một cá thể với xác suất mutation_rate.

### 2️ Thay đổi tham số
Các tham số có thể điều chỉnh:

- **pop_size**: kích thước quần thể
- **generations**: số thế hệ
- **mutation_rate**: tỷ lệ đột biến
- **crossover_rate**: tỷ lệ lai ghép

→ Tác động đến khả năng hội tụ và chất lượng nghiệm tìm được. 

### 3️ Bổ sung Roulette Wheel Selection
#### Hàm lựa chọn bằng Roulette:
```python
def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    pick = random.uniform(0, total_fitness)
    current = 0
    for individual, fitness in zip(population, fitness_values):
        current += fitness
        if current >= pick:
            return individual
    return population[-1]
```
-> Cá thể có giá trị fitness cao hơn sẽ có xác suất chọn lớn hơn.

#### So sánh:
| Phương pháp | Ưu điểm | Nhược điểm |
|-------------|---------|------------|
| Tournament  | Đơn giản, dễ điều chỉnh độ cạnh tranh qua tournament_size | Có thể bỏ qua cá thể tốt nếu chọn ngẫu nhiên |
| Roulette    | Tỷ lệ chọn đúng theo fitness, tăng cơ hội cho cá thể tốt | Cần chuẩn hóa nếu fitness âm hoặc tổng fitness thấp |

### 4️ Trực quan hóa quần thể
#### Vẽ đường fitness tốt nhất:
```python
plt.plot(range(generations), best_fitness_history)
```
-> Theo dõi quá trình hội tụ.

#### Vẽ scatter plot phân bố quần thể:
```python
xs, gens = zip(*population_history)
plt.scatter(xs, gens, alpha=0.5, s=10, c=gens, cmap='viridis')
```
-> Phân bố giá trị các cá thể qua các thế hệ — giúp quan sát sự lan tỏa và hội tụ.

## Hướng dẫn chạy
### Cài đặt thư viện:
```bash
pip install numpy matplotlib
```

### Chạy file:
- Mở lab4.ipynb trên Jupyter Notebook
- hoặc
- Chạy file Python tương ứng.

### Ví dụ chạy:
```python
best_x, best_f = genetic_algorithm_example1(
    pop_size=100,
    generations=200,
    mutation_rate=0.1,
    crossover_rate=0.9,
    selection_method='roulette'
)
```

## Nhận xét — So sánh hiệu quả

### Tournament:
- Hội tụ ổn định với tournament_size hợp lý.
- Phân bố quần thể tập trung dần quanh giá trị tốt nhất.

### Roulette:
- Dễ bị ảnh hưởng bởi cá thể cực tốt dẫn đến mất đa dạng.
- Khi fitness thấp hoặc đồng đều, chọn lọc kém hiệu quả.

### Scatter plot cho thấy:
- Ban đầu quần thể phân bố ngẫu nhiên.
- Qua các thế hệ, giá trị tốt dần được duy trì và hội tụ.


# Lưu ý: Mọi kết luận trong file này được dựa trên file bài tập của thầy Anh và cá nhân sinh viên (người làm file) đúc kết được trong quá trình làm bài tập. 



