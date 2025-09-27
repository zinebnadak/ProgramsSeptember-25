#2. Two-dimentional (multi-) list: Chomp

# initialize(board) → creates a 4x10 board with 'X' and 'O'.
# print_board(board) → prints the board nicely.
# get_move(playerNo, board) → gets a valid move from the player.
# update_board(row, col, board) → updates the board according to Chomp rules.
# main() → handles alternating turns and detects when the game ends.

def initialize(board: list[list[str]]):         # Initialize a 4x10 board: 'X' in the top-left corner, 'O' everywhere else.
    rows = 4
    columns = 10
    for r in range(rows):
        row_list = []
        for c in range(columns):
            if r == 0 and c == 0:
                row_list.append("X")            # poisoned candy
            else:
                row_list.append("O")            # normal candy
        board.append(row_list)                    # Add the row to the board


def print_board(board: list[list[str]]):        # Print the current state of the board.
    print("\n+----------+")
    for row in board:
        print("|" + "".join(row) + "|")
    print("+----------+\n")


def get_move(playerNo: int, board: list[list[str]]) -> tuple[int, int]:  # Prompt the player until a valid move is entered.
    while True:
        move = input(f"Spelare {playerNo}: Gör ditt drag! (rad, kolumn): ")
        try:
            row_str, col_str = move.split(",")
            row = int(row_str) - 1  # convert 1-based to 0-based
            col = int(col_str) - 1
        except ValueError:
            print("Fel format! Ange som rad,kolumn t.ex. 2,3")
            continue

        # Check if indices are valid
        if row < 0 or row >= len(board):
            print("Ogiltig rad!")
            continue
        if col < 0 or col >= len(board[0]):
            print("Ogiltig kolumn!")
            continue
        if board[row][col] == " ":
            print("Redan uppäten!")
            continue

        return row, col  # corrected from 'column' to 'col'


def update_board(row: int, col: int, board: list[list[str]]):  # Update the board: remove the selected candy and all below/right of it.
    rows = len(board)
    cols = len(board[0])
    for r in range(row, rows):
        for c in range(col, cols):
            board[r][c] = " "


def main():
    print("Välkommen till Chomp!")
    board = []
    initialize(board)

    player = 1  # Player 1 starts
    print_board(board)

    while True:
        row, col = get_move(player, board)
        update_board(row, col, board)
        print_board(board)

        # Check if the poisoned candy is eaten
        if row == 0 and col == 0:
            print(f"Spelet är slut, spelare {player} har blivit förgiftad!")
            break

        # Switch player
        player = 2 if player == 1 else 1


if __name__ == "__main__":  # ensures that the game runs when the file is executed directly
    main()
