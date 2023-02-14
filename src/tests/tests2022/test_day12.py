from src.common.grid import Grid, Point


small_data = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".splitlines()


def test_parse_to_grid():
    grid = Grid.from_strings_no_spaces(small_data)
    assert grid.get(0, 0) == "S"
