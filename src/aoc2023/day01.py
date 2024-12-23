from typing import Sequence
from src.common.dataload import DataLoader, Answers

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def load_and_parse() -> list[str]:
    loader = DataLoader(2023, "day01.txt")
    return loader.readlines_str()


def parse_digits(s: str) -> int:
    first = -1
    last = -1
    for c in s:
        if c.isdigit():
            num = int(c)
            if first == -1:
                first = num
            last = num
    return (first * 10) + last


def try_parse_digit(s: str, i: int) -> tuple[bool, int]:
    if s[i].isdigit():
        return (True, int(s[i]))
    for key, value in digits.items():
        if s[i::].startswith(key):
            return (True, value)
    return (False, -1)


def parse_string_digits(s: str) -> int:
    first = -1
    last = -1
    for i in range(len(s)):
        parsed, num = try_parse_digit(s, i)
        if parsed:
            if first == -1:
                first = num
            last = num
    return (first * 10) + last


def _part02_answer(strings: Sequence[str]) -> int:
    total = 0
    for s in strings:
        num = parse_string_digits(s)
        total += num
    return total


class Day01Answers(Answers):
    def __init__(self):
        self.data = load_and_parse()

    def part1(self) -> str:
        total = 0
        for s in self.data:
            num = parse_digits(s)
            total += num
        return str(total)

    def part2(self) -> str:
        """
        54718 - too high
        """
        total = _part02_answer(self.data)
        return str(total)
