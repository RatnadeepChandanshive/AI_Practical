import math

# Initialize board
board = [' ' for _ in range(9)]

# Display board
def print_board():
    print()

    for i in range(3):
        print(
            " " + board[i * 3]
            + " | " + board[i * 3 + 1]
            + " | " + board[i * 3 + 2]
        )

        if i < 2:
            print("---|---|---")

    print()

# Check winner
def check_winner(player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True

    return False


# Check draw
def is_draw():
    return ' ' not in board

# Minimax Algorithm
def minimax(is_max):
    if check_winner('O'):
        return 1

    if check_winner('X'):
        return -1

    if is_draw():
        return 0

    if is_max:
        best = -math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best = max(best, score)

        return best

    else:
        best = math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best = min(best, score)

        return best


# AI Move
def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    board[move] = 'O'

# Human Move
def human_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1

            if 0 <= pos < 9 and board[pos] == ' ':
                board[pos] = 'X'
                break
            else:
                print("Invalid move. Try again.")

        except ValueError:
            print("Enter a valid number.")

# Main Game
print("Positions are:")
print("1 | 2 | 3")
print("--|---|--")
print("4 | 5 | 6")
print("--|---|--")
print("7 | 8 | 9")

while True:
    print_board()
    human_move()

    if check_winner('X'):
        print_board()
        print("You Win!")
        break

    if is_draw():
        print_board()
        print("It's a Draw!")
        break

    ai_move()

    if check_winner('O'):
        print_board()
        print("AI Wins!")
        break

    if is_draw():
        print_board()
        print("It's a Draw!")
        break

# Algorithm

# 1. Start with the current game state as the root of the game tree.
# 2. Generate all legal moves for the current player.
# 3. Recursively expand the game tree, alternating between the maximizing player (MAX) and the minimizing player (MIN).
# 4. Stop when a terminal state is reached (win, loss, or draw), or at a specified depth if using a cutoff.
# 5. Assign utility values to terminal states (or evaluation-function values at the cutoff depth).
# 6. Back up the values through the tree:
#     a. At MAX nodes, choose the maximum child value.
#     b. At MIN nodes, choose the minimum child value.
# 7. Select the move from the root that has the highest minimax value.
