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