from src.common.dataload import DataLoader, Answers
from src.common.parsing import extract_integer
from src.common.extensions import must
from typing import Sequence


def parse_line(line: str) -> tuple[int, set[int], set[int]]:
    card_part, rest = line.split(":")
    card_num = must(extract_integer(card_part))
    winnings_nums, card_nums = rest.split("|")
    winnings_nums_set = set(map(int, winnings_nums.split()))
    card_nums_set = set(map(int, card_nums.split()))
    return (card_num, winnings_nums_set, card_nums_set)


def card_points(winning_nums: set[int], card_nums: set[int]) -> int:
    intersection = winning_nums.intersection(card_nums)
    num_winning = len(intersection)
    if num_winning == 0:
        return 0
    return 1 * (2 ** (num_winning - 1))


def cards_won(card_id: int, set1: set[int], set2: set[int]) -> list[int]:
    """Checks a card's winning numbers and returns a list of the card numbers won."""
    intersection = set1.intersection(set2)
    num_winning = len(intersection)
    return list(range(card_id + 1, card_id + num_winning + 1))


def part01_answer() -> str:
    loader = DataLoader(2023, "day04.txt")
    lines = loader.readlines_str()
    total = 0
    for line in lines:
        game_id, set1, set2 = parse_line(line)
        points = card_points(set1, set2)
        total += points
    return str(total)


def cards_won_algorithm(lines: Sequence[str]) -> list[int]:
    cards = [1] * len(lines)
    for i, val in enumerate(cards):
        card_id, set1, set2 = parse_line(lines[i])
        card_ids_won = cards_won(card_id, set1, set2)
        for card_id in card_ids_won:
            cards[card_id - 1] += val
    return cards


class Day04Answers(Answers):
    def __init__(self):
        loader = DataLoader(2023, "day04.txt")
        self.data = loader.readlines_str()

    def part1(self) -> str:
        total = 0
        for line in self.data:
            game_id, set1, set2 = parse_line(line)
            points = card_points(set1, set2)
            total += points
        return str(total)

    def part2(self) -> str:
        """
        5903503 - too low
        6189740 - correct
        """

        card_array = cards_won_algorithm(self.data)
        return str(sum(card_array))
