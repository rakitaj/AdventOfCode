from src.common.dataload import DataLoader
from src.common.grid import Grid


def visible_trees(grid: Grid[int]) -> set[tuple[int, int]]:
    visible_trees_set: set[tuple[int, int]] = set()
    # Check horiz line.
    for y in range(grid.y_size):
        for x in range(grid.x_size):
            if others_lower_horiz(grid, x, y):
                visible_trees_set.add((x, y))
                continue
            if others_lower_vert(grid, x, y):
                visible_trees_set.add((x, y))
                continue
    return visible_trees_set


def others_lower_horiz(grid: Grid[int], x: int, y: int) -> bool:
    val = grid.get(x, y)
    left_lower = True
    right_lower = True
    if x == 0 or x == grid.x_size - 1:
        return True
    for i in range(x):
        if val <= grid.get(i, y):
            left_lower = False
            break
    for i in range(x + 1, grid.x_size):
        if val <= grid.get(i, y):
            right_lower = False
            break
    return left_lower or right_lower


def others_lower_vert(grid: Grid[int], x: int, y: int) -> bool:
    val = grid.get(x, y)
    up_lower = True
    down_lower = True
    if y == 0 or y == grid.y_size - 1:
        return True
    for i in range(y):
        if val <= grid.get(x, i):
            up_lower = False
            break
    for i in range(y + 1, grid.y_size):
        if val <= grid.get(x, i):
            down_lower = False
            break
    return up_lower or down_lower


# def flood_fill_trees(grid: Grid[int]) -> int:
#     max_score = 0
#     for y in range(grid.y_size):
#         for x in range(grid.x_size):
#             score = flood_fill(grid, x, y, 0)
#             max_score = max(score, max_score)
#     return max_score

# def flood_fill(grid: Grid[int], x: int, y: int) -> int:


class FloodFillTrees:
    def __init__(self, grid: Grid[int]):
        self.grid = grid


def part01_answer() -> str:
    loader = DataLoader(2022, "day08.txt")
    data = loader.readlines_str(trim=True)
    grid = Grid.from_lines_to_int_grid(data, False)
    actual = visible_trees(grid)
    return str(len(actual))
