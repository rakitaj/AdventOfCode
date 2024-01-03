from typing import Sequence, Callable
from enum import IntEnum
from dataclasses import dataclass
from collections import Counter
from functools import cmp_to_key
from src.common.dataload import DataLoader, Answers


class HandType(IntEnum):
    KIND_5 = 7
    KIND_4 = 6
    FULL_HOUSE = 5
    KIND_3 = 4
    PAIR_2 = 3
    PAIR_1 = 2
    HIGH_CARD = 1


CARD_RANK = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
CARD_RANK_2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


@dataclass
class Hand:
    hand_type: HandType
    contents: str
    bid: int


def inner_hand_sort(rank_array: list[str], hand1: Hand, hand2: Hand) -> int:
    assert hand1.hand_type == hand2.hand_type
    for i, e in enumerate(hand1.contents):
        if rank_array.index(hand1.contents[i]) > rank_array.index(hand2.contents[i]):
            return 1
        if rank_array.index(hand2.contents[i]) > rank_array.index(hand1.contents[i]):
            return -1
    return 0


def compare_hands(hand1: Hand, hand2: Hand) -> int:
    """
    Compare two hands.
    -1 -> hand1 < hand2.
    0  -> hand1 == hand2.
    1  -> hand1 > hand2
    """
    if hand1.hand_type == hand2.hand_type:
        return inner_hand_sort(CARD_RANK, hand1, hand2)
    else:
        return hand1.hand_type - hand2.hand_type


def compare_hands_2(hand1: Hand, hand2: Hand) -> int:
    """
    Compare two hands.
    -1 -> hand1 < hand2.
    0  -> hand1 == hand2.
    1  -> hand1 > hand2
    """
    if hand1.hand_type == hand2.hand_type:
        return inner_hand_sort(CARD_RANK_2, hand1, hand2)
    else:
        return hand1.hand_type - hand2.hand_type


def parse_to_hand(line: str) -> Hand:
    hand_str, bid = line.split()
    counts = Counter(hand_str)
    hand_type = HandType.HIGH_CARD
    if 5 in counts.values():
        hand_type = HandType.KIND_5
    elif 4 in counts.values():
        hand_type = HandType.KIND_4
    elif 3 in counts.values() and 2 in counts.values():
        hand_type = HandType.FULL_HOUSE
    elif 3 in counts.values():
        hand_type = HandType.KIND_3
    elif 2 in counts.values():
        pair_count = 0
        for val in counts.values():
            if val == 2:
                pair_count += 1
        if pair_count == 1:
            hand_type = HandType.PAIR_1
        if pair_count == 2:
            hand_type = HandType.PAIR_2
    else:
        hand_type = HandType.HIGH_CARD
    return Hand(hand_type, hand_str, int(bid))


def parse_to_hand_2(line: str) -> Hand:
    hand_str, bid = line.split()
    counts = Counter(hand_str)
    hand_type = HandType.HIGH_CARD
    jack_count = counts["J"]
    if 5 in counts.values():
        hand_type = HandType.KIND_5
    elif 4 in counts.values():
        hand_type = HandType.KIND_4
        if jack_count in [1, 4]:
            hand_type = HandType.KIND_5
    elif 3 in counts.values() and 2 in counts.values():
        hand_type = HandType.FULL_HOUSE
        if jack_count in [2, 3]:
            hand_type = HandType.KIND_5
    elif 3 in counts.values():
        hand_type = HandType.KIND_3
        if jack_count in [1, 3]:
            hand_type = HandType.KIND_4
    elif 2 in counts.values():
        pair_count = 0
        for val in counts.values():
            if val == 2:
                pair_count += 1
        if pair_count == 1:
            hand_type = HandType.PAIR_1
            if jack_count == 1:
                hand_type = HandType.KIND_3
        if pair_count == 2:
            hand_type = HandType.PAIR_2
            if jack_count == 1:
                hand_type = HandType.FULL_HOUSE
            if jack_count == 2:
                hand_type = HandType.KIND_4
    else:
        hand_type = HandType.HIGH_CARD
    return Hand(hand_type, hand_str, int(bid))


def calcuate_answer(
    lines: Sequence[str],
    parse_func: Callable[[str], Hand],
    compare_func: Callable[[Hand, Hand], int],
) -> int:
    hands: list[Hand] = list()
    for line in lines:
        hand = parse_func(line)
        hands.append(hand)
    sorted_hands = sorted(hands, key=cmp_to_key(compare_func))
    total = 0
    for i, hand in enumerate(sorted_hands):
        total += hand.bid * (i + 1)
    return total


class Day07Answers(Answers):
    def __init__(self):
        loader = DataLoader(2023, "day07.txt")
        self.data = loader.readlines_str()

    def part1(self) -> int:
        answer = calcuate_answer(self.data, parse_to_hand, compare_hands)
        return answer

    def part2(self) -> int:
        answer = calcuate_answer(self.data, parse_to_hand_2, compare_hands_2)
        return answer
