from heapq import heappop, heappush
from string import ascii_lowercase
from typing import Callable

from src.common.dataload import DataLoader
from src.common.grid import Grid, Point


def height(s: str) -> int:
    if s == "S":
        return 0
    elif s == "E":
        return 25
    else:
        return ascii_lowercase.index(s)


def find_start(grid: Grid[str]) -> Point:
    start = grid.find("S")
    if start is None:
        raise ValueError("Grid diesn't have a starting point.")
    else:
        return Point(start[0], start[1])


def find_end(grid: Grid[str]) -> Point:
    start = grid.find("E")
    if start is None:
        raise ValueError("Grid diesn't have an ending point.")
    else:
        return Point(start[0], start[1])


def find_path(grid: Grid[str], start: Point) -> tuple[int, int, int] | None:
    result = find_path_core(
        grid, start, "E", lambda next_height, current_height: next_height - current_height <= 1
    )
    return result


def find_path_backwards(grid: Grid[str]) -> tuple[int, int, int] | None:
    # When going backwards actually start at the end
    start = find_end(grid)
    result = find_path_core(
        grid, start, "a", lambda next_height, current_height: current_height - next_height <= 1
    )
    return result


def find_path_core(
    grid: Grid[str], start: Point, end: str, conditional: Callable[[int, int], bool]
) -> tuple[int, int, int] | None:
    queue: list[tuple[int, int, int]] = [(0, start.x, start.y)]
    visited: set[tuple[int, int]] = set()

    while 0 < len(queue):
        distance, x, y = heappop(queue)
        current_val = grid.get(x, y)
        if current_val == end:
            return (distance, x, y)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for nx, ny in grid.moves_cardinal(x, y):
            next_val = grid.get(nx, ny)
            if conditional(height(next_val), height(current_val)):
                heappush(queue, (distance + 1, nx, ny))
    return None


def find_path_bfs(grid: Grid[str], start: Point) -> int:
    queue: list[tuple[int, int]] = [(start.x, start.y)]
    visited: set[tuple[int, int]] = set()
    depth_queue: list[int] = [0]

    while 0 < len(queue):
        depth = depth_queue.pop(0)
        x, y = queue.pop(0)
        current_val = grid.get(x, y)
        if current_val == "E":
            return depth
        for nx, ny in grid.moves_cardinal(x, y):
            next_val = grid.get(nx, ny)
            if (nx, ny) not in visited and height(next_val) - height(current_val) <= 1:
                queue.append((nx, ny))
                depth_queue.append(depth + 1)
                visited.add((nx, ny))
    return -1


def part01_answer() -> str:
    loader = DataLoader(2022, "day12.txt")
    data = loader.readlines_str(trim_newlines=True)
    grid = Grid.from_strings_no_spaces(data)
    start = find_start(grid)
    result = find_path(grid, start)
    return str(result)


def part02_answer() -> str:
    loader = DataLoader(2022, "day12.txt")
    data = loader.readlines_str(trim_newlines=True)
    grid = Grid.from_strings_no_spaces(data)
    result = find_path_backwards(grid)
    if result is not None:
        return str(result)
    else:
        return "No path found."
