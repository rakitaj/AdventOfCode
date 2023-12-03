from __future__ import annotations
from typing import Callable, Sequence

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, type(self)):
            return self.x == __o.x and self.y == __o.y
        return False

    def __repr__(self) -> str:
        return f"Point {{x:{self.x}, y:{self.y}}}"

    def to_tuple(self) -> tuple[int, int]:
        return (self.x, self.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))


def points_between(start: Point, end: Point) -> list[Point]:
    """
    Use Bresenham's line algorithm to find all points on a line between two Point objects.
    https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
    """
    return _points_between(start, end)


def _points_between(p0: Point, p1: Point) -> list[Point]:
    result: list[Point] = list()
    x0, y0 = p0.to_tuple()
    x1, y1 = p1.to_tuple()
    # Vertical line
    if x1 - x0 == 0:
        for i in range(abs(y1 - y0) + 1):
            if y1 - y0 > 0:
                result.append(Point(x0, y0 + i))
            else:
                result.append(Point(x0, y0 - i))
    # Horizontal line
    else:
        for i in range(abs(x1 - x0) + 1):
            if x1 - x0 > 0:
                result.append(Point(x0 + i, y0))
            else:
                result.append(Point(x0 - i, y0))
    return result


class Grid[T]:
    def __init__(self, x_size: int, y_size: int, contents: list[T]):
        if len(contents) != x_size * y_size:
            raise ValueError(f"Size {contents} is not equal to {x_size} * {y_size}")
        self.x_size = x_size
        self.y_size = y_size
        self.g = contents

    def get(self, x: int, y: int) -> T:
        index = (y * self.x_size) + x
        return self.g[index]

    def try_get(self, x: int, y: int) -> bool:
        """Check if the (x, y) coordinate is within the bounds of the grid."""
        # x_in_bounds = (0 <= x) and (x < self.x_size)
        # y_in_bounds = (0 <= y) and (y < self.y_size)
        # return x_in_bounds and y_in_bounds
        return ((0 <= x) and (x < self.x_size)) and ((0 <= y) and (y < self.y_size))

    def find(self, target: T) -> tuple[int, int] | None:
        """Find the first occurance of the target in the grid."""
        for i, e in enumerate(self.g):
            if e == target:
                y = i // self.x_size
                x = i % self.x_size
                return (x, y)
        return None

    def find_all(self, target: T) -> list[tuple[int, int]]:
        result = list()
        for i, e in enumerate(self.g):
            if e == target:
                y = i // self.x_size
                x = i % self.x_size
                result.append((x, y))
        return result

    def moves(self, x: int, y: int) -> list[tuple[int, int]]:
        valid_moves: list[tuple[int, int]] = list()
        potential_moves = [
            (x - 1, y + 1),
            (x - 1, y),
            (x - 1, y - 1),
            (x, y + 1),
            (x, y - 1),
            (x + 1, y + 1),
            (x + 1, y),
            (x + 1, y - 1),
        ]
        for move in potential_moves:
            if self.try_get(move[0], move[1]) is True:
                valid_moves.append(move)
        return valid_moves

    def moves_cardinal(self, x: int, y: int) -> list[tuple[int, int]]:
        valid_moves: list[tuple[int, int]] = list()
        potential_moves = [
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
            (x + 1, y),
        ]
        for move in potential_moves:
            if self.try_get(move[0], move[1]) is True:
                valid_moves.append(move)
        return valid_moves

    @staticmethod
    def from_lines(lines: Sequence[str], convert_func: Callable[[str], T], split: bool = True) -> Grid[T]:
        contents: list[T] = list()
        x_size = 0
        for horizontal_line in lines:
            if split:
                converted_horizontal_line = [convert_func(x_item) for x_item in horizontal_line.split()]
            else:
                converted_horizontal_line = [convert_func(x_item) for x_item in horizontal_line]
            x_size = len(converted_horizontal_line)
            contents.extend(converted_horizontal_line)
        y_size = len(lines)
        grid: Grid[T] = Grid(x_size=x_size, y_size=y_size, contents=contents)
        return grid

    @staticmethod
    def from_lines_to_int_grid(lines: Sequence[str], split: bool) -> Grid[int]:
        return Grid.from_lines(lines, lambda x: int(x), split)

    @staticmethod
    def from_strings_no_spaces(lines: list[str]) -> Grid[str]:
        x_size = len(lines[0])
        y_size = len(lines)
        result: list[str] = list()
        for line in lines:
            result.extend(line)
        grid = Grid(x_size, y_size, result)
        return grid


class Distances:
    def __init__(self, up: int, down: int, left: int, right: int):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def reset(self) -> None:
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0
