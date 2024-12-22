from src.common.dataload import Answers, DataLoader
from collections import Counter


def partition_data(lines: list[list[int]]) -> tuple[list[int], list[int]]:
    left = []
    right = []
    for line in lines:
        left.append(line[0])
        right.append(line[1])
    return (left, right)


class Day01Answers(Answers):
    def __init__(self):
        loader = DataLoader(2024, "day01.txt")
        self.data = loader.readlines_int()

    def part1(self) -> str:
        total = 0
        left, right = partition_data(self.data)
        left_sorted = sorted(left)
        right_sorted = sorted(right)
        combined_sorted_data = zip(left_sorted, right_sorted)
        for l, r in combined_sorted_data:
            total += abs(l - r)
        return str(total)

    def part2(self) -> str:
        total = 0
        left, right = partition_data(self.data)
        right_counts = Counter(right)
        for num in left:
            total += num * right_counts.get(num, 0)
        return str(total)
