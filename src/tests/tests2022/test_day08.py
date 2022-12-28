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
    visible_set = {
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (4, 0),
        (4, 1),
        (4, 2),
        (4, 3),
        (4, 4),
        (1, 4),
        (2, 4),
        (3, 4),
        (1, 1),
        (2, 1),
        (1, 2),
        (3, 2),
        (2, 3),
    }
    assert visible_set == actual
