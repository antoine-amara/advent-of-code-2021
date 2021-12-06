from helpers.input_parser import parse_list_elements_to_int, read_input_lines


def read_input(input_name="example.txt"):
    raw_data = read_input_lines(day=6, input_name=input_name)
    parsed_data = parse_list_elements_to_int(raw_data[0].split(","))
    return parsed_data


def generate_fishlantern_state(*, initial_state=[], nb_days=80):
    fishlantern_state = initial_state
    for _ in range(0, nb_days):
        next_state = []
        new_fishlantern = []
        for fishlantern in fishlantern_state:
            if fishlantern == 0:
                next_state.append(6)
                new_fishlantern.append(6 + 2)
            else:
                next_state.append(fishlantern - 1)

        fishlantern_state = next_state + new_fishlantern

    return fishlantern_state


def part1():
    data = read_input("input.txt")
    final_fishlantern_state = generate_fishlantern_state(initial_state=data, nb_days=80)
    return len(final_fishlantern_state)


def part2():
    print("part2")


def main():
    # part 1: count fishlantern reproduction on 80 days
    response_part1 = part1()
    print("Day 6 -- part 1")
    print(f"Response: {response_part1}\n")
    assert response_part1 == 346063
    # part 2: count fishlantern reproduction on 256 days
    response_part2 = part2()
    print("Day 6 -- part 2")
    print(f"Response: {response_part2}")


main()
