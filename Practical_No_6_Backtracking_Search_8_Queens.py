N = 8


# Function to print the chessboard
def printSolution(board):
    print("Solution:")

    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


# Function to check whether a queen can be placed
def isSafe(board, row, col):

    # Check left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col

    while i < N and j >= 0:
        if board[i][j] == 1:
            return False

        i += 1
        j -= 1

    return True


# Recursive function to solve the problem
def solveNQUtil(board, col):

    # Base case: All queens are placed
    if col >= N:
        return True

    # Try placing queen in each row
    for i in range(N):
        if isSafe(board, i, col):

            # Place the queen
            board[i][col] = 1

            # Recur for next column
            if solveNQUtil(board, col + 1):
                return True

            # Backtrack
            board[i][col] = 0

    return False


# Main function
def solveNQ():

    # Create an 8 × 8 chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solveNQUtil(board, 0):
        print("Solution does not exist")
        return False

    printSolution(board)
    return True


# Driver Code
solveNQ()

# Algorithm

# 1. Start with the first column.
# 2. If all columns are filled, print the solution and stop.
# 3. For each row in the current column:
#     a. Check whether placing a queen is safe.
#     b. If the position is safe:
#         i. Place the queen.
#         ii. Recursively place a queen in the next column.
#         iii. If successful, return TRUE.
#         iv. Otherwise, remove the queen (Backtrack).
# 4. If no safe position exists in the current column, Return FALSE.
