from src.common.parsing import extract_integers
from src.common.dataload import Answers, DataLoader, timed


def parse_line(line: str) -> tuple[int, list[int]]:
    target, rest = line.split(":")
    nums = extract_integers(rest)
    return (int(target), nums)


def calculator(target: int, numbers: list[int], concat: bool) -> bool:
    start = numbers[0]
    rest = numbers[1:]
    if concat:
        return _calc_with_concat(target, rest, start)
    else:
        return _calc(target, rest, start)


def _calc(target: int, nums: list[int], acc: int) -> bool:
    if len(nums) < 1:
        return acc == target
    else:
        add = nums[0] + acc
        mult = nums[0] * acc
        return _calc(target, nums[1:], add) or _calc(target, nums[1:], mult)


def _calc_with_concat(target: int, nums: list[int], acc: int) -> bool:
    if len(nums) < 1:
        return acc == target
    else:
        add = acc + nums[0]
        mult = acc * nums[0]
        concat = str(acc) + str(nums[0])
        concat = int(concat)
        return _calc_with_concat(target, nums[1:], add) or _calc_with_concat(target, nums[1:], mult) or _calc_with_concat(target, nums[1:], concat)


class Day07Answers(Answers):

    def __init__(self) -> None:
        loader = DataLoader(2024, "day07.txt")
        self.lines = loader.readlines_str()

    def part1(self) -> str:
        total = 0
        for line in self.lines:
            target, nums = parse_line(line)
            can_be_calculated = calculator(target, nums, False)
            if can_be_calculated:
                total += target
        return str(total)

    @timed
    def part2(self) -> str:
        total = 0
        for line in self.lines:
            target, nums = parse_line(line)
            can_be_calculated = calculator(target, nums, True)
            if can_be_calculated:
                total += target
        return str(total)
