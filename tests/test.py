import unittest

from logic.check import check_for_winner


class TicTacToe(unittest.TestCase):
    def test_output_1(self):
        CELLS = [["X", "X", "X"],
                 ["O", "O", "."],
                 [".", ".", "."]]
        is_win = check_for_winner(CELLS)
        self.assertEqual(is_win, True, 'An error occurred while processing your request')

    def test_output_2(self):
        CELLS = [["O", "O", "."],
                 ["X", "X", "."],
                 [".", ".", "X"]]
        is_win = check_for_winner(CELLS)
        self.assertEqual(is_win, False, 'An error occurred while processing your request')

    def test_output_3(self):
        CELLS = [[".", ".", "."],
                 ["O", "O", "."],
                 ["X", "X", "X"]]
        is_win = check_for_winner(CELLS)
        self.assertEqual(is_win, True, 'An error occurred while processing your request')

    def test_output_4(self):
        CELLS = [["X", ".", "X"],
                 [".", ".", "O"],
                 ["X", ".", "O"]]
        is_win = check_for_winner(CELLS)
        self.assertEqual(is_win, False, 'An error occurred while processing your request')

    def test_output_5(self):
        CELLS = [[".", "X", "."],
                 [".", "X", "O"],
                 [".", "X", "O"]]
        is_win = check_for_winner(CELLS)
        self.assertEqual(is_win, True, 'An error occurred while processing your request')

    def test_output_6(self):
        CELLS = [[".", ".", "X"],
                 [".", "X", "O"],
                 [".", "X", "O"]]
        is_win = check_for_winner(CELLS)
        self.assertEqual(is_win, False, 'An error occurred while processing your request')

    def test_output_7(self):
        CELLS = [["X", ".", "X"],
                 [".", "X", "O"],
                 [".", ".", "O"]]
        is_win = check_for_winner(CELLS)
        self.assertEqual(is_win, False, 'An error occurred while processing your request')

    def test_output_8(self):
        CELLS = [["X", ".", "O"],
                 [".", "X", "O"],
                 [".", ".", "X"]]
        is_win = check_for_winner(CELLS)
        self.assertEqual(is_win, True, 'An error occurred while processing your request')

    def test_output_9(self):
        CELLS = [["X", "X", "O"],
                 [".", "O", "X"],
                 ["O", ".", "X"]]
        is_win = check_for_winner(CELLS)
        self.assertEqual(is_win, True, 'An error occurred while processing your request')

    def test_output_10(self):
        CELLS = [[".", ".", "."],
                 [".", ".", "."],
                 [".", ".", "."]]
        is_win = check_for_winner(CELLS)
        self.assertEqual(is_win, False, 'An error occurred while processing your request')
