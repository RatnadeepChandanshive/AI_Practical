def reflex_agent(location, room_status):
    if room_status[location] == "Dirty":
        print(f"Room {location} is dirty")
        print("Action: SUCK")
        room_status[location] = "Clean"
    else:
        if location == "A":
            print("Room A is clean")
            print("Action: Move Right to room B")
            location = "B"
        else:
            print("Room B is clean")
            print("Action: Move Left to room A")
            location = "A"

    return location, room_status


print("=== Vacuum-Cleaner World Setup ===")

while True:
    location = input(
        "Enter initial location of the agent (A or B): "
    ).strip().upper()

    if location in ["A", "B"]:
        break

    print("Invalid input! Please enter either 'A' or 'B'.")


while True:
    status_A = input(
        "Enter status for Room A (Clean or Dirty): "
    ).strip().capitalize()

    if status_A in ["Clean", "Dirty"]:
        break

    print("Invalid input! Please enter 'Clean' or 'Dirty'.")


while True:
    status_B = input(
        "Enter status for Room B (Clean or Dirty): "
    ).strip().capitalize()

    if status_B in ["Clean", "Dirty"]:
        break

    print("Invalid input! Please enter 'Clean' or 'Dirty'.")


room_status = {
    "A": status_A,
    "B": status_B
}

print("\n--- Simulation Started ---")
print("Initial Environment Status:", room_status)
print(f"Agent starts in Room: {location}\n")


while True:
    location, room_status = reflex_agent(location, room_status)

    if room_status["A"] == "Clean" and room_status["B"] == "Clean":
        print("\nBoth rooms are clean!")
        print("Action: No Operation (NoOp)")
        break