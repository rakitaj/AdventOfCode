from src.common.extensions import flatten
from src.common.dataload import DataLoader
import json


def calculate_depth(line: str) -> tuple[bool, int]:
    count = 0
    empty = True
    for char in line:
        if char == "[":
            count += 1
        elif char.isdigit():
            empty = False
    return (empty, count)


def compare_lines(line1: str, line2: str) -> bool:
    line1_parsed = json.loads(line1)
    line2_parsed = json.loads(line2)
    left = flatten(line1_parsed)
    right = flatten(line2_parsed)

    line1_empty, line1_depth = calculate_depth(line1)
    line2_empty, line2_depth = calculate_depth(line2)
    if line1_empty and line2_empty and line1_depth > line2_depth:
        return False

    for i in range(len(left)):
        if i >= len(right):
            break
        if left[i] > right[i]:
            return False
        # if left[i] == right[i] and i == len(right) - 1 and len(right) < len(left):
        #     return False
    return True


def load_and_parse() -> list[tuple[str, str]]:
    loader = DataLoader(2022, "day13.txt")
    lines = loader.readlines_str(True)
    result: list[tuple[str, str]] = list()
    for i in range(2, len(lines) + 1, 3):
        pair_of_lines = (lines[i - 2], lines[i - 1])
        result.append(pair_of_lines)
    return result


def part01_answer() -> str:
    line_pairs = load_and_parse()
    valid_pairs: list[int] = []
    for i, line_pair in enumerate(line_pairs):
        if compare_lines(line_pair[0], line_pair[1]):
            valid_pairs.append(i + 1)
    total = sum(valid_pairs)
    return str(total)
