def print_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def check_win(board, player):
    # Check rows
    for row in board:
        if all(symbol == player for symbol in row):
            return True
    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == player for row in range(len(board))):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(len(board))):
        return True
    if all(board[i][len(board)-i-1] == player for i in range(len(board))):
        return True
    return False

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    while True:
        print_board(board)
        player = players[current_player]
        print(f"Player {player}'s turn.")
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1
        if board[row][col] == " ":
            board[row][col] = player
            if check_win(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                return
            if check_tie(board):
                print_board(board)
                print("Tie game!")
                return
            current_player = (current_player + 1) % 2
        else:
            print("That spot is already taken. Please choose another spot.")

play_game()
