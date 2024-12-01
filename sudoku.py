def is_valid(num, row, col, board):
    """
    Check if placing a number in a specific cell is valid.
    :param num: Number to place (1-9)
    :param row: Row index
    :param col: Column index
    :param board: Current Sudoku board
    :return: True if valid, False otherwise
    """
    # Check row
    if num in board[row]:
        return False
    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False
    # Check 3x3 grid
    box_row, box_col = row // 3 * 3, col // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    return True


def is_board_valid(board):
    """
    Check if the initial board is valid by ensuring no duplicates in rows, columns, and grids.
    :param board: 9x9 Sudoku board
    :return: True if valid, False otherwise
    """
    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != 0:
                # Temporarily clear the cell to avoid self-check
                board[row][col] = 0
                if not is_valid(num, row, col, board):
                    return False
                # Restore the cell
                board[row][col] = num
    return True


def solve_sudoku(board):
    """
    Solves a Sudoku puzzle.
    :param board: A 9x9 2D list representing the Sudoku board
    :return: Solved board or None if unsolvable or invalid
    """
    # Check if board size is valid (must be 9x9)
    if len(board) != 9 or any(len(row) != 9 for row in board):
        return None  # Invalid board size

    # Check if all elements are integers between 0 and 9
    if any(
        not isinstance(cell, int) or not (0 <= cell <= 9)
        for row in board
        for cell in row
    ):
        return None  # Invalid element(s) in the board

    if not is_board_valid(board):
        return None  # Invalid board content

    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:  # Find the first empty cell
                    for num in range(1, 10):  # Try numbers 1-9
                        if is_valid(num, i, j, board):
                            board[i][j] = num
                            if backtrack():
                                return True
                            board[i][j] = 0  # Undo assignment
                    return False  # No valid numbers
        return True

    if not backtrack():  # If the board is unsolvable
        return None
    return board


if __name__ == "__main__":
    # Valid Sudoku puzzle
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    # Invalid Sudoku puzzle (duplicate 5 in the first row)
    invalid_puzzle = [
        [5, 5, 0, 0, 7, 0, 0, 0, 0],  # Invalid duplicate 5 in row
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Valid board test:")
    solution = solve_sudoku(puzzle)
    if solution:
        for row in solution:
            print(row)
    else:
        print("The puzzle is unsolvable or invalid.")

    print("\nInvalid board test:")
    invalid_solution = solve_sudoku(invalid_puzzle)
    print(invalid_solution)  # Should print None
