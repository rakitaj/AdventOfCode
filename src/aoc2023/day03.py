from typing import Sequence
from src.common.dataload import DataLoader, Answers
import re

pattern_numbers = re.compile(r"(\d+)")


def symbol_adjacent(num_start_end: tuple[int, int], symbols: list[int]) -> bool:
    """Is the number adjacent to any symbols?
    Range (3, 7)
    Symbols [2, 10]
    """
    start, end = num_start_end
    for i in symbols:
        if i >= start - 1 and i <= end + 1:
            return True
    return False


def match_symbols(line: str) -> list[int]:
    mactch_indices = list()
    for i, e in enumerate(line):
        if e != "." and not e.isdigit() and e != "\n":
            mactch_indices.append(i)
    return mactch_indices


def part_numbers(prev_line: str | None, line: str, next_line: str | None) -> list[int]:
    numbers: list[int] = list()
    symbol_matches: list[int] = list()
    for l in (prev_line, line, next_line):
        if l is not None:
            match_indices = match_symbols(l)
            symbol_matches.extend(match_indices)
    for m in pattern_numbers.finditer(line):
        if symbol_adjacent((m.start(), m.end() - 1), symbol_matches):
            numbers.append(int(m.group(1)))
    return numbers


def part_numbers_all_lines(lines: Sequence[str]) -> int:
    total = list()
    for i in range(len(lines)):
        if i - 1 < 0:
            prev_line = None
        else:
            prev_line = lines[i - 1]
        if i + 1 >= len(lines):
            next_line = None
        else:
            next_line = lines[i + 1]
        nums = part_numbers(prev_line, lines[i], next_line)
        total.extend(nums)
    return sum(total)


def gear_adjacent(matches: list[re.Match], i: int) -> tuple[int, int] | None:
    adjacent_nums = list()
    for m in matches:
        if i >= m.start() - 1 and i <= m.end():
            adjacent_nums.append(int(m.group(1)))
    if len(adjacent_nums) == 2:
        return (adjacent_nums[0], adjacent_nums[1])
    else:
        return None


def gear_numbers(prev_line: str, line: str, next_line: str) -> list[int]:
    numbers: list[int] = list()
    symbol_indices = match_symbols(line)
    number_matches: list[re.Match] = list()
    for l in (prev_line, line, next_line):
        for m in pattern_numbers.finditer(l):
            number_matches.append(m)
    for i in symbol_indices:
        nums_adjacent = gear_adjacent(number_matches, i)
        if isinstance(nums_adjacent, tuple):
            numbers.extend(nums_adjacent)
    return numbers


class Day03Answers(Answers):
    def __init__(self) -> None:
        loader = DataLoader(2023, "day03.txt")
        self.data = loader.readlines_str()

    def part1(self) -> str:
        """Too high 88151870"""
        total = part_numbers_all_lines(self.data)
        return str(total)

    def part2(self) -> str:
        return "Not yet"
