grid = [
    ['S', '.', '.', '.', '.'],
    ['X', '.', 'X', '.', '.'],
    ['.', '.', '.', 'X', '.'],
    ['.', 'X', '.', '.', '.'],
    ['.', '.', '.', '.', 'G']
]

row = 0
col = 0
visited = []

while True:
    visited.append((row, col))
    print("Current Position:", (row, col))

    if grid[row][col] == 'G':
        print("Goal")
        break

    if col < 4 and grid[row][col + 1] != 'X':
        col = col + 1

    elif row < 4 and grid[row + 1][col] != 'X':
        row = row + 1

    else:
        print("Path not found")
        break

print("Visited Cells:", visited)

# Algorithm

# 1. Start.
# 2. Create a grid with free cells, obstacles, start, and goal.
# 3. Initialize the agent at the start position.
# 4. Create an empty visited list (internal state).
# 5. Store the current position in the visited list.
# 6. If the current position is the goal, stop.
# 7. Otherwise:
#     - Move Right if the next cell is free.
#     - Else move Down if the next cell is free.
#     - If neither move is possible, display “No Path Found”.
# 8. Repeat until the goal is reached.
# 9. Display the visited cells.
# 10. Stop.
