from src.common.dataload import Answers, DataLoader

def is_report_safe(numbers: list[int]) -> bool:
    direction = numbers[1] - numbers[0]
    for i in range(0, len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]
        if direction > 0:
            if diff > 3 or diff < 1:
                return False
        else:
            if diff < -3 or diff > -1:
                return False
    return True

class Day02Answers(Answers):

    def __init__(self) -> None:
        loader = DataLoader(2024, "day02.txt")
        self.data = loader.readlines_ints()

    def part1(self) -> str:
        total = 0
        for line in self.data:
            if is_report_safe(line):
                total += 1
        return str(total)
    
    def part2(self) -> str:
        return ""