from __future__ import annotations
from typing import TypeVar, Generic, Callable

T = TypeVar("T")


class Grid(Generic[T]):
    def __init__(self, x_size: int, y_size: int):
        self.x_size = x_size
        self.y_size = y_size
        self.g: list[list[T]] = list()

    def get(self, x: int, y: int) -> T:
        return self.g[y][x]

    @staticmethod
    def from_lines(lines: list[str], convert_func: Callable[[str], T]) -> Grid[T]:
        x_size = len(lines[0])
        y_size = len(lines)
        grid: Grid[T] = Grid(x_size=x_size, y_size=y_size)
        for horizontal_line in lines:
            converted_y_line = [convert_func(x_item) for x_item in horizontal_line.split()]
            grid.g.append(converted_y_line)
        return grid
