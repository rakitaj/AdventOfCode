from typing import Sequence
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


def card_rank(rank: str) -> int:
    match rank:
        case "A":
            return 14
        case "K":
            return 13
        case "Q":
            return 12
        case "J":
            return 11
        case "T":
            return 10
        case _:
            return int(rank)


@dataclass
class Hand:
    hand_type: HandType
    contents: str
    bid: int


def inner_hand_sort(hand1: Hand, hand2: Hand) -> int:
    assert hand1.hand_type == hand2.hand_type
    for i in range(len(hand1.contents)):
        if card_rank(hand1.contents[i]) > card_rank(hand2.contents[i]):
            return 1
        if card_rank(hand2.contents[i]) > card_rank(hand1.contents[i]):
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
        return inner_hand_sort(hand1, hand2)
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


def parse_many_hands(lines: Sequence[str]) -> list[Hand]:
    hands: list[Hand] = list()
    for line in lines:
        hand = parse_to_hand(line)
        hands.append(hand)
    return hands


def calcuate_part1_answer(lines: Sequence[str]) -> int:
    hands = parse_many_hands(lines)
    sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))
    total = 0
    for i, hand in enumerate(sorted_hands):
        total += hand.bid * (i + 1)
    return total


class Day07Answers(Answers):
    def __init__(self):
        loader = DataLoader(2023, "day07.txt")
        self.data = loader.readlines_str()

    def part1(self) -> int:
        answer = calcuate_part1_answer(self.data)
        return answer

    def part2(self) -> int:
        return -1
