import pytest
from src.aoc2023.day02 import parse_and_test_line, CubeCounts

cube_predicate = CubeCounts(12, 13, 14)


@pytest.mark.parametrize(
    "line, is_possible",
    [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", True),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", True),
        ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", False),
        ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", False),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", True),
    ],
)
def test_parse_and_test_cube_game(line: str, is_possible: bool):
    actual = parse_and_test_line(line, cube_predicate)
    assert actual is is_possible
