from typing import Sequence
from src.common.dataload import DataLoader, Answers
from src.common.parsing import extract_integers


def derivative(numbers: list[int]) -> list[int]:
    nprime: list[int] = list()
    for i in range(len(numbers) - 1):
        nprime.append(numbers[i + 1] - numbers[i])
    return nprime


def derivative_all(numbers: list[int]) -> list[list[int]]:
    result: list[list[int]] = list()
    result.append(numbers)
    while any(numbers):
        numbers = derivative(numbers)
        result.append(numbers)
    return result


def parse(lines: Sequence[str]) -> list[list[int]]:
    num_lines = list()
    for line in lines:
        numbers = extract_integers(line)
        assert numbers is not None
        num_lines.append(numbers)
    return num_lines


# def next_in_sequence(derivatives_list: list[list[int]]) -> int:
#     # result: list[int] = list()
#     # for i in range(0, len(derivatives_list) - 1):
#     #     n = derivatives_list[i][-1] + derivatives_list[i + 1][-1]
#     #     result.append(n)
#     # return result
#     return derivatives_list[0][-1] + derivatives_list[1][-1]


def next_in_sequence(derivatives_list: list[list[int]]) -> list[list[int]]:
    for i in range(0, len(derivatives_list) - 1):
        n = derivatives_list[i][-1] + derivatives_list[i + 1][-1]
        derivatives_list[i].append(n)
    return derivatives_list


def sum_all(lines: list[list[int]]) -> list[int]:
    all_next_numbers: list[int] = list()
    for line in lines:
        derivatives = derivative_all(line)
        n = next_in_sequence(derivatives)
        all_next_numbers.append(n)
    return all_next_numbers


class Day09Answers(Answers):
    def __init__(self):
        loader = DataLoader(2023, "day09.txt")
        raw_data = loader.readlines_str()
        self.data = parse(raw_data)

    def part1(self) -> str:
        all_next_numbers = sum_all(self.data)
        return str(sum(all_next_numbers))

    def part2(self) -> str:
        return super().part2()
