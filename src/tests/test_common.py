import pytest

from src.common.equations import quadratic, binary_permutations
from src.common.extensions import flatten, single
from src.common.grid import Grid, Point, points_between
from src.common.parsing import extract_integer, extract_integers

small_grid_input = """1 2 3
4 5 6
7 8 9
""".splitlines()


def test_single() -> None:
    set_of_one = {"A"}
    assert single(set_of_one) == "A"


def test_grid() -> None:
    grid: Grid[int] = Grid.from_lines(small_grid_input, lambda x: int(x))
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
        assert Point(0, 0) < Point(5, 5)  # type: ignore
    with pytest.raises(TypeError):
        assert Point(0, 0) > Point(5, 5)  # type: ignore


def test_point_add() -> None:
    p1 = Point(2, 4)
    p2 = Point(3, 7)
    assert p1 + p2 == Point(5, 11)


def test_point_subtract() -> None:
    p1 = Point(10, 5)
    p2 = Point(12, 4)
    assert p1 - p2 == Point(-2, 1)

def test_grid_yield_all_points():
    points: list[Point] = list()
    grid: Grid[int] = Grid.from_lines(small_grid_input, lambda x: int(x))
    for p in grid.iter_points():
        points.append(p)
    assert len(points) == 9

@pytest.mark.parametrize("target, expected", [(1, (0, 0)), (4, (0, 1)), (10, None)])
def test_find(target: int, expected: tuple[int, int] | None) -> None:
    grid = Grid.from_lines_to_int_grid(small_grid_input, True)
    assert grid.find(target) == expected


@pytest.mark.parametrize(
    "point1, point2, expected",
    [(Point(0, 0), Point(0, 0), True), (Point(1, 2), Point(1, 2), True), (Point(7, 1), Point(6, 1), False)],
)
def test_hash_equality(point1: Point, point2: Point, expected: bool) -> None:
    actual = hash(point1) == hash(point2)
    assert actual is expected


def test_hash_point_in_set_should_be_true():
    s = {Point(0, 0), Point(-1, -5)}
    result = Point(-1, -5) in s
    assert result is True


def test_hash_point_in_set_should_be_false():
    s = {Point(0, 0), Point(-1, -5)}
    result = Point(100, -5) in s
    assert result is False


@pytest.mark.parametrize(
    "nested_array, flattened_array",
    [([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]), ([[[]]], [])],
)
def test_flatten_array(nested_array, flattened_array: list[int]):
    actual = flatten(nested_array)
    assert actual == flattened_array


@pytest.mark.parametrize(
    "start, end, expected",
    [
        [(498, 4), (498, 6), [Point(498, 4), Point(498, 5), Point(498, 6)]],
        [(498, 6), (496, 6), [Point(498, 6), Point(497, 6), Point(496, 6)]],
    ],
)
def test_bresenhams_algo(start: tuple[int, int], end: tuple[int, int], expected: list[Point]):
    start_point = Point(start[0], start[1])
    end_point = Point(end[0], end[1])
    points = points_between(start_point, end_point)
    assert points == expected


@pytest.mark.parametrize(
    "string, expected", [("Game 10", 10), ("101 Dalmations", 101), ("No numbers here", None)]
)
def test_extract_integer(string: str, expected: int):
    actual = extract_integer(string)
    assert actual == expected


@pytest.mark.parametrize("string, expected", [("seeds: 79 14 55 13", [79, 14, 55, 13])])
def test_extract_integers(string: str, expected: list[int]):
    actual = extract_integers(string)
    assert actual == expected


@pytest.mark.parametrize("a, b, c, expected", [(1, -1, -2, (-1, 2))])
def test_quadratic_equation_solver(a: int, b: int, c: int, expected: tuple[int, int]):
    root1, root2 = quadratic(a, b, c)
    assert {root1, root2} == set(expected)


def test_binary_permutations():
    result = binary_permutations(4)
    assert len(result) == 16
