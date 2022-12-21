import pytest
from src.aoc2022.day02 import rock_paper_scissors, rock_paper_scissors_2


@pytest.mark.parametrize(
    "opponent, me, expected",
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
def test_rock_paper_scissors(opponent: str, me: str, expected: int):
    actual = rock_paper_scissors(opponent, me)
    assert actual == expected


@pytest.mark.parametrize(
    "opponent, outcome, expected",
    [
        ("A", "Y", 4),
        ("B", "X", 1),
        ("C", "Z", 7),
    ],
)
def test_rock_paper_scissors_outcome(opponent: str, outcome: str, expected: int):
    actual = rock_paper_scissors_2(opponent, outcome)
    assert actual == expected
