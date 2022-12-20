import pytest
from src.aoc2022.day03 import priority, priority_of_backpack


@pytest.mark.parametrize("char, expected", [("a", 1), ("z", 26), ("A", 27), ("Z", 52)])
def test_priority(char: str, expected: int):
    actual = priority(char)
    assert actual is expected


@pytest.mark.parametrize("backpack_contents, expected", [("vJrwpWtwJgWrhcsFMMfFFhFp", 16)])
def test_priority_of_backpack(backpack_contents: str, expected: int):
    actual = priority_of_backpack(backpack_contents)
    assert actual == expected
