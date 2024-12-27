from typing import Sequence
from src.common.dataload import DataLoader, Answers, timed
from src.common.grid import Grid, Direction
from src.common.extensions import must


class Day06Answers(Answers):

    def __init__(self) -> None:
        loader = DataLoader(2024, "day06.txt")
        self.lines = loader.readlines_str()
        self.set_grid(self.lines)

    def set_grid(self, lines: Sequence[str]) -> None:
        self.grid = Grid.from_strings_no_spaces(lines)

    @timed
    def part1(self) -> str:
        visited: set[tuple[int, int]] = set()
        start = self.grid.find("^")
        assert start is not None
        x, y = start
        direction = Direction.UP

        while self.grid.try_get(x, y):
            visited.add((x, y))
            next_char = self.peek(x, y, direction)
            if next_char == "#":
                direction = Direction.roate_right(direction)
            x, y = self.move(x, y, direction)
        return str(len(visited))

    @timed
    def part2(self) -> str:
        # total = 0
        # for p in self.grid.iter_points():
        #     # If we pass by the same spot going the same direction we're in a loop!
        #     visited: set[tuple[int, int, Direction]] = set()
        #     x, y = must(self.grid.find("^"))
        #     direction = Direction.UP

        #     # Skip the case where the blocking obstruction and guard are in the same spot.
        #     if p.x == x and p.y == y:
        #         continue
        #     changed = False
        #     if self.grid.get(p.x, p.y) == ".":
        #         self.grid.set(p.x, p.y, "#")
        #         changed = True

        #     while self.grid.try_get(x, y):
        #         if (x, y, direction) in visited:
        #             total += 1
        #             break
        #         visited.add((x, y, direction))
        #         next_char = self.peek(x, y, direction)
        #         if next_char == "#":
        #             direction = Direction.roate_right(direction)
        #         x, y = self.move(x, y, direction)

        #     if changed:
        #         self.grid.set(p.x, p.y, ".")
        # return str(total)
        return ""

    def peek(self, x: int, y: int, direction: Direction) -> str | None:
        match direction:
            case Direction.UP:
                return self.grid.get(x, y - 1) if self.grid.try_get(x, y - 1) else None
            case Direction.RIGHT:
                return self.grid.get(x + 1, y) if self.grid.try_get(x + 1, y) else None
            case Direction.DOWN:
                return self.grid.get(x, y + 1) if self.grid.try_get(x, y + 1) else None
            case Direction.LEFT:
                return self.grid.get(x - 1, y) if self.grid.try_get(x - 1, y) else None

    def move(self, x: int, y: int, direction: Direction) -> tuple[int, int]:
        match direction:
            case Direction.UP:
                return (x, y - 1)
            case Direction.RIGHT:
                return (x + 1, y)
            case Direction.DOWN:
                return (x, y + 1)
            case Direction.LEFT:
                return (x - 1, y)


# 1893 - too low
