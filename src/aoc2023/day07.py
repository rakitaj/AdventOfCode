from enum import IntEnum
from dataclasses import dataclass


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
