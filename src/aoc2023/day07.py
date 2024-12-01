from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from enum import IntEnum
from typing import Callable, Sequence

from src.common.dataload import Answers, DataLoader


class HandType(IntEnum):
    KIND_5 = 7
    KIND_4 = 6
    FULL_HOUSE = 5
    KIND_3 = 4
    PAIR_2 = 3
    PAIR_1 = 2
    HIGH_CARD = 1


@dataclass
class Hand:
    hand_type: HandType
    contents: str
    bid: int
    rank_strategy: Callable[[Hand], list[str]]

    CARD_RANK = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    CARD_RANK_2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

    def __eq__(self, other: object) -> bool:
        
        return (
            isinstance(other, Hand) and
            (self.hand_type == other.hand_type)
            and (self.contents == other.contents)
            and (self.rank_strategy(self) == other.rank_strategy(self))
        )

    def __lt__(self, other: Hand) -> bool:
        rank_algo = self.rank_strategy(self)

        if other.hand_type == self.hand_type:
            for i, e in enumerate(self.contents):
                if rank_algo.index(self.contents[i]) < rank_algo.index(other.contents[i]):
                    return True
                if rank_algo.index(self.contents[i]) > rank_algo.index(other.contents[i]):
                    return False
            return False
        else:
            return self.hand_type < other.hand_type


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
    return Hand(hand_type, hand_str, int(bid), lambda x: x.CARD_RANK)


def parse_to_hand_2(line: str) -> Hand:
    hand_str, bid = line.split()
    counts = Counter(hand_str)
    hand_type = HandType.HIGH_CARD
    jack_count = counts["J"]
    if 5 in counts.values():
        hand_type = HandType.KIND_5
    elif 4 in counts.values() and "J" in counts:
        hand_type = HandType.KIND_5
    elif 4 in counts.values():
        hand_type = HandType.KIND_4
    elif 3 in counts.values() and 2 in counts.values() and "J" in counts:
        hand_type = HandType.KIND_5
    elif 3 in counts.values() and 2 in counts.values():
        hand_type = HandType.FULL_HOUSE
    elif 3 in counts.values() and "J" in counts and (counts["J"] == 3 or counts["J"] == 1):
        hand_type = HandType.KIND_4
    elif 3 in counts.values():
        hand_type = HandType.KIND_3
    elif 2 in counts.values():
        pair_count = len([x for x in counts.values() if x == 2])
        if pair_count == 2 and "J" in counts and counts["J"] == 2:
            hand_type = HandType.KIND_4
        elif pair_count == 2 and "J" in counts and counts["J"] == 1:
            hand_type = HandType.FULL_HOUSE
        elif pair_count == 2:
            hand_type = HandType.PAIR_2
        elif pair_count == 1 and "J" in counts:
            hand_type = HandType.KIND_3
        elif pair_count == 1:
            hand_type = HandType.PAIR_1
    else:
        if "J" in counts:
            hand_type = HandType.PAIR_1
        else:
            hand_type = HandType.HIGH_CARD

    return Hand(hand_type, hand_str, int(bid), lambda x: x.CARD_RANK_2)


def calcuate_answer(lines: Sequence[str], parse_func: Callable[[str], Hand]) -> int:
    hands: list[Hand] = list()
    for line in lines:
        hand = parse_func(line)
        hands.append(hand)
    sorted_hands = sorted(hands)
    total = 0
    for i, hand in enumerate(sorted_hands):
        total += hand.bid * (i + 1)
    return total


class Day07Answers(Answers):
    def __init__(self) -> None:
        loader = DataLoader(2023, "day07.txt")
        self.data = loader.readlines_str()

    def part1(self) -> str:
        answer = calcuate_answer(self.data, parse_to_hand)
        return str(answer)

    def part2(self) -> str:
        answer = calcuate_answer(self.data, parse_to_hand_2)
        return str(answer)
