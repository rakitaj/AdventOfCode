from typing import Callable
from src.common.parsing import extract_integers
from src.common.dataload import Answers, DataLoader, timed


def parse_line(line: str) -> tuple[int, list[int]]:
    target, rest = line.split(":")
    nums = extract_integers(rest)
    return (int(target), nums)


def calculator(target: int, numbers: list[int]) -> bool:
    start = numbers[0]
    rest = numbers[1:]
    return _calc(target, rest, start)


def _calc(target: int, nums: list[int], acc: int) -> bool:
    if len(nums) < 1:
        return acc == target
    else:
        add = nums[0] + acc
        mult = nums[0] * acc
        return _calc(target, nums[1:], add) or _calc(target, nums[1:], mult)


def calculator_backwards_with_concat(target: int, numbers: list[int]) -> bool:
    return _calc_with_concat(target, numbers)


def _calc_with_concat(acc: int, nums: list[int]) -> bool:
    n = nums[-1]

    if len(nums) == 1:
        # Must use the identity result. 1 for multiplication, 0 for addition.
        result = acc / n == 1 or acc - n == 0 or str(acc) == str(n)
        return result

    if acc - n >= 0:
        new_acc = acc - n
        add_possible = _calc_with_concat(new_acc, nums[:-1])
    else:
        add_possible = False
    if acc % n == 0:
        new_acc = acc // n
        mult_possible = _calc_with_concat(new_acc, nums[:-1])
    else:
        mult_possible = False
    if str(acc).endswith(str(n)) and len(str(acc).removesuffix(str(n))) > 0:
        new_acc = str(acc).removesuffix(str(n))
        new_acc = int(new_acc)
        concat_possible = _calc_with_concat(new_acc, nums[:-1])
    else:
        concat_possible = False
    return add_possible or mult_possible or concat_possible


class Day07Answers(Answers):

    def __init__(self) -> None:
        loader = DataLoader(2024, "day07.txt")
        self.lines = loader.readlines_str()

    def part1(self) -> str:
        total = 0
        for line in self.lines:
            target, nums = parse_line(line)
            can_be_calculated = calculator(target, nums)
            if can_be_calculated:
                total += target
        return str(total)

    @timed
    def part2(self) -> str:
        total = 0
        for line in self.lines:
            target, nums = parse_line(line)
            can_be_calculated = calculator_backwards_with_concat(target, nums)
            if can_be_calculated:
                total += target
        return str(total)
