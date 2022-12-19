import pytest
from src.aoc2022.day02 import rock_paper_scissors


@pytest.mark.parametrize(
    "me, opponent, expected",
    [
        ("A", "X", 4),
        ("A", "Y", 8),
        ("A", "Z", 3),
        ("B", "X", 1),
        ("B", "Y", 5),
        ("B", "Z", 9),
        ("C", "X", 7),
        ("C", "Y", 2),
        ("C", "Z", 6),
    ],
)
def test_rock_paper_scissors(me: str, opponent: str, expected: int):
    actual = rock_paper_scissors(me, opponent)
    assert actual == expected
