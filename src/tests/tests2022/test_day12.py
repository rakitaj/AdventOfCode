import pytest
from src.common.grid import Grid, Point
from src.aoc2022.day12 import find_start, find_end, find_path, find_path_bfs


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
    result = find_path(grid, start)
    assert result is not None
    distance, x, y = result
    assert distance == 31 and (x, y) == end.to_tuple()


def test_pathfinding_bfs():
    grid = Grid.from_strings_no_spaces(small_data)
    start = find_start(grid)
    distance = find_path_bfs(grid, start)
    assert distance == 31
