def print_board(board):
    print("\n    " + "   ".join([str(i + 1) for i in range(len(board))]))
    for i, row in enumerate(board):
        row_str = f"{i + 1} " + " | ".join(row)
        print(row_str)
        if i != len(board) - 1:
            print("   " + "----" * len(row))


def get_move(player_name, turn, board):
    while True:
        try:
            row = int(input(f"{player_name} ({turn}), enter Row (1-{len(board)}): "))
            col = int(input(f"{player_name} ({turn}), enter Col (1-{len(board)}): "))
        except ValueError:
            print("❌ Please enter valid numbers!")
            continue

        if row < 1 or row > len(board):
            print("❌ Invalid row, try again.")
            continue
        elif col < 1 or col > len(board[row - 1]):
            print("❌ Invalid column, try again.")
            continue
        elif board[row - 1][col - 1] != " ":
            print("❌ Cell already taken, try again.")
        else:
            break

    board[row - 1][col - 1] = turn


def check_win(board, turn):
    size = len(board)
    win_condition = 4  # First to 4 in a row

    # Check rows
    for row in board:
        count = 0
        for cell in row:
            if cell == turn:
                count += 1
                if count == win_condition:
                    return True
            else:
                count = 0

    # Check columns
    for col in range(size):
        count = 0
        for row in range(size):
            if board[row][col] == turn:
                count += 1
                if count == win_condition:
                    return True
            else:
                count = 0

    # Check diagonals (top-left to bottom-right)
    for row in range(size - win_condition + 1):
        for col in range(size - win_condition + 1):
            count = 0
            for i in range(win_condition):
                if board[row + i][col + i] == turn:
                    count += 1
                    if count == win_condition:
                        return True
                else:
                    break

    # Check diagonals (top-right to bottom-left)
    for row in range(size - win_condition + 1):
        for col in range(win_condition - 1, size):
            count = 0
            for i in range(win_condition):
                if board[row + i][col - i] == turn:
                    count += 1
                    if count == win_condition:
                        return True
                else:
                    break

    return False


def play_game(player1, player2, scores):
    size = 5  # 5x5 board
    board = [[" " for _ in range(size)] for _ in range(size)]

    turn = "X"
    turn_number = 0
    max_turns = size * size
    print_board(board)

    while turn_number < max_turns:
        current_player = player1 if turn == "X" else player2

        get_move(current_player, turn, board)
        print_board(board)

        if check_win(board, turn):
            print(f"🎉 Congratulations {current_player}! You won this round.")
            scores[current_player] += 1
            break

        if turn == "X":
            turn = "O"
        else:
            turn = "X"

        turn_number += 1

    if turn_number == max_turns and not check_win(board, turn):
        print("🤝 It's a tie!")

    print(f"\n🏆 Current Scores:")
    print(f"{player1}: {scores[player1]}")
    print(f"{player2}: {scores[player2]}\n")

    play_again = input("Do you want to play another round? (y/n): ").lower()
    if play_again == 'y':
        play_game(player1, player2, scores)
    else:
        print("🎮 Game Over! Final Scores:")
        print(f"{player1}: {scores[player1]}")
        print(f"{player2}: {scores[player2]}")
        print("Thank you for playing! 👋")


# Game start
print("Welcome to 5x5 Tic-Tac-Toe (First to 4 in a Row)!")
player1 = input("Enter Player 1 name (X): ")
player2 = input("Enter Player 2 name (O): ")
scores = {player1: 0, player2: 0}

play_game(player1, player2, scores)
