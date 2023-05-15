def print_board(board):
    print("-------------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(" " + cell + " |", end="")
        print("\n-------------")

def is_winner(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    current_player = "X"

    while True:
        print_board(board)

        # Get player's move
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        # Check if the move is valid
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check if the current player wins
        if is_winner(board, current_player):
            print_board(board)
            print("Player", current_player, "wins!")
            break

        # Check if it's a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch to the other player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

# Start the game
play_game()
