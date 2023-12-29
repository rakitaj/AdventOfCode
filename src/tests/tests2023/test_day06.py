from src.aoc2023.day06 import calculate_how_to_win


def test_calculate_how_to_win():
    actual = calculate_how_to_win(7, 9)
    assert actual == [2, 3, 4, 5]
