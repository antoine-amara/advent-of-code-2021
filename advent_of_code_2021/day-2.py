import pandas as pd

# move direction
HORIZONTAL = "horizontal"
DEPTH = "depth"
AIM = "aim"

# move list
FORWARD = "forward"
DOWN = "down"
UP = "up"


def read_input(input_name="example.txt"):
    path = f"advent_of_code_2021/data/day-2/{input_name}"
    df = pd.read_csv(path, delimiter=" ", header=None, names=["command", "units"])
    return df


def execute_one_move_part_1(currentPositions, *, command, units):
    if command == FORWARD:
        currentPositions[HORIZONTAL] += units
        return

    if command == DOWN:
        currentPositions[DEPTH] += units
        return

    if command == UP:
        currentPositions[DEPTH] -= units
        return


def execute_one_move_part_2(currentPositions, *, command, units):
    if command == FORWARD:
        currentPositions[HORIZONTAL] += units
        currentPositions[DEPTH] += currentPositions[AIM] * units
        return

    if command == DOWN:
        currentPositions[AIM] += units

    if command == UP:
        currentPositions[AIM] -= units


def execute_move_plan(move_plan, *, move_executor):
    positions = {
        HORIZONTAL: 0,
        DEPTH: 0,
        # AIM is used only on part 2
        AIM: 0,
    }

    for _, move in move_plan.iterrows():
        move_executor(positions, command=move["command"], units=move["units"])

    return positions


def part1():
    move_plan = read_input("input.txt")
    positions_after_moves = execute_move_plan(move_plan, move_executor=execute_one_move_part_1)
    return positions_after_moves[HORIZONTAL] * positions_after_moves[DEPTH]


def part2():
    move_plan = read_input("input.txt")
    positions_after_moves = execute_move_plan(move_plan, move_executor=execute_one_move_part_2)
    return positions_after_moves[HORIZONTAL] * positions_after_moves[DEPTH]


def main():
    # part 1: make some moves and multiply horizontal and depth.
    # It take care of the horizontal and depth for each moves
    response_part1 = part1()
    print("Day 2 -- part 1")
    print(f"Response: {response_part1}\n")
    assert response_part1 == 1654760
    # part 2: make some moves and multiply horizontal and depth.
    # It take care of the horizontal, the depth adn the aim for each moves
    response_part2 = part2()
    print("Day 2 -- part 2")
    print(f"Response: {response_part2}")
    assert response_part2 == 1956047400


main()
