from src.common.grid import Grid, Point
from src.aoc2024.day04 import find_sequence_8_directions, xmas_cross

lines = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()

XMAS = ["X", "M", "A", "S"]


def test_find_sequence_in_good_spot():
    grid = Grid.from_strings_no_spaces(lines)
    start = Point(4, 0)
    result = find_sequence_8_directions(grid, start, XMAS)
    assert result == 1


def test_find_sequence_in_bad_spot():
    grid = Grid.from_strings_no_spaces(lines)
    start = Point(6, 0)
    result = find_sequence_8_directions(grid, start, XMAS)
    assert result == 0


def test_find_sequence_test_data():
    grid = Grid.from_strings_no_spaces(lines)
    total = 0
    for point in grid.iter_points():
        point_count = find_sequence_8_directions(grid, point, XMAS)
        total += point_count
    assert total == 18


def test_xmas_crosses():
    grid = Grid.from_strings_no_spaces(lines)
    total = 0
    for point in grid.iter_points():
        if xmas_cross(grid, point):
            total += 1
            print(point)
    assert total == 9
