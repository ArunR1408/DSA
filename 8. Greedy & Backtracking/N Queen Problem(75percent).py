def solve_nqueens(n):
    def is_safe(board, row, col):
        for i in range(col):
            if board[i] == row or \
               board[i] - i == row - col or \
               board[i] + i == row + col:
                return False
        return True

    def backtrack(board, col):
        if col == n:
            solutions.append(board[:])
            return
        for row in range(n):
            if is_safe(board, row, col):
                board[col] = row
                backtrack(board, col + 1)

    solutions = []
    backtrack([0] * n, 0)
    return solutions

n = int(input())
solutions = solve_nqueens(n)

if not solutions:
    print("[]")
else:
    for sol in solutions:
        print("[" + " ".join(str(x + 1) for x in sol) + " ]", end=" ")
print()