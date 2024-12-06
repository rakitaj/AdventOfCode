from src.common.dataload import DataLoader, Answers
from src.common.parsing import extract_integers
import re

pattern = r"mul\(\d+,\d+\)"
mul_regex = re.compile(pattern)


def multiply_line(line: str) -> int:
    total = 0
    matches = mul_regex.findall(line)
    for m in matches:
        integers = extract_integers(m)
        total += integers[0] * integers[1]
    return total


def multiply_line_conditional(line: str) -> int:
    enabled = True
    i = 0
    total = 0
    while i < len(line):
        if line.startswith("do()", i):
            enabled = True
            i += 3
        elif not enabled:
            i += 1
        elif line.startswith("don't()", i):
            enabled = False
            i += 6
        else:
            m = mul_regex.match(line, i)
            if m is not None:
                matching_string = m.group(0)
                integers = extract_integers(matching_string)
                total += integers[0] * integers[1]
            i += 1
    return total


class Day03Answers(Answers):

    def __init__(self) -> None:
        loader = DataLoader(2024, "day03.txt")
        self.lines = loader.readlines_str()
        self.raw = loader.read()

    def part1(self) -> str:
        total = 0
        for line in self.lines:
            total += multiply_line(line)
        return str(total)

    # Must treat input as one line. The multiplication do/don't carries over from line to line.
    def part2(self) -> str:
        total = 0
        total += multiply_line_conditional(self.raw)
        return str(total)
