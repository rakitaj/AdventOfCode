import pytest
from src.aoc2024.day07 import parse_line, calculator


@pytest.mark.parametrize("line", ["190: 10 19", "3267: 81 40 27", "292: 11 6 16 20"])
def test_calculate_add_and_mult_known_good(line: str):
    target, numbers = parse_line(line)
    assert calculator(target, numbers, False) is True


@pytest.mark.parametrize("line", ["83: 17 5", "156: 15 6", "7290: 6 8 6 15", "161011: 16 10 13", "192: 17 8 14", "21037: 9 7 18 13"])
def test_calculate_add_and_mult_known_bad(line: str):
    target, numbers = parse_line(line)
    assert calculator(target, numbers, False) is False


@pytest.mark.parametrize("line", ["190: 10 19", "3267: 81 40 27", "292: 11 6 16 20", "156: 15 6", "7290: 6 8 6 15", "192: 17 8 14"])
def test_calculate_add_and_mult_known_good_with_concat(line: str):
    target, numbers = parse_line(line)
    assert calculator(target, numbers, True) is True


@pytest.mark.parametrize("line", ["83: 17 5", "161011: 16 10 13", "21037: 9 7 18 13"])
def test_calculate_add_and_mult_known_bad_with_concat(line: str):
    target, numbers = parse_line(line)
    assert calculator(target, numbers, True) is False
