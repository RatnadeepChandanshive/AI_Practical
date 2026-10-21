from collections import deque


def get_successors(state):
    successors = []

    for i in range(3):
        if state[i]:
            disk = state[i][-1]

            for j in range(3):
                if i != j:
                    if not state[j] or state[j][-1] > disk:
                        new_state = [list(peg) for peg in state]

                        new_state[i].pop()
                        new_state[j].append(disk)

                        successors.append(
                            tuple(tuple(peg) for peg in new_state)
                        )

    return successors


def bfs_tower_of_hanoi(n):
    start = (tuple(range(n, 0, -1)), (), ())
    goal = ((), (), tuple(range(n, 0, -1)))

    queue = deque([(start, [])])
    visited = set()
    visited.add(start)

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        for next_state in get_successors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [state]))

    return None


def print_solution(solution):
    print("\nSolution Steps:\n")

    for step, state in enumerate(solution):
        print(f"Step {step}")
        print("A:", list(state[0]))
        print("B:", list(state[1]))
        print("C:", list(state[2]))
        print("-" * 25)


n = int(input("Enter number of disks: "))

solution = bfs_tower_of_hanoi(n)

if solution:
    print_solution(solution)
    print("Total Moves =", len(solution) - 1)
else:
    print("No Solution Found")