def is_safe(board, row, col, n): 
    for i in range(row): 
        if board[i][col] == 1: 
            return False 
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False 
    for i, j in zip(range(row, -1, -1), range(col, n)): 
        if board[i][j] == 1: 
            return False 
    return True 

def solve_n_queens_util(board, row, n, solutions): 
    if row == n: 
        solutions.append([row[:] for row in board]) 
        return 0
    for col in range(n): 
        if is_safe(board, row, col, n): 
            board[row][col] = 1 
            solve_n_queens_util(board, row + 1, n, solutions) 
            board[row][col] = 0 # Backtrack 

def solve_n_queens(n): 
    board = [[0] * n for _ in range(n)] 
    solutions = [] 
    solve_n_queens_util(board, 0, n, solutions) 
    return solutions 

def print_board(board): 
    for row in board: 
        print(' '.join('Q' if cell == 1 else '.' for cell in row)) 

# Example usage: 
n = 4
solutions = solve_n_queens(n) 
print(f"Total solutions for {n}-Queens problem:", len(solutions)) 
for idx, sol in enumerate(solutions, start=1): 
    print(f"Solution {idx}:") 
    print_board(sol) 
    print()