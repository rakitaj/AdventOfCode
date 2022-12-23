from src.common.extensions import single
from src.common.grid import Grid


def test_single():
    set_of_one = {"A"}
    assert single(set_of_one) == "A"


def test_grid():
    lines = """1 2 3
4 5 6
7 8 9
""".splitlines()
    grid = Grid.from_lines(lines, lambda x: int(x))
    assert grid.get(0, 0) == 1
    assert grid.get(1, 0) == 2
    assert grid.get(1, 2) == 8
