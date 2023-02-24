from src.common.grid import Grid, Point


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
    result: list[Point] = list()

    while 0 < len(queue):
        current = queue.pop(len(queue) - 1)
        visited.add(current)
        result.append(current)
        current_val = grid.get(current.x, current.y)
        current_ord = ord_override(current_val)
        if current_val == "E":
            break
        for x, y in grid.moves_cardinal(current.x, current.y):
            next_val = grid.get(x, y)
            next_ord = ord_override(next_val)
            next_p = Point(x, y)
            if next_ord - current_ord in [0, 1] and next_p not in visited:
                queue.append(Point(x, y))
    return result


def ord_override(char: str) -> int:
    if char == "S":
        return 0
    elif char == "E":
        return 123
    else:
        return ord(char) - 97
