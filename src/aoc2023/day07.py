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


@dataclass
class Hand:
    hand_type: HandType
    contents: str


def inner_hand_sort(hand1: Hand, hand2: Hand) -> int:
    # for i in range(len(hand1.contents)):
    #     if hand1.contents[i] != hand2.contents[i]:
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
