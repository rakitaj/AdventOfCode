from src.common.dataload import DataLoader
import re
from dataclasses import dataclass
from collections import deque


@dataclass
class StacksAndInstructions:
    stacks: list[deque[str]]
    instructions: list[str]


num_pattern = re.compile("(\\d+)")


def load_and_parse() -> StacksAndInstructions:
    loader = DataLoader(2022, "day05.txt")
    data = loader.readlines_str()
    num_stacks, line_num_end_stacks_setup = find_quantity(data)
    stacks = populate_stacks(data, num_stacks, line_num_end_stacks_setup)
    return StacksAndInstructions(stacks, data[line_num_end_stacks_setup:])


def find_quantity(all_data: list[str]) -> tuple[int, int]:
    """
    Look for the largest number before the black line. That will be the number of stacks.
    Returns a tuple[int, int] of (num_stacks, line_num). Returns (num_stacks, -1) if it can't
    find a stopping point.
    """
    max_number = 0
    for i, line in enumerate(all_data):
        all_matches = num_pattern.findall(line)
        if len(all_matches) > 0:
            max_number = max(max_number, int(max(all_matches)))
        if not line or line.isspace():
            return (max_number, i)
    return (max_number, -1)


def populate_stacks(data: list[str], num_stacks: int, stop_at: int) -> list[deque[str]]:
    char_regex = re.compile("(\\w)")
    stacks: list[deque[str]] = list()
    for _ in range(num_stacks):
        stacks.append(deque())
    for i in range(stop_at - 2, 0, -1):
        columns = data[i].split()
        for ii, col in enumerate(columns):
            char = char_regex.match(col, 0)
            stacks[ii].append(char)
    return stacks
