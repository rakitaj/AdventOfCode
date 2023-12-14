import pytest
from src.aoc2023.day04 import card_points, parse_line, cards_won, cards_won_algorithm


@pytest.mark.parametrize(
    "winning_nums, all_nums, expected",
    [
        ({41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53}, 8),
        ({13, 32, 20, 16, 61}, {61, 30, 68, 82, 17, 32, 24, 19}, 2),
        ({1, 21, 53, 59, 44}, {69, 82, 63, 72, 16, 21, 14, 1}, 2),
        ({41, 92, 73, 84, 69}, {59, 84, 76, 51, 58, 5, 54, 83}, 1),
        ({87, 83, 26, 28, 32}, {88, 30, 70, 12, 93, 22, 82, 36}, 0),
    ],
)
def test_card_points(winning_nums: set[int], all_nums: set[int], expected: int):
    actual = card_points(winning_nums, all_nums)
    assert actual == expected


@pytest.mark.parametrize(
    "card_id, set1, set2, expected",
    [
        (1, {41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53}, [2, 3, 4, 5]),
        (2, {13, 32, 20, 16, 61}, {61, 30, 68, 82, 17, 32, 24, 19}, [3, 4]),
        (3, {1, 21, 53, 59, 44}, {69, 82, 63, 72, 16, 21, 14, 1}, [4, 5]),
        (4, {41, 92, 73, 84, 69}, {59, 84, 76, 51, 58, 5, 54, 83}, [5]),
        (5, {87, 83, 26, 28, 32}, {88, 30, 70, 12, 93, 22, 82, 36}, []),
    ],
)
def test_cards_won(card_id: int, set1: set[int], set2: set[int], expected: list[int]):
    actual = cards_won(card_id, set1, set2)
    assert actual == expected


@pytest.mark.parametrize(
    "line, game_id, set1, set2",
    [
        (
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            1,
            {41, 48, 83, 86, 17},
            {83, 86, 6, 31, 17, 9, 48, 53},
        )
    ],
)
def test_parse_line(line: str, game_id: str, set1: set[int], set2: set[int]):
    parsed_game_id, parsed_set1, parsed_set2 = parse_line(line)
    assert parsed_game_id == game_id
    assert parsed_set1 == set1
    assert parsed_set2 == set2


def test_cards_won_algorithm():
    lines = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()
    card_array = cards_won_algorithm(lines)
    assert card_array == [1, 2, 4, 8, 14, 1]
    assert sum(card_array) == 30
