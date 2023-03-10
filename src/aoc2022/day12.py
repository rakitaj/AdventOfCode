from src.common.grid import Grid, Point
from src.common.dataload import DataLoader
from heapq import heappop, heappush


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
    queue: list[tuple[int, int, int]] = [(0, start.x, start.y)]
    visited: set[tuple[int, int]] = set()

    while 0 < len(queue):
        distance, x, y = heappop(queue)
        current_val = grid.get(x, y)
        if current_val == "E":
            return (distance, x, y)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for nx, ny in grid.moves_cardinal(x, y):
            next_val = grid.get(nx, ny)
            if ord_override(next_val) - ord_override(current_val) <= 1:
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
            if (nx, ny) not in visited and ord_override(next_val) - ord_override(current_val) <= 1:
                queue.append((nx, ny))
                depth_queue.append(depth + 1)
                visited.add((nx, ny))
    return -1


def ord_override(char: str) -> int:
    if char == "S":
        return 0
    elif char == "E":
        return ord("z") - ord("a")
    else:
        return ord(char) - ord("a")


def part01_answer() -> str:
    loader = DataLoader(2022, "day12.txt")
    data = loader.readlines_str()
    grid = Grid.from_strings_no_spaces(data)
    start = find_start(grid)
    result = find_path_bfs(grid, start)
    return str(result)


def part02_answer() -> str:
    loader = DataLoader(2022, "day12.txt")
    data = loader.readlines_str()
    grid = Grid.from_strings_no_spaces(data)
    starts = grid.find_all("a")
    distances: list[int] = list()
    for start in starts:
        path_result = find_path(grid, Point(start[0], start[1]))
        if path_result is not None:
            distances.append(path_result[0])
    return str(min(distances))
