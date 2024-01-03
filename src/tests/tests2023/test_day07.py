import pytest
from src.aoc2023.day07 import (
    compare_hands,
    Hand,
    HandType,
    parse_to_hand,
    calcuate_answer,
    parse_to_hand_2,
    compare_hands_2,
)


@pytest.mark.parametrize(
    "hand1, hand2, expected",
    [
        (Hand(HandType.PAIR_2, "23432", 28), Hand(HandType.PAIR_2, "23432", 28), 0),
        (Hand(HandType.FULL_HOUSE, "KK888", 100), Hand(HandType.KIND_3, "44423", 200), 1),
        (Hand(HandType.PAIR_1, "QQ567", 123), Hand(HandType.PAIR_1, "QQ567", 123), 0),
        (Hand(HandType.PAIR_1, "QQ565", 321), Hand(HandType.PAIR_1, "QQ567", 509), -1),
        (Hand(HandType.KIND_4, "J5555", 555), Hand(HandType.KIND_4, "T5555", 555), 1),
    ],
)
def test_compare_hands(hand1: Hand, hand2: Hand, expected: int):
    assert compare_hands(hand1, hand2) == expected


@pytest.mark.parametrize(
    "hand_str, expected",
    [("23432 101", Hand(HandType.PAIR_2, "23432", 101)), ("AAAAA 28", Hand(HandType.KIND_5, "AAAAA", 28))],
)
def test_parse_to_hand(hand_str: str, expected: Hand):
    assert parse_to_hand(hand_str) == expected


def test_compute_part1_answer():
    lines = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()
    answer = calcuate_answer(lines, parse_func=parse_to_hand, compare_func=compare_hands)
    assert answer == 6440


def test_compute_part2_answer():
    lines = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()
    answer = calcuate_answer(lines, parse_func=parse_to_hand_2, compare_func=compare_hands_2)
    assert answer == 5905


def test_compute_part2_answer_2():
    lines = """JAAKK 1
JJJAK 2""".splitlines()
    answer = calcuate_answer(lines, parse_func=parse_to_hand_2, compare_func=compare_hands_2)
    assert answer == 5
