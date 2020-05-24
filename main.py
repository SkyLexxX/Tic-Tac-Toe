from tabulate import tabulate

from logic.check import *

CELLS = [[".", ".", "."],
         [".", ".", "."],
         [".", ".", "."]]
ROWS, COLS = 3, 3
PLAYER_1_FIGURE, PLAYER_2_FIGURE = "X", "O"
FONT = "\033[1m"


def print_grid(matrix):
    return tabulate(matrix, tablefmt="psql")


def main():
    counter = 0
    player_turn = PLAYER_1_FIGURE
    while counter < (ROWS * COLS) and not check_for_winner(CELLS, player_turn):
        x, y = [int(x) for x in input(f"{FONT}Player-{player_turn} turn\nEnter the coordinates: ").split()]
        if x > 3 or y > 3:
            print("You picked the wrong house fool")
        else:
            if check_if_cell_is_empty(x, y):
                if player_turn is PLAYER_1_FIGURE:
                    CELLS[x - 1][y - 1] = PLAYER_1_FIGURE
                    player_turn = PLAYER_2_FIGURE
                else:
                    CELLS[x - 1][y - 1] = PLAYER_2_FIGURE
                    player_turn = PLAYER_1_FIGURE
                print(print_grid(CELLS))
                counter += 1
            else:
                print("This cell is already chosen by your opponent")
    if player_turn is PLAYER_1_FIGURE:
        player_turn = PLAYER_2_FIGURE
    else:
        player_turn = PLAYER_1_FIGURE

    print("Game over")
    print(f"Winner is Player-{player_turn}:")
    exit()


if __name__ == '__main__':
    main()
