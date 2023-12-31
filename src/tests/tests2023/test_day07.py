import pytest
from src.aoc2023.day07 import compare_hands, Hand, HandType


@pytest.mark.parametrize(
    "hand1, hand2, expected",
    [
        (Hand(HandType.PAIR_2, "23432"), Hand(HandType.PAIR_2, "23432"), 0),
        (Hand(HandType.FULL_HOUSE, "KK888"), Hand(HandType.KIND_3, "44423"), 1),
        (Hand(HandType.PAIR_1, "QQ567"), Hand(HandType.PAIR_1, "QQ567"), 0),
        (Hand(HandType.PAIR_1, "QQ565"), Hand(HandType.PAIR_1, "QQ567"), -1),
    ],
)
def test_compare_hands(hand1: Hand, hand2: Hand, expected: int):
    assert compare_hands(hand1, hand2) == expected
