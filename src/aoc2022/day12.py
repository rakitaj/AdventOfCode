from src.common.grid import Grid, Point
from src.common.dataload import DataLoader


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


def find_path(grid: Grid[str], start: Point, end: Point) -> list[Point]:
    queue: list[Point] = [start]
    visited: set[Point] = set()
    edge_to: dict[Point, Point | None] = {start: None}

    while 0 < len(queue):
        current = queue.pop(0)
        visited.add(current)
        current_val = grid.get(current.x, current.y)
        current_ord = ord_override(current_val)
        if current_val == "E":
            return path(edge_to, current)
        for x, y in grid.moves_cardinal(current.x, current.y):
            next_val = grid.get(x, y)
            next_ord = ord_override(next_val)
            next_p = Point(x, y)
            if next_ord - current_ord <= 1 and next_p not in visited:
                queue.append(Point(x, y))
                edge_to[next_p] = current
    raise ValueError("No path found.")


def path(edge_to: dict[Point, Point | None], end_point: Point) -> list[Point]:
    current: Point | None = end_point
    result: list[Point] = list()
    while current is not None:
        result.append(current)
        current = edge_to[current]
    result.reverse()
    return result


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
    end = find_end(grid)
    path = find_path(grid, start, end)
    return str(len(path) - 1)
