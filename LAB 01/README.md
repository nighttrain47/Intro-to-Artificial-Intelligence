# LAB 01: Thuật Toán Tìm Kiếm Mù - Breadth-First Search & Depth-First Search

Lời nói đầu: File README này dùng để báo cáo về LAB01, hay là kiến thức mà người viết hiểu được dùng để trình bày về những bài tập đã giải quyết.

## 1. Tổng Quan

Lab này tập trung vào hai thuật toán tìm kiếm mù cơ bản trong trí tuệ nhân tạo: Thuật toán tìm kiếm theo chiều rộng (BFS) và thuật toán tìm kiếm theo chiều sâu (DFS). Các thuật toán này được áp dụng trên các đồ thị không trọng số và có trọng số để tìm đường đi từ một nút nguồn đến nút đích.

## 2. Cơ Sở Lý Thuyết

### 2.1 Tìm Kiếm Mù (Uninformed Search)

Tìm kiếm mù là các thuật toán tìm kiếm không sử dụng thông tin heuristic, duyệt qua không gian trạng thái theo cách có hệ thống, dựa trên cấu trúc bài toán chứ không dựa trên đánh giá về khoảng cách đến mục tiêu.

### 2.2 Tìm Kiếm theo Chiều Rộng (BFS)

- **Nguyên lý**: BFS khám phá tất cả các nút ở mức hiện tại trước khi chuyển sang mức tiếp theo.
- **Cấu trúc dữ liệu**: Hàng đợi (Queue) - FIFO (First In First Out).
- **Đặc điểm**:
  - Đảm bảo tìm ra đường đi ngắn nhất theo số cạnh trên đồ thị không trọng số.
  - Không đảm bảo đường đi có tổng trọng số nhỏ nhất trên đồ thị có trọng số.
  - Không bị rơi vào vòng lặp vô hạn với không gian trạng thái hữu hạn.

### 2.3 Tìm Kiếm theo Chiều Sâu (DFS)

- **Nguyên lý**: DFS khám phá một nhánh đến tận cùng trước khi quay lại thử nhánh khác.
- **Cấu trúc dữ liệu**: Ngăn xếp (Stack) hoặc đệ quy.
- **Đặc điểm**:
  - Không đảm bảo đường đi ngắn nhất trong cả đồ thị không trọng số và có trọng số.
  - Kết quả phụ thuộc vào thứ tự duyệt các nút kề.
  - Có thể đi sâu vô tận trong không gian trạng thái vô hạn.

## 3. Phân Tích Thuật Toán trên Các Loại Đồ Thị

### 3.1 Đồ Thị Không Trọng Số

- **BFS**: Đảm bảo tìm được đường đi có ít cạnh nhất (đường đi ngắn nhất).
- **DFS**: Không đảm bảo tìm được đường đi ngắn nhất, nhưng có thể hiệu quả trong một số trường hợp đặc biệt.

### 3.2 Đồ Thị Có Trọng Số

- **BFS**: Tìm ra đường đi với ít cạnh nhất, nhưng không đảm bảo tổng trọng số nhỏ nhất.
- **DFS**: Không đảm bảo tìm ra đường đi tối ưu về số cạnh hoặc tổng trọng số.

## 4. Triển Khai và Kết Quả

### 4.1 Kết Quả trên Đồ Thị Mẫu 1 (Không Trọng Số)

BFS tìm ra đường đi: `S → B → E → G` với độ dài 3, là đường đi ngắn nhất.  
DFS tìm ra đường đi: `S → B → E → G` (trong trường hợp này, trùng với BFS).

### 4.2 Kết Quả trên Đồ Thị Mẫu 5 (Có Trọng Số)

BFS tìm ra đường đi: `S → A → G` với tổng trọng số 4.  
DFS tìm ra đường đi: `S → A → G` với tổng trọng số 4.

### 4.3 Kết Quả trên Đồ Thị Mẫu 6 (Có Trọng Số)

BFS tìm ra đường đi: `S → A → B → E → H` với tổng trọng số 21.  
DFS tìm ra đường đi: `S → A → B → E → H` với tổng trọng số 21.

### 4.4 Kết Quả trên Đồ Thị Mẫu 7 (Không Trọng Số, Mật Độ Cao)

BFS tìm ra đường đi: `S → E → H` là đường đi ngắn nhất với 2 cạnh.  
DFS tìm ra một đường đi: `S → A → B → C → F → G → H` với 6 cạnh.

## 5. Câu Hỏi Lý Thuyết

### 5.1 Tại sao BFS đảm bảo đường đi ngắn nhất trên đồ thị không trọng số nhưng không đảm bảo trên đồ thị có trọng số?

BFS duyệt các đỉnh theo thứ tự tăng dần về khoảng cách (số cạnh) từ đỉnh nguồn. Khi đồ thị không có trọng số, mỗi cạnh được xem như có độ dài bằng 1, nên khoảng cách ngắn nhất đồng nghĩa với ít cạnh nhất.

