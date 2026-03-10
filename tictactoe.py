# build a simple in-terminal tictactoe game

def print_board(board, n):
    for i, row in enumerate(board):
        print(" " + " | ".join(row) + " ")
        if i < n-1:
            print("-"*(n*4 - 1))


# takes in user input and returns list [row, column]
def position_translator(pick, n):
    row = (pick) // n
    column = (pick) % n
    return row, column


def get_move(board, player, n):
    while True:
        try:
            pick = int(input(f"Player {player}, where do you want to go? ")) - 1
            row, column = position_translator(pick, n)
    
            if 0 <= pick <= (n**2 - 1) and board[row][column] == " ":
                return row, column
            elif 0 <= pick <= (n**2 - 1):
                print(f"Position {pick + 1} is already taken! Try again.")
    
            else:
                print(f"This position is out of bounds! Try again.")
    
        except ValueError:
            print("Your selection could not be understood. Try again.")


def win_detector(board, n):
    # check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != " ": return row[0]

    # check columns, first by creating a list of columns
    for col in range(n):
        columns = [board[row][col] for row in range(n)]
        if len(set(columns)) == 1 and columns[0] != " ": return columns[0]

    # check diagonals
    main_diagonal = [board[i][i] for i in range(n)]
    if len(set(main_diagonal)) == 1 and main_diagonal[0] != " ": return main_diagonal[0]
    anti_diagonal = [board[i][n-1-i] for i in range(n)]
    if len(set(anti_diagonal)) == 1 and anti_diagonal[0] != " ": return anti_diagonal[0]

def main():
    # present instructions, position map
    n = 3
    print(f"Welcome to Charity's fabulous tic-tac-toe!")
    position_map = [[f"{i + 1}" for i in range(n * j, n * (j + 1))] for j in range(n)]
    print(f"\nCheck out the position map that you will use to select your moves: ")
    print_board(position_map, n)

    while True:
        # initialize the game state
        board = [[" " for _ in range(n)] for _ in range(n)]
        current_player = "X"
        turn = 0
        max_turns = n**2

        # game loop
        while turn < max_turns:
            current_player = turn % 2 + 1
            # show the current board and prompt user for selection
            row, column = get_move(board, current_player, n)

            # update the board and show to players
            if current_player == 1: board[row][column] = "X"
            if current_player == 2: board[row][column] = "O"
            # how do I add an undo feature? like when your mom steals you move :)

            print(f"\nNice move! Here is the current board: ")
            print_board(board, n)

            win = win_detector(board, n)

            if win == "X":
                print(f"\nPlayer {current_player} wins! Nicely done.")
                turn = n**2 - 1

            if win == "O":
                print(f"\nPlayer {current_player} wins! Nicely done.")
                turn = n**2 - 1

            turn = turn + 1

            if turn == n**2 and not win:
                print(f"It's a draw! You must be a good match.")
        again = input("\nWould you like to play again? (y/n): ").lower()
        if again != 'y':
            print(f"\nThank you for playing Charity's fabulous tic-tac-toe!")
            break

if __name__ == "__main__":
    main()


