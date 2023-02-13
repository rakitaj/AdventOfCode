from src.common.grid import Grid, Point
from src.aoc2022.day12 import convert

small_data = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".splitlines()


def test_parse_to_grid():
    grid = Grid.from_lines(small_data)
    assert grid.get(0, 0) == "S"
