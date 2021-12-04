import pandas as pd
from iteration_utilities import deepflatten

from helpers.input_parser import parse_list_elements_to_int, read_input_lines


def parse_one_bingo_input(data_iter):
    # pass the blank line
    next(data_iter)

    bingo_board = []
    # parse the 5 lines representing a bingo board
    for _ in range(0, 5):
        next_line = next(data_iter)
        splited_line = next_line.split(" ")
        parsed_line = parse_list_elements_to_int(splited_line)
        bingo_board.append(parsed_line)

    return bingo_board


def read_input(input_name="example.txt"):
    raw_data_iter = iter(read_input_lines(day=4, input_name=input_name))
    bingo_board_list = []

    # parse bingo input and get list of int
    bingo_input = next(raw_data_iter)
    bingo_input = bingo_input.split(",")
    bingo_inputs = parse_list_elements_to_int(bingo_input)

    while True:
        try:
            bingo_board_list.append(parse_one_bingo_input(raw_data_iter))
        except StopIteration:
            break

    return bingo_inputs, bingo_board_list


def check_bingo_board_win(bingo_board, bingo_input):
    match_board = pd.DataFrame(columns=range(5), index=range(5))
    # create the match board
    for line_index, line in enumerate(bingo_board):
        for element_index, element in enumerate(line):
            if element in bingo_input:
                match_board[element_index][line_index] = True
            else:
                match_board[element_index][line_index] = False

    # check if one line
    # or column have bingo (all True)
    for i in range(0, 5):
        column_win = sum(match_board[i]) == 5
        line_win = sum(match_board.iloc[i]) == 5

        if column_win or line_win:
            return True, match_board.values.tolist()

    return False, match_board.values.tolist()


def compute_winner_board_score(winner_board, winner_match_board, last_bingo_element):
    score = 0
    for element_index, element_match in enumerate(winner_match_board):
        if element_match is False:
            score += winner_board[element_index]

    return score * last_bingo_element


def resolve_bingo_first_board_win(bingo_input, bingo_boards):
    input_length = 1
    win = False
    winner_score = 0
    while win is False:
        next_bingo_input = bingo_input[:input_length]
        for board in bingo_boards:
            is_winner, match_board = check_bingo_board_win(board, next_bingo_input)
            if is_winner is True:
                winner_score = compute_winner_board_score(
                    list(deepflatten(board)), list(deepflatten(match_board)), next_bingo_input[-1]
                )
                win = True
        input_length += 1

    return winner_score


def resolve_bingo_last_board_win(bingo_input, bingo_boards):
    input_length = 1
    win = False
    winner_score = 0
    winner_boards_index = []
    while win is False:
        next_bingo_input = bingo_input[:input_length]
        for board_index, board in enumerate(bingo_boards):
            is_winner, match_board = check_bingo_board_win(board, next_bingo_input)
            if is_winner is True:
                if board_index not in winner_boards_index:
                    winner_boards_index.append(board_index)
                if len(winner_boards_index) == len(bingo_boards):
                    win = True
        input_length += 1

    last_winner_board = bingo_boards[winner_boards_index[-1]]
    is_winner, match_board = check_bingo_board_win(
        bingo_boards[winner_boards_index[-1]], next_bingo_input
    )
    winner_score = compute_winner_board_score(
        list(deepflatten(last_winner_board)), list(deepflatten(match_board)), next_bingo_input[-1]
    )

    return winner_score


def part1():
    bingo_input, bingo_boards = read_input("input.txt")
    winner_score = resolve_bingo_first_board_win(bingo_input, bingo_boards)
    return winner_score


def part2():
    bingo_input, bingo_boards = read_input("input.txt")
    winner_score = resolve_bingo_last_board_win(bingo_input, bingo_boards)
    return winner_score


def main():
    # part 1: find the first bingo board winner from boards and inputs
    response_part1 = part1()
    print("Day 4 -- part 1")
    print(f"Response: {response_part1}\n")
    assert response_part1 == 8136
    # part 2: find the last board winner from boards and inputs
    response_part2 = part2()
    print("Day 4 -- part 2")
    print(f"Response: {response_part2}")
    assert response_part2 == 12738


main()
