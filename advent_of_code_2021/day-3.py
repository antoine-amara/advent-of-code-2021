import pandas as pd

from helpers.input_parser import parse_list_elements_to_u8_string, read_input_lines

LEAST = "least"
MOST = "most"


def read_input(input_name="example.txt"):
    raw_data = read_input_lines(day=3, input_name=input_name)
    data = parse_list_elements_to_u8_string(raw_data)
    data = [[int(unit) for unit in element] for element in data]
    df = pd.DataFrame(data)
    return df


def count_column_values(column, type=MOST):
    counts = column.value_counts()

    if type == LEAST:
        if counts[0] > counts[1]:
            return 1
        else:
            return 0

    if type == MOST:
        if counts[0] <= counts[1]:
            return 1
        else:
            return 0


def filter_report(report_df, column_index, type=MOST):
    if report_df.shape[0] == 1:
        return report_df

    bit_to_keep = count_column_values(report_df[column_index], type=type)
    list_to_keep = [row for _, row in report_df.iterrows() if row[column_index] == bit_to_keep]
    filtered_rating_df = pd.DataFrame(list_to_keep)
    return filtered_rating_df


def part1():
    report_df = read_input("input.txt")
    gamma = ""
    epsilon = ""
    for _, column in report_df.items():
        gamma += str(count_column_values(column))
        epsilon += str(count_column_values(column, type=LEAST))

    return int(gamma, 2) * int(epsilon, 2)


def part2():
    report_df = read_input("input.txt")
    oxygen_generator_rating_df = report_df.copy()
    co2_scrubber_rating_df = report_df.copy()

    for index, _ in report_df.items():
        # oxygen_generator_rating:
        # for each column keep lines with the most values occurent at index i
        oxygen_generator_rating_df = filter_report(oxygen_generator_rating_df, index, type=MOST)

        # co2_scrubber_rating_df:
        # for each column keep lines with the least values occurent at index i
        co2_scrubber_rating_df = filter_report(co2_scrubber_rating_df, index, type=LEAST)

    # DIRTY convert the dataframe to list of string
    # (representing the number in base 2) to integer base 10
    oxygen_generator_rating_list = [str(elmt) for elmt in list(oxygen_generator_rating_df.iloc[0])]
    co2_scrubber_rating_list = [str(elmt) for elmt in list(co2_scrubber_rating_df.iloc[0])]

    oxygen_generator_rating = int("".join(oxygen_generator_rating_list), 2)
    co2_scrubber_rating = int("".join(co2_scrubber_rating_list), 2)

    # final response
    return oxygen_generator_rating * co2_scrubber_rating


def main():
    # part 1: determine by column the most and least binary bit
    # appering and mutiply the results in base 2.
    response_part1 = part1()
    print("Day 3 -- part 1")
    print(f"Response: {response_part1}\n")
    assert response_part1 == 4138664
    # part 2: filter the report to extract 2 metrics
    # and multiply them
    response_part2 = part2()
    print("Day 3 -- part 2")
    print(f"Response: {response_part2}")
    assert response_part2 == 4273224


main()
