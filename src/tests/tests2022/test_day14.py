import pytest
from src.common.grid import Point
from src.aoc2022.day14 import parse_line


@pytest.mark.parametrize(
    "line, expected",
    [
        ("498,4 -> 498,6 -> 496,6", [(498, 4), (498, 6), (496, 6)]),
        ("503,4 -> 502,4 -> 502,9 -> 494,9", [(503, 4), (502, 4), (502, 9), (494, 9)]),
    ],
)
def test_parse_line(line: str, expected: list[tuple[int, int]]):
    expected_points = list()
    for coordinates in expected:
        x, y = coordinates
        expected_points.append(Point(x, y))
    assert parse_line(line) == expected_points
