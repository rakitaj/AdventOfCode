from src.common.grid import Grid
from src.aoc2022.day08 import visible_trees

tiny_data = """30373
25512
65332
33549
35390""".splitlines()


def test_visible_trees():
    grid = Grid.from_lines_to_int_grid(tiny_data, False)
    actual = visible_trees(grid)
    assert actual == 21
