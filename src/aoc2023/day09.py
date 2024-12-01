from typing import Sequence

from src.common.dataload import Answers, DataLoader
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


def next_in_sequence(derivatives_list: list[list[int]]) -> list[list[int]]:
    for i in range(len(derivatives_list) - 2, -1, -1):
        n = derivatives_list[i][-1] + derivatives_list[i + 1][-1]
        derivatives_list[i].append(n)
    return derivatives_list


def previous_in_sequence(derivatives_list: list[list[int]]) -> list[list[int]]:
    for i in range(len(derivatives_list) - 2, -1, -1):
        n = derivatives_list[i][0] - derivatives_list[i + 1][0]
        derivatives_list[i].insert(0, n)
    return derivatives_list


class Day09Answers(Answers):
    def __init__(self) -> None:
        loader = DataLoader(2023, "day09.txt")
        raw_data = loader.readlines_str()
        self.data = parse(raw_data)

    def part1(self) -> str:
        total = 0
        for i, line in enumerate(self.data):
            derivatives = derivative_all(numbers=line)
            derivateves_next = next_in_sequence(derivatives)
            total += derivateves_next[0][-1]
        return str(total)

    def part2(self) -> str:
        total = 0
        for i, line in enumerate(self.data):
            derivatives = derivative_all(numbers=line)
            derivateves_prev = previous_in_sequence(derivatives)
            total += derivateves_prev[0][0]
        return str(total)
