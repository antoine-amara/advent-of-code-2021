import pandas as pd

from helpers.input_parser import parse_list_elements_to_int_tuple, read_input_lines


def read_input(input_name="example.txt"):
    raw_data = read_input_lines(day=5, input_name=input_name)
    parsed_data = [parse_list_elements_to_int_tuple(line.split(" -> ")) for line in raw_data]
    # determin length of diagram
    # it is the max on list of array(2) of tuple
    diagram_length = max(
        [max(max(input_data[0]), max(input_data[1])) for input_data in parsed_data]
    )
    return diagram_length, parsed_data


def place_horizontal_vertical_point(one_inputs, *, is_x_equals, is_y_equals, diagram_matrix):
    range_to_update = None

    if is_y_equals:
        range_tuple = (one_inputs[0][0], one_inputs[1][0])
        range_to_update = range(min(range_tuple), max(range_tuple) + 1)
    if is_x_equals:
        range_tuple = (one_inputs[0][1], one_inputs[1][1])
        range_to_update = range(min(range_tuple), max(range_tuple) + 1)

    for i in range_to_update:
        if is_y_equals:
            y = one_inputs[0][1]
            diagram_matrix[i][y] += 1
        if is_x_equals:
            x = one_inputs[0][0]
            diagram_matrix[x][i] += 1

    return diagram_matrix


def place_diagonal_point(one_inputs, diagram_matrix):
    start_point, end_point = one_inputs
    x_start_point, y_start_point = start_point
    x_end_point, y_end_point = end_point
    # place point at begining and end
    diagram_matrix[x_start_point][y_start_point] += 1
    diagram_matrix[x_end_point][y_end_point] += 1

    # place points on the diagonal
    is_end = False
    last_point = start_point
    while not is_end:
        # compute next x
        if last_point[0] < end_point[0]:
            last_point[0] += 1
        else:
            last_point[0] -= 1
        # compute next y
        if last_point[1] < end_point[1]:
            last_point[1] += 1
        else:
            last_point[1] -= 1

        x_last_point, y_last_point = last_point

        if x_last_point == x_end_point and y_last_point == y_end_point:
            is_end = True
            continue

        diagram_matrix[x_last_point][y_last_point] += 1

    return diagram_matrix


def place_one_point_on_diagram(one_inputs, diagram_matrix, diagonal):
    is_x_equals = one_inputs[0][0] == one_inputs[1][0]
    is_y_equals = one_inputs[0][1] == one_inputs[1][1]

    if (not is_x_equals and not is_y_equals) or (is_x_equals and is_y_equals):
        if diagonal is True:
            place_diagonal_point(one_inputs, diagram_matrix)

        return diagram_matrix

    place_horizontal_vertical_point(
        one_inputs, is_x_equals=is_x_equals, is_y_equals=is_y_equals, diagram_matrix=diagram_matrix
    )

    return diagram_matrix


def compute_diagram_score(diagram_matrix):
    score = 0
    for _, row in diagram_matrix.iterrows():
        for _, value in row.iteritems():
            if value >= 2:
                score += 1

    return score


def place_points_on_diagram(inputs, diagram_length, *, diagonal=False):
    diagram_matrix = pd.DataFrame(
        0, index=range(0, diagram_length + 1), columns=range(0, diagram_length + 1)
    )
    for input in inputs:
        place_one_point_on_diagram(input, diagram_matrix, diagonal)

    return diagram_matrix


def part1():
    diagram_length, inputs = read_input("input.txt")
    diagram_matrix = place_points_on_diagram(inputs, diagram_length)
    score = compute_diagram_score(diagram_matrix)
    return score


def part2():
    diagram_length, inputs = read_input("input.txt")
    diagram_matrix = place_points_on_diagram(inputs, diagram_length, diagonal=True)
    score = compute_diagram_score(diagram_matrix)
    return score


def main():
    # part 1: compute point in a diagram and return the number od adjacent line
    # ignore the diagonal points
    response_part1 = part1()
    print("Day 5 -- part 1")
    print(f"Response: {response_part1}\n")
    assert response_part1 == 5576
    # part 2: compute point in a diagram and return the number od adjacent line
    # compute the diagonal points
    response_part2 = part2()
    print("Day 5 -- part 2")
    print(f"Response: {response_part2}")
    assert response_part2 == 18144


main()
