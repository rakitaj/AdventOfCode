from __future__ import annotations
from typing import TypeVar, Generic, Callable

T = TypeVar("T")


class Grid(Generic[T]):
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
        x_in_bounds = (0 <= x) and (x < self.x_size)
        y_in_bounds = (0 <= y) and (y < self.y_size)
        return x_in_bounds and y_in_bounds

    @staticmethod
    def from_lines(lines: list[str], convert_func: Callable[[str], T], split: int = True) -> Grid[T]:
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
    def from_lines_to_int_grid(lines: list[str], split: bool) -> Grid[int]:
        return Grid.from_lines(lines, lambda x: int(x), split)


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
