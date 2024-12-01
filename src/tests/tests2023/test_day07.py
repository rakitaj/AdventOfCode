import pytest

from src.aoc2023.day07 import (
    Hand,
    HandType,
    calcuate_answer,
    parse_to_hand,
    parse_to_hand_2,
)

part_1_strategy = lambda x: x.CARD_RANK


@pytest.mark.parametrize(
    "hand1, hand2, expected",
    [
        (
            Hand(HandType.PAIR_2, "23432", 28, part_1_strategy),
            Hand(HandType.PAIR_2, "23432", 28, part_1_strategy),
            False,
        ),
        (
            Hand(HandType.FULL_HOUSE, "KK888", 100, part_1_strategy),
            Hand(HandType.KIND_3, "44423", 200, part_1_strategy),
            False,
        ),
        (
            Hand(HandType.PAIR_1, "QQ567", 123, part_1_strategy),
            Hand(HandType.PAIR_1, "QQ567", 123, part_1_strategy),
            False,
        ),
        (
            Hand(HandType.PAIR_1, "QQ565", 321, part_1_strategy),
            Hand(HandType.PAIR_1, "QQ567", 509, part_1_strategy),
            True,
        ),
        (
            Hand(HandType.KIND_4, "J5555", 555, part_1_strategy),
            Hand(HandType.KIND_4, "T5555", 555, part_1_strategy),
            False,
        ),
        (
            Hand(HandType.KIND_4, "52TJJ", 555, part_1_strategy),
            Hand(HandType.KIND_4, "52TKK", 555, part_1_strategy),
            True,
        ),
    ],
)
def test_compare_hands(hand1: Hand, hand2: Hand, expected: bool):
    assert (hand1 < hand2) == expected


@pytest.mark.parametrize(
    "hand_str, expected",
    [
        ("23432 101", Hand(HandType.PAIR_2, "23432", 101, part_1_strategy)),
        ("AAAAA 28", Hand(HandType.KIND_5, "AAAAA", 28, part_1_strategy)),
    ],
)
def test_parse_to_hand(hand_str: str, expected: Hand):
    assert parse_to_hand(hand_str) == expected


def test_compute_part1_answer():
    lines = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()
    answer = calcuate_answer(lines, parse_func=parse_to_hand)
    assert answer == 6440


def test_compute_part2_answer():
    lines = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()
    answer = calcuate_answer(lines, parse_func=parse_to_hand_2)
    assert answer == 5905


def test_compute_part2_answer_2():
    lines = """JAAKK 1
JJJAK 2""".splitlines()
    answer = calcuate_answer(lines, parse_func=parse_to_hand_2)
    assert answer == 5


@pytest.mark.parametrize(
    "parse_func, expected",
    [(parse_to_hand, 6592), (parse_to_hand_2, 6839)],
)
def test_compute_both_parts(parse_func, expected: int):
    lines = """2345A 1
Q2KJJ 13
Q2Q2Q 19
T3T3J 17
T3Q33 11
2345J 3
J345A 2
32T3K 5
T55J5 29
KK677 7
KTJJT 34
QQQJA 31
JJJJJ 37
JAAAA 43
AAAAJ 59
AAAAA 61
2AAAA 23
2JJJJ 53
JJJJ2 41""".splitlines()
    answer = calcuate_answer(lines, parse_func=parse_func)
    assert answer == expected
