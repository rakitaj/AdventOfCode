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


class FloodFillTrees:
    def __init__(self, grid: Grid[int]):
        self.grid = grid
        self.max_score = 0
        self.distances = [0, 0, 0, 0]

    def find_max(self) -> None:
        for y in range(self.grid.y_size):
            for x in range(self.grid.x_size):
                self._find_max(x, y)
                score = self.distances[0] * self.distances[1] * self.distances[2] * self.distances[3]
                self.max_score = max(score, self.max_score)
                self.distances = [0, 0, 0, 0]

    def _find_max(self, x: int, y: int) -> None:
        val = self.grid.get(x, y)
        orig = (x, y)
        while self.grid.try_get(x - 1, y) is True and self.grid.get(x - 1, y) < val:
            self.distances[0] += 1
            x -= 1
        x, y = orig
        while self.grid.try_get(x + 1, y) is True and self.grid.get(x + 1, y) < val:
            self.distances[1] += 1
            x += 1
        x, y = orig
        while self.grid.try_get(x, y + 1) is True and self.grid.get(x, y + 1) < val:
            self.distances[2] += 1
            y += 1
        x, y = orig
        while self.grid.try_get(x, y - 1) is True and self.grid.get(x, y - 1) < val:
            self.distances[3] -= 1
            y -= 1


def part01_answer() -> str:
    loader = DataLoader(2022, "day08.txt")
    data = loader.readlines_str(trim=True)
    grid = Grid.from_lines_to_int_grid(data, False)
    actual = visible_trees(grid)
    return str(len(actual))
