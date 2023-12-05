# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53


def parse_line(line: str) -> tuple[str, set[int], set[int]]:
    card_num, rest = line.split(":")
    winnings_nums, card_nums = rest.split("|")
    # winnings_nums_set = set([int(n) for n in winnings_nums.split()])
    # card_nums_set = set([int(n) for n in card_nums.split()])
    winnings_nums_set = set(map(int, winnings_nums.split()))
    card_nums_set = set(map(int, card_nums.split()))
    return (card_num, winnings_nums_set, card_nums_set)


def card_points(winning_nums: set[int], card_nums: set[int]) -> int:
    intersection = winning_nums.intersection(card_nums)
    num_winning = len(intersection)
    if num_winning == 0:
        return 0
    return 1 * (2 ** (num_winning - 1))
