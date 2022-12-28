import pytest
from src.common.extensions import single
from src.common.grid import Grid

small_grid_input = """1 2 3
4 5 6
7 8 9
""".splitlines()


def test_single():
    set_of_one = {"A"}
    assert single(set_of_one) == "A"


def test_grid():
    grid = Grid.from_lines(small_grid_input, lambda x: int(x))
    assert grid.get(0, 0) == 1
    assert grid.get(1, 0) == 2
    assert grid.get(1, 2) == 8


@pytest.mark.parametrize("x, y, expected", [(0, 0, True), (2, 2, True), (2, 3, False), (3, 2, False)])
def test_grid_tryget(x: int, y: int, expected: bool):
    grid = Grid.from_lines_to_int_grid(small_grid_input, True)
    assert grid.try_get(x, y) is expected
