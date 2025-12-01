from src.common.dataload import Answers, DataLoader


def is_within_tolerance(numbers: list[int]) -> bool:
    direction = numbers[1] - numbers[0]
    for i in range(0, len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if direction > 0:
            if diff < 1 or diff > 3:
                return False
        else:
            if diff < -3 or diff > -1:
                return False
    return True


def is_within_tolerance_damped(numbers: list[int]) -> bool:
    for i in range(0, len(numbers)):
        with_one_dropped = numbers[:i] + numbers[i + 1 :]
        if is_within_tolerance(with_one_dropped):
            return True
    return False


class Day02Answers(Answers):
    def __init__(self) -> None:
        dataloader = DataLoader(2024, "day02.txt")
        self.data = dataloader.readlines_int()

    def part1(self) -> str:
        total = 0
        for row in self.data:
            if is_within_tolerance(row):
                total += 1
        return str(total)

    def part2(self) -> str:
        total = 0
        for row in self.data:
            if is_within_tolerance_damped(row):
                total += 1
        return str(total)
