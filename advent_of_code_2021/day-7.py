from helpers.input_parser import parse_list_elements_to_int, read_input_lines


def sum_numbers_zero_to_N(N):
    return round((N * (N + 1) / 2))


def read_input(input_name="example.txt"):
    raw_data = read_input_lines(day=7, input_name=input_name)
    parsed_data = parse_list_elements_to_int(raw_data[0].split(","))
    return parsed_data


def compute_least_fuel_consumption_1_fuel_each_move(inputs):
    inputs_fuel_consumption = {}
    min_point = min(inputs)
    max_point = max(inputs)
    for input_to_compare in range(min_point, max_point):
        distance_fuel_consumption = sum(
            [
                abs(input_to_compare - point_to_compare)
                for point_to_compare in inputs
                if point_to_compare != input_to_compare
            ]
        )
        inputs_fuel_consumption[input_to_compare] = distance_fuel_consumption

    key_min = min(inputs_fuel_consumption, key=inputs_fuel_consumption.get)
    return inputs_fuel_consumption[key_min]


def compute_least_fuel_consumption_plus_1_fuel_each_move(inputs):
    inputs_fuel_consumption = {}
    min_point = min(inputs)
    max_point = max(inputs)

    for input_to_compare in range(min_point, max_point):
        distance_fuel_consumption = sum(
            [
                sum_numbers_zero_to_N(abs(input_to_compare - point_to_compare))
                for point_to_compare in inputs
                if point_to_compare != input_to_compare
            ]
        )
        inputs_fuel_consumption[input_to_compare] = distance_fuel_consumption

    key_min = min(inputs_fuel_consumption, key=inputs_fuel_consumption.get)
    return inputs_fuel_consumption[key_min]


def part1():
    inputs = read_input("input.txt")
    min_fuel = compute_least_fuel_consumption_1_fuel_each_move(inputs)
    return min_fuel


def part2():
    inputs = read_input("input.txt")
    min_fuel = compute_least_fuel_consumption_plus_1_fuel_each_move(inputs)
    return min_fuel


def main():
    # part 1: align points with minimum moves
    response_part1 = part1()
    print("Day 7 -- part 1")
    print(f"Response: {response_part1}\n")
    assert response_part1 == 328318
    # part 2:
    response_part2 = part2()
    print("Day 7 -- part 2")
    print(f"Response: {response_part2}")


main()