Tuy nhiên, trong đồ thị có trọng số, đường đi có ít cạnh nhất không nhất thiết có tổng trọng số nhỏ nhất. BFS không xét đến trọng số khi quyết định thứ tự duyệt các đỉnh, nên có thể đến đích sớm qua một đường đi có trọng số lớn hơn, thay vì chọn đường đi tổng trọng số nhỏ hơn.

### 5.2 Trong đồ thị có chu trình, làm thế nào để BFS và DFS tránh lặp vô hạn?

Cả BFS và DFS đều sử dụng một tập hợp (set) các đỉnh đã thăm để tránh duyệt lại các đỉnh. Khi một đỉnh được thêm vào hàng đợi (BFS) hoặc ngăn xếp (DFS), đỉnh đó cũng được đánh dấu là đã thăm. Sau đó, mỗi khi xét một đỉnh kề, ta chỉ xét các đỉnh chưa được đánh dấu. Cách này đảm bảo mỗi đỉnh chỉ được thăm một lần, tránh lặp vô hạn.

## 6. Minh Họa Thủ Công

### 6.1 BFS trên Đồ Thị Mẫu 2 (Có Chu Trình):
```
Khởi tạo: Hàng đợi = [(S, [S])], Đã thăm = {S}
Lấy S, thêm A, B: Hàng đợi = [(A, [S, A]), (B, [S, B])], Đã thăm = {S, A, B}
Lấy A, thêm C: Hàng đợi = [(B, [S, B]), (C, [S, A, C])], Đã thăm = {S, A, B, C}
Lấy B, thêm D: Hàng đợi = [(C, [S, A, C]), (D, [S, B, D])], Đã thăm = {S, A, B, C, D}
Lấy C: Không có đỉnh kề mới (D đã thăm)
Lấy D, thêm G: Hàng đợi = [(G, [S, B, D, G])], Đã thăm = {S, A, B, C, D, G}
Lấy G: G là đích, trả về [S, B, D, G]
```

Kết quả: Đường đi BFS: S → B → D → G

### 6.2 DFS trên Đồ Thị Mẫu 2 (Có Chu Trình):
```
Khởi tạo: Ngăn xếp = [(S, [S])], Đã thăm = {S}
Lấy S, thêm A: Ngăn xếp = [(A, [S, A])], Đã thăm = {S, A}
Lấy A, thêm C, B: Ngăn xếp = [(C, [S, A, C]), (B, [S, A, B])], Đã thăm = {S, A, C, B}
Lấy C, thêm D: Ngăn xếp = [(D, [S, A, C, D]), (B, [S, A, B])], Đã thăm = {S, A, C, B, D}
Lấy D, thêm G: Ngăn xếp = [(G, [S, A, C, D, G]), (B, [S, A, B])], Đã thăm = {S, A, C, B, D, G}
Lấy G: G là đích, trả về [S, A, C, D, G]
```

Kết quả: Đường đi DFS: S → A → C → D → G


### Đồ thị mẫu 3
Đồ thị mẫu 3:
BFS:
Khởi tạo: Hàng đợi = [(S, [S])], Đã thăm = {S}
Lấy S, thêm A, B: Hàng đợi = [(A, [S, A]), (B, [S, B])], Đã thăm = {S, A, B}
Lấy A, thêm C: Hàng đợi = [(B, [S, B]), (C, [S, A, C])], Đã thăm = {S, A, B, C}
Lấy B, thêm D: Hàng đợi = [(C, [S, A, C]), (D, [S, B, D])], Đã thăm = {S, A, B, C, D}
Lấy C, không có đỉnh mới.
Lấy D, không có đỉnh mới.
Vậy là ta không tìm thấy G.

DFS:
Khởi tạo: Ngăn xếp = [(S, [S])], Đã thăm = {S}
Lấy S, thêm A: Ngăn xếp = [(A, [S, A])], Đã thăm = {S, A}
Lấy A, thêm C: Ngăn xếp = [(C, [S, A, C])], Đã thăm = {S, A, C}
Lấy C, không có đỉnh mới.
Quay lại, lấy B: Ngăn xếp = [(B, [S, B])], Đã thăm = {S, A, C, B}
Lấy B, thêm D: Ngăn xếp = [(D, [S, B, D])], Đã thăm = {S, A, C, B, D}
Lấy D, không có đỉnh mới.
Vậy là ta không tìm thấy G.



