import pytest
from src.common.extensions import single
from src.common.grid import Grid, Point

small_grid_input = """1 2 3
4 5 6
7 8 9
""".splitlines()


def test_single() -> None:
    set_of_one = {"A"}
    assert single(set_of_one) == "A"


def test_grid() -> None:
    grid = Grid.from_lines(small_grid_input, lambda x: int(x))
    assert grid.get(0, 0) == 1
    assert grid.get(1, 0) == 2
    assert grid.get(1, 2) == 8


@pytest.mark.parametrize("x, y, expected", [(0, 0, True), (2, 2, True), (2, 3, False), (3, 2, False)])
def test_grid_tryget(x: int, y: int, expected: bool) -> None:
    grid = Grid.from_lines_to_int_grid(small_grid_input, True)
    assert grid.try_get(x, y) is expected


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected", [(0, 0, 0, 0, True), (2, 12, 2, 12, True), (1, 0, 0, 1, False)]
)
def test_point_equality(x1: int, y1: int, x2: int, y2: int, expected: bool) -> None:
    actual = Point(x1, y1) == Point(x2, y2)
    assert actual is expected


def test_point_equality_different_types() -> None:
    assert Point(3, 4) != (3, 4)


def test_point_gt_lt_should_raise() -> None:
    with pytest.raises(TypeError):
        Point(0, 0) < Point(5, 5)  # type: ignore
    with pytest.raises(TypeError):
        Point(0, 0) > Point(5, 5)  # type: ignore


@pytest.mark.parametrize("target, expected", [(1, (0, 0)), (4, (0, 1)), (10, None)])
def test_find(target: int, expected: tuple[int, int] | None) -> None:
    grid = Grid.from_lines_to_int_grid(small_grid_input, True)
    assert grid.find(target) == expected
