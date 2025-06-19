import numpy as np

def is_valid_state(state, num_queens):
    return len(state) == num_queens

def get_candidates(state, num_queens):
    if not state:
        return range(num_queens)

    position = len(state)
    candidates = set(range(num_queens))

    for row, col in enumerate(state):
        candidates.discard(col)
        # Calculate distance between current position and previous queen's row
        dist = position - row
        candidates.discard(col + dist)
        candidates.discard(col - dist)

    return candidates

def search(state, solutions, num_queens):
    if is_valid_state(state, num_queens):
        solutions.append(state.copy())
        return
    
    for candidate in get_candidates(state, num_queens):
        state.append(candidate)
        search(state, solutions, num_queens)
        print(f"Backtracking from state: {state}")
        state.remove(candidate)

def solve(num_queens):
    solutions = []
    state = []
    search(state, solutions, num_queens)
    return solutions

if __name__ == "__main__":
    # nhập số lượng và in bàng cớ trắng
    num_queens = int(input("Nhap so luong quan hau: "))
    
    empty_board = np.full((num_queens, num_queens), "-")
    print(empty_board)
    solutions = solve(num_queens)
    print(f"\n tong loi giai tim duoc: {len(solutions)}")
    for index, solution in enumerate(solutions, start=1):
        board = np.full((num_queens, num_queens), "-")
        for row, col in enumerate(solution):
            board[row][col] = 'Q'
        print(f"\n Loi giai {index}: {solution}")
        print(board)
        for row in board:
            print(" ".join(row))

        print("Toa do cac quan hau (hàng, cột):", end=" ")
        coordinates = []
        for row, col in enumerate(solution):
            coordinates.append(f"({row}, {col})")
        print(", ".join(coordinates))