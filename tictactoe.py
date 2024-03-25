def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)
def check_winner(board):

    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        row = int(input("Enter row (1, 2, 3): ")) - 1
        col = int(input("Enter column (1, 2, 3): ")) - 1
        if board[row][col] == " ":
            board[row][col] = player
            print_board(board)
            if check_winner(board):
                print(f"Player {player} wins!")
                break
            elif all(board[i][j] != " " for i in range(3) for j in range(3)):
                print("It's a draw!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken. Try again.")
main()