from tabulate import tabulate

CELLS = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
ROWS, COLS = 3, 3
PLAYER_1_FIGURE = "X"
PLAYER_2_FIGURE = "O"
FONT = "\033[1m"


def print_grid(matrix):
    return tabulate(matrix, tablefmt="psql")


def check_if_cell_is_empty(x, y):
    if CELLS[x-1][y-1] == ".":
        return True
    return False


def main():
    counter = 0
    player_turn = 0
    while counter < (ROWS*COLS):
        x, y = [int(x) for x in input(f"{FONT}Player-{player_turn+1} turn\nEnter the coordinates: ").split()]
        if x > 3 or y > 3:
            print("You picked the wrong house fool")
        else:
            if check_if_cell_is_empty(x, y):
                if player_turn == 0:
                    CELLS[x-1][y-1] = PLAYER_1_FIGURE
                    player_turn = 1
                else:
                    CELLS[x - 1][y - 1] = PLAYER_2_FIGURE
                    player_turn = 0
                print(print_grid(CELLS))
                counter += 1
            else:
                print("This cell is already chosen by your opponent")


if __name__ == '__main__':
    main()
