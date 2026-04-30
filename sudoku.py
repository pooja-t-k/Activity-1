def solveSudoku(board):
    
    def isValid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num:
                return False
        for i in range(9):
            if board[i][col] == num:
                return False

        startRow = (row // 3) * 3
        startCol = (col // 3) * 3

        for i in range(3):
            for j in range(3):
                if board[startRow + i][startCol + j] == num:
                    return False

        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    for num in "123456789":
                        if isValid(board, row, col, num):
                            board[row][col] = num

                            if backtrack():
                                return True

                            board[row][col] = "."  

                    return False
        return True

    backtrack()

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solveSudoku(board)

print("Solved Sudoku:")
for row in board:
    print(row)
