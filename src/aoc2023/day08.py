from src.common.dataload import DataLoader, Answers
from typing import Sequence, Iterator
from dataclasses import dataclass
import re
import math

word_pattern = re.compile(r"(\w+)")


@dataclass
class Navigator:
    directions: str
    mapping: dict[str, tuple[str, str]]

    def path(self) -> int:
        count = 0
        current = "AAA"
        direction_generator = self.yield_direction()
        while current != "ZZZ":
            next_side = next(direction_generator)
            current = self.mapping[current][next_side]
            count += 1
        return count

    def path2(self) -> int:
        """This is solved using the least common multiple math technique."""
        current_keys: list[str] = list()
        current_counts: list[int] = list()
        direction_generator = self.yield_direction()
        done = lambda x: all([x.endswith("Z") for x in current_keys])
        for key in self.mapping:
            if key.endswith("A"):
                current_keys.append(key)
                current_counts.append(0)
        while not done(current_keys):
            next_side = next(direction_generator)
            for i, key in enumerate(current_keys):
                if key.endswith("Z"):
                    continue
                current_keys[i] = self.mapping[current_keys[i]][next_side]
                current_counts[i] += 1
        return math.lcm(*current_counts)

    def yield_direction(self) -> Iterator[int]:
        i = 0
        while True:
            d = self.directions[i % len(self.directions)]
            if d == "L":
                yield 0
            elif d == "R":
                yield 1
            i += 1


def parse(lines: Sequence[str]) -> Navigator:
    directions = lines[0].strip()
    mapping: dict[str, tuple[str, str]] = dict()
    for line in lines[2:]:
        source, destination = line.split("=")
        matches = word_pattern.findall(destination)
        mapping[source.strip()] = (matches[0], matches[1])
    return Navigator(directions, mapping)


class Day08Answers(Answers):
    def __init__(self):
        loader = DataLoader(2023, "day08.txt")
        self.data = loader.readlines_str()

    def part1(self) -> str:
        navigator = parse(self.data)
        return str(navigator.path())

    def part2(self) -> str:
        navigator = parse(self.data)
        return str(navigator.path2())
