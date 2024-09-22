import sys

N = int(sys.stdin.readline())

def solve_n_queens(n):
    def place_queens(col):
        if col == n:
            return 1
        count = 0
        for row in range(n):
            if not (rows[row] or diagonals1[row + col] or diagonals2[row - col + n - 1]):
                rows[row] = diagonals1[row + col] = diagonals2[row - col + n - 1] = True
                count += place_queens(col + 1)
                rows[row] = diagonals1[row + col] = diagonals2[row - col + n - 1] = False
        return count

    rows = [False] * n
    diagonals1 = [False] * (2 * n - 1)  # 오른쪽 상단으로 향하는 대각선
    diagonals2 = [False] * (2 * n - 1)  # 왼쪽 상단으로 향하는 대각선
    return place_queens(0)

print(solve_n_queens(N))

