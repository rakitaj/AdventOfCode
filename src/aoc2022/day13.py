import json
from typing import Any

from src.common.dataload import DataLoader

# Results - part 1
# 4554 - too low


def compare_lines(line1: str, line2: str) -> bool:
    line1_parsed = json.loads(line1)
    line2_parsed = json.loads(line2)

    try:
        result = compare(line1_parsed, line2_parsed)
    except IndexError as ex:
        print(ex)
        result = False
    return result > 0


def compare(line1: Any, line2: Any) -> int:
    for i in range(len(line1)):
        e1 = line1[i]
        e2 = line2[i]
        if isinstance(e1, list) and isinstance(e2, list):
            if i > len(e2):
                return False
            if compare(e1, e2) is False:
                return False
        elif isinstance(e1, int) and isinstance(e2, int):
            if e1 > e2:
                return False
        elif isinstance(e1, list) and isinstance(e2, int):
            return compare(e1, [e2])
        elif isinstance(e1, int) and isinstance(e2, list):
            return compare([e1], e2)
        else:
            breakpoint()
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
