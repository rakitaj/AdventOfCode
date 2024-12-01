import pytest

from src.aoc2022.day04 import SegmentLocations


@pytest.mark.parametrize(
    "start_one, end_one, start_two, end_two, expected",
    [(2, 4, 6, 8, 0), (2, 3, 4, 5, 0), (5, 7, 7, 9, 1), (2, 8, 3, 7, 1), (6, 6, 4, 6, 1), (2, 6, 4, 8, 1)],
)
def test_check_overlapping_any(start_one: int, end_one: int, start_two: int, end_two: int, expected: int):
    sl = SegmentLocations(start_one, end_one, start_two, end_two)
    assert sl.any_overlap() == expected
