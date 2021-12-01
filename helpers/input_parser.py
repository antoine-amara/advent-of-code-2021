def read_input_lines(*, day=1, input_name="example.txt"):
    path = f"advent_of_code_2021/data/day-{day}/{input_name}"
    with open(path) as file:
        lines = file.readlines()
        return lines


def parse_list_elements_to_int(input_list=[]):
    return [int(element) for element in input_list]
