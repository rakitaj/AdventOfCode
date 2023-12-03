from src.common.dataload import DataLoader
import re
from dataclasses import dataclass
from collections import deque
from typing import Sequence


@dataclass
class StacksAndInstructions:
    stacks: list[deque[str]]
    instructions: Sequence[str]


num_pattern = re.compile("(\\d+)")
instruction_patern = re.compile("move (\\d+) from (\\d+) to (\\d+)")


def load_and_parse() -> StacksAndInstructions:
    loader = DataLoader(2022, "day05.txt")
    data = loader.readlines_str()
    result = parse_lines(data)
    return result


def parse_lines(lines: Sequence[str]) -> StacksAndInstructions:
    num_stacks, line_num_end_stacks_setup = find_quantity(lines)
    stacks = populate_stacks(lines, num_stacks, line_num_end_stacks_setup)
    return StacksAndInstructions(stacks, lines[line_num_end_stacks_setup + 1 :])


def find_quantity(all_data: Sequence[str]) -> tuple[int, int]:
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


def populate_stacks(data: Sequence[str], num_stacks: int, stop_at: int) -> list[deque[str]]:
    stacks: list[deque[str]] = list()
    for _ in range(num_stacks):
        stacks.append(deque())
    for i in range(stop_at - 2, -1, -1):
        for j in range(num_stacks):
            offset = (j * 4) + 1
            char = data[i][offset : offset + 1]
            if not char.isspace():
                stacks[j].append(char)
    return stacks


def execute_instructions(s_and_i: StacksAndInstructions) -> list[str]:
    stacks = s_and_i.stacks
    for instruction in s_and_i.instructions:
        captures = instruction_patern.findall(instruction)
        count, source, target = captures[0]
        for _ in range(int(count)):
            temp = stacks[int(source) - 1].pop()
            stacks[int(target) - 1].append(temp)
    result: list[str] = list()
    for stack in stacks:
        result.append(stack.pop())
    return result


def execute_instructions_2(s_and_i: StacksAndInstructions) -> list[str]:
    stacks = s_and_i.stacks
    for instruction in s_and_i.instructions:
        captures = instruction_patern.findall(instruction)
        count, source, target = captures[0]
        temp: list[str] = list()
        for _ in range(int(count)):
            temp.append(stacks[int(source) - 1].pop())
        for _ in range(int(count)):
            stacks[int(target) - 1].append(temp.pop())
    result: list[str] = list()
    for stack in stacks:
        result.append(stack.pop())
    return result


def part01_answer() -> str:
    stacks_and_instructions = load_and_parse()
    result = execute_instructions(stacks_and_instructions)
    return "".join(result)


def part02_answer() -> str:
    stacks_and_instructions = load_and_parse()
    result = execute_instructions_2(stacks_and_instructions)
    return "".join(result)
