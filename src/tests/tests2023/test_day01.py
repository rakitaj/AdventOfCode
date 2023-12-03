from src.aoc2023.day01 import parse_digits, parse_string_digits, _part02_answer
import pytest


@pytest.mark.parametrize(
    "line, expected", [("1abc2", 12), ("pqr3stu8vwx", 38), ("a1b2c3d4e5f", 15), ("treb7uchet", 77)]
)
def test_parse_digits(line: str, expected: int):
    actual = parse_digits(line)
    assert actual == expected


@pytest.mark.parametrize(
    "line, expected",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ],
)
def test_parse_string_digits(line: str, expected: int):
    actual = parse_string_digits(line)
    assert actual == expected


def test_part_2_answer():
    test_data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()
    actual = _part02_answer(test_data)
    assert actual == 281
