import tkinter as tk
from tkinter import messagebox

def solve_sudoku(board):
    # Find the next empty cell
    empty = find_empty_location(board)
    if not empty:
        return True  # Puzzle solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Backtrack
    return False

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, row, col, num):
    # Check if num is not in the current row
    if num in board[row]:
        return False

    # Check if num is not in the current column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check if num is not in the current 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.board = [[0] * 9 for _ in range(9)]

        self.entries = [[tk.Entry(root, width=5, font=('Arial', 18), justify='center') for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.entries[i][j].grid(row=i, column=j, padx=5, pady=5)
                self.entries[i][j].bind("<FocusOut>", self.update_board)

        self.solve_button = tk.Button(root, text="Solve", command=self.solve)
        self.solve_button.grid(row=10, column=0, columnspan=9, pady=10)

    def update_board(self, event=None):
        for i in range(9):
            for j in range(9):
                try:
                    value = int(self.entries[i][j].get())
                    self.board[i][j] = value if 1 <= value <= 9 else 0
                except ValueError:
                    self.board[i][j] = 0

    def solve(self):
        self.update_board()
        if solve_sudoku(self.board):
            self.display_board()
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists!")

    def display_board(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(self.board[i][j]))

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()
