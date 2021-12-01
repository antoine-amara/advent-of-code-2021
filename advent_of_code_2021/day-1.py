def read_input(input_name="example.txt"):
    path = "advent_of_code_2021/data/day1/" + input_name
    with open(path) as file:
        lines = file.readlines()
        return lines


def count_larger_mesures_one_by_one(data):
    count_list = [
        int(mesure) < int(data[index + 1])
        for index, mesure in enumerate(data)
        if index + 1 < len(data)
    ]
    assert len(count_list) == len(data) - 1
    return sum(count_list)


def count_larger_mesures_three_by_three(data):
    tuples_sum = [
        sum([int(mesure), int(data[index + 1]), int(data[index + 2])])
        for index, mesure in enumerate(data)
        if index + 2 < len(data)
    ]
    assert len(tuples_sum) == len(data) - 2
    return count_larger_mesures_one_by_one(tuples_sum)


def part1():
    # should be = 1532
    data = read_input("input.txt")
    counter = count_larger_mesures_one_by_one(data)
    return counter


def part2():
    # should be = 1571
    data = read_input("input.txt")
    counter = count_larger_mesures_three_by_three(data)
    return counter


def main():
    # part 1: compare elements one by one
    response_part1 = part1()
    print("Day 1 -- part 1")
    print(f"Response: {response_part1}")
    # part 1: compare elements  with sum of three elements
    response_part2 = part2()
    print("Day 1 -- part 2")
    print(f"Response: {response_part2}")


main()
