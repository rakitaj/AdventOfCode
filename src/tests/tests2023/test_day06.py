from src.aoc2023.day06 import BoatRace, calculate_how_to_win, calculate_how_to_win_math


def test_calculate_how_to_win():
    actual = calculate_how_to_win(7, 9)
    assert actual == [2, 3, 4, 5]


def test_calculate_how_to_win_math():
    actual = calculate_how_to_win_math(7, 9)
    assert actual == 4


def test_real_data():
    race = BoatRace(40709879, 215105121471005)
    wins = calculate_how_to_win_math(race.time, race.max_distance)
    assert wins == 28228952
