# LAB 02 - N-Queens Problem

## Giới thiệu

Báo cáo này trình bày về việc giải quyết bài toán N-Queens, một bài toán kinh điển trong trí tuệ nhân tạo, sử dụng thuật toán quay lui (Backtracking). Cụ thể, báo cáo tập trung vào hai trường hợp: bài toán 4-Queens và 8-Queens mà giảng viên hướng dẫn.

## Tổng quan về bài toán N-Queens

Bài toán N-Queens yêu cầu đặt N quân hậu trên bàn cờ NxN sao cho không có hai quân hậu nào có thể tấn công lẫn nhau. Theo luật cờ vua, quân hậu có thể tấn công theo:
- Cùng hàng ngang
- Cùng cột dọc
- Các đường chéo

## Phương pháp giải quyết

### Thuật toán Backtracking

Backtracking là kỹ thuật thiết kế thuật toán dựa trên đệ quy để tìm tất cả các giải pháp cho bài toán. Ý tưởng chính của thuật toán:

1. Đặt quân hậu lần lượt trên từng hàng của bàn cờ
2. Khi đặt quân hậu ở một hàng, kiểm tra xem vị trí đó có bị tấn công bởi quân hậu khác không
3. Nếu vị trí an toàn, tiếp tục đặt quân hậu ở hàng tiếp theo
4. Nếu không tìm được vị trí an toàn ở hàng hiện tại, quay lại hàng trước và thử vị trí khác

### Cấu trúc code

Code được tổ chức thành các hàm chính:

1. **is_valid_state(state, num_queens)**: Kiểm tra xem trạng thái hiện tại có phải là lời giải hoàn chỉnh không
2. **get_candidates(state, num_queens)**: Tìm tất cả các cột có thể đặt quân hậu ở hàng tiếp theo
3. **search(state, solutions, num_queens)**: Hàm đệ quy thực hiện backtracking để tìm tất cả lời giải
4. **solve(num_queens)**: Gọi hàm search và trả về tất cả các lời giải

## Giải thích chi tiết thuật toán

### Biểu diễn trạng thái

Trong thuật toán này:
- Mỗi trạng thái được biểu diễn bằng một mảng 1 chiều
- Chỉ số của mảng là hàng của bàn cờ
- Giá trị tại mỗi chỉ số là cột nơi đặt quân hậu trong hàng đó
- Ví dụ: state = [1, 3, 0, 2] nghĩa là quân hậu được đặt tại các vị trí (0,1), (1,3), (2,0), (3,2)

### Kiểm tra vị trí an toàn

Hàm `get_candidates` xác định các vị trí an toàn để đặt quân hậu bằng cách loại bỏ:
- Các cột đã có quân hậu
- Các vị trí trên đường chéo của các quân hậu đã đặt

```python
def get_candidates(state, num_queens):
    if not state:
        return range(num_queens)

    position = len(state)
    candidates = set(range(num_queens))

    for row, col in enumerate(state):
        candidates.discard(col)
        dist = position - row
        candidates.discard(col + dist)
        candidates.discard(col - dist)

    return candidates
```

Trong đó:
- `position` là hàng hiện tại cần đặt quân hậu
- `candidates` ban đầu chứa tất cả các cột từ 0 đến num_queens-1
- Với mỗi quân hậu đã đặt, loại bỏ cột đã sử dụng và các vị trí trên đường chéo
- Hãy nhớ hai cái này, vì thiếu hai cái này là cả bài toán xem như chết. Và cũng đừng quên dist = position - row.

### Tìm kiếm lời giải

Hàm `search` thực hiện việc tìm kiếm đệ quy:

```python
def search(state, solutions, num_queens):
    if is_valid_state(state, num_queens):
        solutions.append(state.copy())
        return
    
    for candidate in get_candidates(state, num_queens):
        state.append(candidate)
        search(state, solutions, num_queens)
        state.pop()
```

## Kết quả

### Bài toán 4-Queens
- Số lời giải tìm được: 2 lời giải
- Các lời giải thể hiện bằng cách đặt quân hậu ở các vị trí sao cho không quân hậu nào tấn công quân hậu khác

### Bài toán 8-Queens
- Số lời giải tìm được: 92 lời giải
- Do số lượng lời giải lớn, nên yêu cầu chỉ output in ra 2 lời giải random

## Khái quát từ bản thân người viết theo cách chung nhất.
- Ta biết rằng, để giải bài toán này chính là làm sao sắp xếp được những con hậu vào bàn cờ, sao cho không tấn công lẫn nhau được. 
- Ở chương trình, ta có is_valid_state để kiểm tra lời giải, get_candidates để kiểm tra cột và search để tìm kiếm đệ quy, solve để gọi search và in ra lời giải. 
- Thực tế rằng điều mà quan trọng nhất là ở hàm main, ít quân hậu thì ta có thể viết đơn giản if - else rồi for. Nhưng quân hậu càng lớn thì càng dễ xảy lỗi, nên có thêm try expect.