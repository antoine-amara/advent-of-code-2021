import pandas as pd


def read_input_lines(*, day=1, input_name="example.txt"):
    path = f"advent_of_code_2021/data/day-{day}/{input_name}"
    with open(path) as file:
        lines = file.readlines()
        return lines


def parse_list_elements_to_int(input_list=[]):
    return [int(element) for element in input_list if element != ""]


def parse_list_elements_to_int_tuple(input_list=[]):
    splitted_input = [input_raw.split(",") for input_raw in input_list]
    parsed_tuple = [parse_list_elements_to_int(splitted) for splitted in splitted_input]
    return parsed_tuple


def parse_list_elements_to_u8_string(input_list=[]):
    return [element.format(0b11000011).strip() for element in input_list]


def read_input_as_dataframe(*, day=1, input_name="example.txt", delimiter=" ", names=[]):
    path = f"advent_of_code_2021/data/day-{day}/{input_name}"
    return pd.read_csv(path, delimiter=delimiter, header=None, names=names)
