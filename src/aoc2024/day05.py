from typing import Sequence
from src.common.dataload import DataLoader, Answers, timed
from src.common.parsing import extract_integers


class Rules:

    def __init__(self) -> None:
        self.forwards: dict[int, set[int]] = dict()


def is_page_sorted_pessimisstic(page_numbers: list[int], rules: Rules) -> bool:
    seen: set[int] = set()
    for page_num in page_numbers:
        must_come_after = rules.forwards.get(page_num, set())
        if len(seen.intersection(must_come_after)) > 0:
            return False
        seen.add(page_num)
    return True


class Day05Parsed:

    def __init__(self, lines: Sequence[str]) -> None:
        self.rules = Rules()
        self.page_updates: list[list[int]] = list()
        for line in lines:
            numbers = extract_integers(line)
            if len(numbers) == 2:
                self.rules.forwards.setdefault(numbers[0], {numbers[1]}).add(numbers[1])
            elif len(numbers) > 2:
                self.page_updates.append(numbers)


class Day05Answers(Answers):

    def __init__(self) -> None:
        loader = DataLoader(2024, "day05.txt")
        self.lines = loader.readlines_str()

    @timed
    def part1(self) -> str:
        parsed = Day05Parsed(self.lines)
        total = 0
        for line in parsed.page_updates:
            if is_page_sorted_pessimisstic(line, parsed.rules):
                midpoint = len(line) // 2
                total += line[midpoint]
        return str(total)

    def part2(self) -> str:
        return ""
