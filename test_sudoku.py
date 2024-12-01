import unittest
from sudoku import solve_sudoku

class TestSudokuSolver(unittest.TestCase):
    def test_valid_sudoku(self):
        """Test a valid Sudoku puzzle."""
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
        solution = solve_sudoku(puzzle)
        self.assertIsNotNone(solution)

    def test_unsolvable_sudoku(self):
        """Test an unsolvable Sudoku puzzle."""
        unsolvable = [
            [5, 5, 0, 0, 7, 0, 0, 0, 0],  # Invalid: duplicate 5 in the first row
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.assertIsNone(solve_sudoku(unsolvable))

    def test_empty_sudoku(self):
        """Test a completely empty Sudoku puzzle."""
        puzzle = [[0] * 9 for _ in range(9)]
        solution = solve_sudoku(puzzle)
        self.assertIsNotNone(solution)  # The empty board should be solvable

    def test_already_solved_sudoku(self):
        """Test an already solved Sudoku puzzle."""
        solved = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        solution = solve_sudoku(solved)
        self.assertEqual(solution, solved)

    def test_invalid_board_size(self):
        """Test a board that is not 9x9."""
        invalid_board = [[0] * 8 for _ in range(8)]  # 8x8 board
        self.assertIsNone(solve_sudoku(invalid_board))

    def test_non_numeric_input(self):
        """Test a board with invalid (non-numeric) inputs."""
        invalid_board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, "X", 0, 1, 9, 5, 0, 0, 0],  # Invalid: "X"
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.assertIsNone(solve_sudoku(invalid_board))

if __name__ == '__main__':
    unittest.main()
