import heapq

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)


def heuristic(state):
    distance = 0

    for tile in range(1, 9):
        current = state.index(tile)
        goal_pos = goal.index(tile)

        current_row, current_col = divmod(current, 3)
        goal_row, goal_col = divmod(goal_pos, 3)

        distance += (
            abs(current_row - goal_row)
            + abs(current_col - goal_col)
        )

    return distance


def neighbours(state):
    result = []
    blank = state.index(0)
    row, col = divmod(blank, 3)

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in moves:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_blank = nr * 3 + nc
            new_state = list(state)

            new_state[blank], new_state[new_blank] = (
                new_state[new_blank],
                new_state[blank]
            )

            result.append(tuple(new_state))

    return result


def print_state(state):
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])


def a_star(start):
    open_list = []

    heapq.heappush(
        open_list,
        (heuristic(start), 0, start)
    )

    parent = {}
    parent[start] = None

    g_score = {}
    g_score[start] = 0

    visited = set()
    step = 0

    while open_list:
        f, g, current = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)

        print("\n--------------------------------")
        print("Step", step)
        print("--------------------------------")

        print_state(current)
        print()
        print("g =", g)
        print("h =", heuristic(current))
        print("f =", f)

        step += 1

        if current == goal:
            print("\nGoal Found!")

            path = []
            node = current

            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()

            print("\n========== Solution Path ==========\n")

            for i, state in enumerate(path):
                print("Move", i)
                print_state(state)
                print()

            print("Total Moves =", len(path) - 1)
            return

        for child in neighbours(current):
            new_g = g + 1

            if child not in g_score or new_g < g_score[child]:
                g_score[child] = new_g
                parent[child] = current

                new_f = new_g + heuristic(child)

                heapq.heappush(
                    open_list,
                    (new_f, new_g, child)
                )

    print("No Solution Found")


a_star(start)

# Algorithm 

# 1. Create a search graph G, consisting solely of the start node, no. Put no on a list called OPEN.
# 2. Create a list called CLOSED that is initially empty.
# 3. If OPEN is empty, exit with failure.
# 4. Select the first node on OPEN, remove it from OPEN, and put it on CLOSED. Called this node n.
# 5. If n is a goal node, exit successfully with the solution obtained by tracing a path along the pointers from n to no in G. (The pointers define a search tree and are established in Step 7)
# 6. Expand node n, generating the set M, of its successors that are not already ancestors of n in G. Install these members of M as successors of n in G.
# 7. Establish a pointer to n from each of those members of M that were not already in G (i.e., not already on either OPEN or CLOSED). Add these members of M to OPEN. For each member, m, of M that was already on OPEN or CLOSED, redirect its pointer to n if the best path to m found so far is through n. For each member of M already on CLOSED, redirect the pointers of each of its descendants in G so that they point backward along the best paths found so far to these descendants.
# 8. Reorder the list OPEN in order of increasing f values. (Ties among minimal f values are resolved in favor of the deepest node in the search tree.)
# 9. Go to Step 3.
