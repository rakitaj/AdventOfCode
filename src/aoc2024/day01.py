from functools import reduce

from src.common.dataload import Answers, DataLoader


def load_and_parse() -> list[str]:
    loader = DataLoader(2024, "day01.txt")
    return loader.readlines_str()


def split_to_left_and_right(lines: list[str]) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []
    for line in lines:
        l, r = line.split()
        left.append(int(l.strip()))
        right.append(int(r.strip()))
    return (left, right)


class Day01Answers(Answers):
    def __init__(self) -> None:
        self.data = load_and_parse()

    def part1(self) -> str:
        left, right = split_to_left_and_right(self.data)
        left_sorted = sorted(left)
        right_sorted = sorted(right)
        paired_data = zip(left_sorted, right_sorted, strict=False)
        total = reduce(lambda acc, x: acc + abs(x[0] - x[1]), paired_data, 0)
        return str(total)

    def part2(self) -> str:
        return "hi"
