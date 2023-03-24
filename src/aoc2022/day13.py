from src.common.extensions import flatten
from src.common.dataload import DataLoader
import json


def compare_lines(line1: str, line2: str) -> bool:
    line1_parsed = json.loads(line1)
    line2_parsed = json.loads(line2)
    left = flatten(line1_parsed)
    right = flatten(line2_parsed)
    try:
        for i in range(len(right)):
            if left[i] == right[i] and i == len(right) - 1 and len(right) < len(left):
                return False
            if left[i] > right[i]:
                return False
    except IndexError as index_error:
        print(f"{index_error}\nLeft: {left}\nRight: {right}\n")
    return True


def load_and_parse() -> list[tuple[str, str]]:
    loader = DataLoader(2022, "day13.txt")
    lines = loader.readlines_str(True)
    result: list[tuple[str, str]] = list()
    for i in range(2, len(lines), 3):
        pair_of_lines = (lines[i - 2], lines[i - 1])
        result.append(pair_of_lines)
    return result


def part01_answer() -> str:
    line_pairs = load_and_parse()
    count = 0
    for line_pair in line_pairs:
        if compare_lines(line_pair[0], line_pair[1]):
            count += 1
    return str(count)
