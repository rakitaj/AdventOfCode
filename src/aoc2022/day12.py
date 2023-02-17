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
    acc: list[Point] = list()
    for move in grid.moves(start.x, start.y):
        p = Point(move[0], move[1])
        _find_path(grid, p, acc)
    return acc


def _find_path(grid: Grid[str], current: Point, acc: list[Point]) -> None:
    acc.append(current)
    current_val = grid.get(current.x, current.y)
    if current_val == "E":
        return
    current_ord = ord(current_val)
    for x, y in grid.moves(current.x, current.y):
        next_val = grid.get(x, y)
        next_ord = ord(next_val)
        if next_ord - current_ord == 0 or next_ord - current_ord == 1:
            next_p = Point(x, y)
            _find_path(grid, next_p, acc)
    acc.pop()
