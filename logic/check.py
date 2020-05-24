from main import CELLS


def check_if_cell_is_empty(x, y):
    if CELLS[x - 1][y - 1] == ".":
        return True
    return False


def check_rows(row, matrix):
    row = set([matrix[row][i] for i in range(len(matrix))])
    if len(row) == 1 and "." not in row:
        return True


def check_cols(col, matrix):
    row = set([matrix[i][col] for i in range(len(matrix))])
    if len(row) == 1 and "." not in row:
        return True


def check_diagonals(matrix):
    first_diagonal = set([matrix[i][i] for i in range(len(matrix))])
    second_diagonal = set([matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))])

    if len(first_diagonal) == 1 and "." not in first_diagonal \
            or len(second_diagonal) == 1 and "." not in second_diagonal:
        return True


def check_for_winner(matrix):
    for i in range(0, len(matrix)):
        if check_rows(i, matrix):
            return True
        if check_cols(i, matrix):
            return True
        if check_diagonals(matrix):
            return True
    return False
