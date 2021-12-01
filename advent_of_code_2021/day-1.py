from helpers.input_parser import parse_list_elements_to_int, read_input_lines


def read_input(input_name="example.txt"):
    string_lines = read_input_lines(day=1, input_name=input_name)
    return parse_list_elements_to_int(string_lines)


def count_larger_mesures_one_by_one(data):
    count_list = [
        mesure < data[index + 1] for index, mesure in enumerate(data) if index + 1 < len(data)
    ]
    assert len(count_list) == len(data) - 1
    return sum(count_list)


def count_larger_mesures_three_by_three(data):
    tuples_sum = [
        sum([mesure, data[index + 1], data[index + 2]])
        for index, mesure in enumerate(data)
        if index + 2 < len(data)
    ]
    assert len(tuples_sum) == len(data) - 2
    return count_larger_mesures_one_by_one(tuples_sum)


def part1():
    # should be = 1532
    data = read_input("input.txt")
    counter = count_larger_mesures_one_by_one(data)
    assert counter == 1532
    return counter


def part2():
    # should be = 1571
    data = read_input("input.txt")
    counter = count_larger_mesures_three_by_three(data)
    assert counter == 1571
    return counter


def main():
    # part 1: compare elements one by one
    response_part1 = part1()
    print("Day 1 -- part 1")
    print(f"Response: {response_part1}\n")
    # part 2: compare elements  with sum of three elements
    response_part2 = part2()
    print("Day 1 -- part 2")
    print(f"Response: {response_part2}")


main()