### 6.3 BFS trên Đồ Thị Mẫu 6 (Có Trọng Số):
```
Khởi tạo: Hàng đợi = [(S, [S], 0)], Đã thăm = {S}
Lấy S, thêm A (2), C (5): Hàng đợi = [(A, [S, A], 2), (C, [S, C], 5)], Đã thăm = {S, A, C}
Lấy A, thêm B (5), D (6): Hàng đợi = [(C, [S, C], 5), (B, [S, A, B], 5), (D, [S, A, D], 6)], Đã thăm = {S, A, C, B, D}
Lấy C, thêm F (14): Hàng đợi = [(B, [S, A, B], 5), (D, [S, A, D], 6), (F, [S, C, F], 14)], Đã thăm = {S, A, C, B, D, F}
Lấy B, thêm E (11): Hàng đợi = [(D, [S, A, D], 6), (F, [S, C, F], 14), (E, [S, A, B, E], 11)], Đã thăm = {S, A, C, B, D, F, E}
Lấy D, E đã thăm
Lấy F, thêm G (26): Hàng đợi = [(E, [S, A, B, E], 11), (G, [S, C, F, G], 26)], Đã thăm = {S, A, C, B, D, F, E, G}
Lấy E, thêm H (21): Hàng đợi = [(G, [S, C, F, G], 26), (H, [S, A, B, E, H], 21)], Đã thăm = {S, A, C, B, D, F, E, G, H}
Lấy G, H đã thăm
Lấy H: H là đích, trả về [S, A, B, E, H], tổng trọng số 21
```

Kết quả: Đường đi BFS: S → A → B → E → H với tổng trọng số 21

### 6.4 Các Đường Đi BFS từ S đến H trên Đồ Thị Mẫu 7:
['S', 'E', 'H']
['S', 'A', 'E', 'H']
['S', 'D', 'E', 'H']
['S', 'E', 'F', 'H']
['S', 'A', 'B', 'E', 'H']
['S', 'A', 'B', 'F', 'H']
['S', 'A', 'D', 'E', 'H']
['S', 'A', 'E', 'F', 'H']
['S', 'D', 'E', 'F', 'H']
['S', 'E', 'F', 'G', 'H']
['S', 'A', 'B', 'C', 'F', 'H']
['S', 'A', 'B', 'C', 'G', 'H']
['S', 'A', 'B', 'E', 'F', 'H']
['S', 'A', 'B', 'F', 'G', 'H']
['S', 'A', 'D', 'E', 'F', 'H']
['S', 'A', 'E', 'F', 'G', 'H']
['S', 'D', 'E', 'F', 'G', 'H']
['S', 'A', 'B', 'C', 'F', 'G', 'H']
['S', 'A', 'B', 'E', 'F', 'G', 'H']
['S', 'A', 'D', 'E', 'F', 'G', 'H']

## 7. Bài Tập Nâng Cao

### 7.1 So Sánh Hiệu Suất BFS và DFS

Khi chạy trên đồ thị mẫu 6 (có trọng số):
- BFS: Thời gian chạy ≈ 0.000072 giây
- DFS: Thời gian chạy ≈ 0.000045 giây

Khi chạy trên đồ thị mẫu 7 (không trọng số):
- BFS: Thời gian chạy ≈ 0.000040 giây
- DFS: Thời gian chạy ≈ 0.000042 giây

Nhận xét: BFS và DFS có thời gian thực thi tương đương nhau trên các đồ thị nhỏ. Sự khác biệt về thời gian có thể trở nên đáng kể trên các đồ thị lớn hoặc không gian trạng thái rộng.

### 7.2 Kết Quả trên Đồ Thị Phức Tạp (12 nút, 17 cạnh)

Khi chạy trên đồ thị phức tạp từ S đến K:
- BFS: Đường đi S → A → C → F → I → K với tổng trọng số 35
- DFS: Đường đi S → A → C → F → I → K với tổng trọng số 35


### Lưu ý chung: 
- Tuy nói rằng việc tìm BFS và DFS điều có ưu điểm riêng của nó, nhưng khi bê lên code, thì nó sẽ khó ở chỗ để không bị rơi vào vòng lặp.
- Thường thì ta sẽ dễ bị thấy chương trình xét đỉnh này xong lại xoay lên đỉnh khác rồi lại về đỉnh này. Nghĩa là thay vì đi đường ngắn nhất, nó sẽ xét lặp lại.
- Để giải quyết tình trạng này, ta sẽ chỉnh sửa input đồ thị vào, bỏ đi những node chung để không bị xét lặp lại. 
- Đó là lí do tại sao, khi mà ta mô hình hoá thủ công bằng tay thì ra được đường ngắn. Mà khi bê lên chương trình thì lại ra đường dài vô cùng, mặc dù code đúng về cách tìm kiếm.

### Nói thêm về tại sao một số code dùng "từ điển dùng từ điển", mà có một số cái lại không sử dụng nó:
- Vì không thể lưu được trọng số dễ dàng
- Truy cập không hiệu quả
- Không phù hợp với các nút không có thứ tự
- Phù hợp sử dụng cho đồ thị có trọng số.

### Tại sao không dùng từ điển lồng từ điển hết luôn cho khoẻ?
- Vì từ điển lồng từ điển chỉ phù hợp cho đồ thị có trọng số, vì chúng ta cần lưu trọng số mỗi cạnh
- Dùng từ điển với danh sách khi đồ thị không có trọng số, vì ta chỉ cần liệt kê các nút kề mà không cần thêm thông tin gì về cạnh đó.





