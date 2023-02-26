import pytest
from src.common.grid import Grid, Point
from src.aoc2022.day12 import find_start, find_end, find_path


small_data = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".splitlines()


@pytest.mark.parametrize("x, y, expected", [(0, 0, "S"), (5, 2, "E"), (7, 4, "i")])
def test_parse_to_grid(x: int, y: int, expected: str):
    grid = Grid.from_strings_no_spaces(small_data)
    assert grid.get(x, y) == expected


def test_find_start_and_end():
    grid = Grid.from_strings_no_spaces(small_data)
    start = find_start(grid)
    end = find_end(grid)
    assert start == Point(0, 0)
    assert end == Point(5, 2)


def test_pathfinding():
    grid = Grid.from_strings_no_spaces(small_data)
    start = find_start(grid)
    end = find_end(grid)
    path = find_path(grid, start, end)
    assert len(path) - 1 == 31
    # assert path == [
    #     Point(0, 0),
    #     Point(0, 1),
    #     Point(1, 1),
    #     Point(1, 2),
    #     Point(2, 2),
    #     Point(2, 3),
    #     Point(2, 4),
    #     Point(3, 4),
    #     Point(4, 4),
    #     Point(5, 4),
    #     Point(6, 4),
    #     Point(7, 4),
    #     Point(7, 3),
    #     Point(7, 2),
    #     Point(7, 1),
    #     Point(7, 0),
    #     Point(6, 0),
    #     Point(5, 0),
    #     Point(4, 0),
    #     Point(3, 0),
    #     Point(3, 1),
    #     Point(3, 2),
    #     Point(3, 3),
    #     Point(4, 3),
    #     Point(5, 3),
    #     Point(6, 3),
    #     Point(6, 2),
    #     Point(6, 1),
    #     Point(5, 1),
    #     Point(4, 1),
    #     Point(4, 2),
    #     Point(5, 2),
    # ]
