from src.common.grid import Grid


def visible_trees(grid: Grid[int]) -> int:
    visible_trees_set: set[tuple[int, int]] = set()
    # Check horiz line.
    for y in range(grid.y_size):
        for x in range(grid.x_size):
            if others_lower_horiz(grid, x, y):
                visible_trees_set.add((x, y))
            if others_lower_vert(grid, x, y):
                visible_trees_set.add((x, y))
    return len(visible_trees_set)


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
    for i in range(x, grid.x_size):
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
    for i in range(y, grid.y_size):
        if val <= grid.get(x, i):
            down_lower = False
            break
    return up_lower or down_lower
